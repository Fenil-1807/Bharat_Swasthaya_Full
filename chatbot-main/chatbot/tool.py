from typing import Optional
import os
from langchain_core.tools import tool
import requests
from rag import retrieve_and_rerank
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

HEALTH_API_BASE_URL = os.getenv("HEALTH_API_BASE_URL")

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

GOOGLE_MAPS_API_KEY = os.environ["GOOGLE_MAPS_API_KEY"]


@tool
def google_search(query: str) -> str:
    """
    Search the internet for general-purpose information.

    Use this tool when:
    - Current information is required
    - The user explicitly asks to search the web
    - Recent news or announcements are needed
    - Information is not available in the knowledge base
    - Information about people, companies, products, places,
      technologies, or other general topics is required
    """

    try:
        response = tavily_client.search(
            query=query,
            search_depth="basic",
            topic="general",
            max_results=3,
            include_answer=True
        )

        output = []
        answer = response.get("answer")

        if answer:
            output.append(f"Summary:\n{answer}")

        results = response.get("results", [])

        if not results:
            return "No relevant search results found."

        output.append("\nSearch Results:")

        for i, result in enumerate(results, 1):

            title = result.get("title", "")
            url = result.get("url", "")
            content = result.get("content", "")

            output.append(
                f"""
{i}. {title}

URL: {url}

Content:
{content}
"""
            )

        return "\n".join(output)

    except Exception as e:
        return f"Search failed: {str(e)}"

@tool
def calculate_distance(
    origin: str,
    destination: str
) -> str:
    """
    Calculate driving distance and estimated travel time
    between the user's location and a healthcare facility.

    Returns distance in kilometers and travel time in minutes.
    """

    url = "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": "routes.distanceMeters,routes.duration",
    }

    body = {
        "origin": {
            "address": origin
        },
        "destination": {
            "address": destination
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=body,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        if not data.get("routes"):
            return "Could not calculate the distance."

        route = data["routes"][0]

        distance_meters = route["distanceMeters"]
        distance_km = distance_meters / 1000

        duration_seconds = float(
            route["duration"].rstrip("s")
        )

        duration_minutes = round(
            duration_seconds / 60
        )

        return (
            f"Distance: {distance_km:.2f} km.\n"
            f"Estimated travel time: {duration_minutes} minutes."
        )

    except requests.exceptions.Timeout:
        return "Route calculation timed out."

    except requests.exceptions.RequestException:
        return "Unable to calculate the route."

    except (KeyError, ValueError, TypeError):
        return "Unable to process route information."

@tool
def find_healthcare_facility(
    location: str,
    facility_type: str
) -> str:
    """
    Search the web (via Tavily) for healthcare facilities near a location.
    """

    query = f"best {facility_type} near {location} India contact number address"

    try:
        response = tavily_client.search(
            query=query,
            search_depth="basic",
            max_results=5,
            include_answer=True,
        )

        results = []

        if response.get("answer"):
            results.append(f"Summary: {response['answer']}")

        for item in response.get("results", []):
            title = item.get("title", "Unknown")
            url = item.get("url", "")
            content = item.get("content", "")[:300]

            results.append(
                f"Name/Title: {title}\n"
                f"Snippet: {content}\n"
                f"Source: {url}"
            )

        if not results:
            return "No results found."

        return "\n\n".join(results)

    except Exception as e:
        return f"Failed to search healthcare facilities: {str(e)}"

@tool
def government_scheme_rag(query:str)->str:
    """
    Retrieve information about Indian government healthcare
    schemes from the BharatSwasthya knowledge base.

    Use this tool when the user asks about:
    - Government healthcare schemes
    - Scheme eligibility
    - Benefits provided by a scheme
    - Required documents
    - Application or enrollment process
    - Coverage and financial assistance
    - Beneficiary requirements
    - Scheme-specific rules and guidelines

    This tool searches the stored government-scheme documents
    using semantic similarity search and returns the most
    relevant information.

    Do NOT use this tool for:
    - Diagnosing diseases
    - Symptoms or medical conditions
    - Finding hospitals or PHCs
    - Hospital distance or travel time
    - Emergency services
    - Current facility availability
    - General web searches

    Args:
        query: The user's question about a government
               healthcare scheme.

    Returns:
        Relevant government healthcare scheme information
        from the knowledge base.
    """

    context = retrieve_and_rerank(query)

    return context

@tool
def proactive_guidance(state: str, district: str, city: Optional[str] = None) -> str:
    """
    Retrieve daily proactive AI disease forecasts and preventive healthcare guidance
    correlated with meteorological weather factors (humidity, rainfall, heatwave indices, air quality).

    Use this tool when:
    - You know the user's Indian state and district (and optionally city) and want to provide proactive, preventive healthcare guidance.
    - Answering questions about seasonal disease forecasts or weather-correlated disease risks.
    - Providing preventive measures based on current climate and environmental conditions.

    Args:
        state: Indian State name (e.g., 'Maharashtra', 'Delhi', 'Karnataka').
        district: Indian District name (e.g., 'Ahmedabad', 'Bengaluru Urban', 'Central Delhi').
        city: Optional city or village name (e.g., 'Pune', 'Bengaluru').

    Returns:
        Proactive AI advisory and preventive healthcare guidance.
    """
    url = "https://proactivellm.onrender.com/api/v1/proactive-advisory"
    payload = {
        "state": state.strip(),
        "district": district.strip()
    }
    if city and city.strip():
        payload["city"] = city.strip()

    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        res_json = response.json()

        llm_output = res_json.get("llm_output")
        if llm_output:
            return llm_output

        return f"No proactive guidance available for {district}, {state}."

    except requests.exceptions.ConnectionError:
        return "Unable to connect to the proactive advisory server. Please ensure the service is running."
    except requests.exceptions.Timeout:
        return "Proactive guidance service timed out."
    except requests.exceptions.HTTPError as e:
        return f"Proactive guidance service error ({e.response.status_code}): {e.response.text}"
    except Exception as e:
        return f"Failed to retrieve proactive guidance: {str(e)}"

@tool
def regional_disease_alert(state: str, district: str, city: Optional[str] = None) -> str:
    """
    Retrieve active viral disease outbreaks, case counts, clinical protocols,
    and doctor observations for a specific state, district, or city in India.

    Use this tool when:
    - The user asks about disease outbreaks, viral infections, or illness clusters in their area.
    - Checking if an area (state/district/city) is currently experiencing viral outbreaks (e.g. Dengue, H3N2, etc.).
    - Retrieving clinical protocols, danger signs, doctor diagnoses, and precautions for active outbreaks.
    - You can also use this if you want to know user's current symptoms meet with viral disease.

    Args:
        state: Filter by Indian State (e.g., 'Maharashtra', 'Gujarat').
        district: Filter by District (e.g., 'Pune', 'Mumbai Suburban').
        city: Optional filter by City or Village (e.g., 'Shivajinagar', 'Hadapsar', 'Andheri').

    Returns:
        Active viral disease outbreak data including case numbers, severity, symptoms,
        danger signs, doctor remarks, and treatment/management protocols.
    """
    url = f"{HEALTH_API_BASE_URL}/api/v1/public/viral-diseases"
    params = {
        "state": state.strip(),
        "district": district.strip()
    }
    if city and city.strip():
        params["city"] = city.strip()

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        res_json = response.json()

        data = res_json.get("data", {})
        diseases = data.get("data", [])

        loc_str = f"{city + ', ' if city else ''}{district}, {state}"

        if not diseases:
            return f"No active viral disease outbreaks reported for {loc_str}."

        formatted_diseases = []
        for i, disease in enumerate(diseases, 1):
            name = disease.get("diseaseName", "Unknown Disease")
            st = disease.get("state", state)
            dist = disease.get("district", district)
            affected_cities = ", ".join(disease.get("affectedCities", [])) or "All"
            total_cases = disease.get("totalCases", 0)
            active_reports = disease.get("activeReportsCount", 0)
            severity = str(disease.get("highestSeverity", "N/A")).upper()
            recent_date = disease.get("recentReportDate", "N/A")
            is_viral = "Yes" if disease.get("isViral") else "No"
            transmission = disease.get("transmissionType", "N/A")
            incubation = disease.get("incubationPeriod", "N/A")
            seasonal_risk = disease.get("seasonalRisk", "N/A")
            high_risk_groups = disease.get("highRiskGroups", "N/A")
            clinical_protocol = disease.get("clinicalProtocol", "N/A")

            symptoms = disease.get("symptoms", [])
            symptoms_str = "\n".join(f"  • {s}" for s in symptoms) if symptoms else "  • None specified"

            danger_signs = disease.get("dangerSigns", [])
            danger_signs_str = "\n".join(f"  • {d}" for d in danger_signs) if danger_signs else "  • None specified"

            precautions = disease.get("recommendedPrecautions", [])
            precautions_str = "\n".join(f"  • {p}" for p in precautions) if precautions else "  • None specified"

            doctor_remarks = disease.get("doctorRemarks", [])
            remarks_str = "\n".join(f"  • {r}" for r in doctor_remarks) if doctor_remarks else "  • None"

            doctor_diagnoses = disease.get("doctorDiagnoses", [])
            diagnoses_str = "\n".join(f"  • {diag}" for diag in doctor_diagnoses) if doctor_diagnoses else "  • None"

            prescribed_actions = disease.get("prescribedActions", [])
            actions_str = "\n".join(f"  • {a}" for a in prescribed_actions) if prescribed_actions else "  • None"

            formatted_diseases.append(
                f"--- Outbreak {i}: {name} ---\n"
                f"• Viral Disease: {is_viral}\n"
                f"• Severity: {severity}\n"
                f"• Location: State: {st}, District: {dist}, Affected Area(s): {affected_cities}\n"
                f"• Total Cases: {total_cases} | Active Field Reports: {active_reports} | Recent Date: {recent_date}\n"
                f"• Transmission: {transmission}\n"
                f"• Incubation Period: {incubation}\n"
                f"• Seasonal Risk: {seasonal_risk}\n"
                f"• High Risk Groups: {high_risk_groups}\n"
                f"• Key Symptoms:\n{symptoms_str}\n"
                f"• Danger Signs (Urgent Care Needed):\n{danger_signs_str}\n"
                f"• Doctor Diagnoses / Field Findings:\n{diagnoses_str}\n"
                f"• Doctor Remarks:\n{remarks_str}\n"
                f"• Prescribed Actions:\n{actions_str}\n"
                f"• Recommended Precautions:\n{precautions_str}\n"
                f"• Clinical Management Protocol: {clinical_protocol}"
            )

        return f"Active Viral Disease Outbreaks for {loc_str} ({len(diseases)} found):\n\n" + "\n\n".join(formatted_diseases)

    except requests.exceptions.ConnectionError:
        return f"Unable to connect to the disease intelligence server at {HEALTH_API_BASE_URL}. Please ensure the service is running or check HEALTH_API_BASE_URL."
    except requests.exceptions.Timeout:
        return "Viral diseases service timed out."
    except requests.exceptions.HTTPError as e:
        return f"Viral diseases service error ({e.response.status_code}): {e.response.text}"
    except Exception as e:
        return f"Failed to retrieve viral disease data: {str(e)}"


@tool
def hospital_bed_availability(
    hospital_name: Optional[str] = None,
    district: Optional[str] = None,
    state: Optional[str] = None,
    city: Optional[str] = None,
    ward_type: Optional[str] = None,
) -> str:
    """
    Retrieve real-time hospital bed capacity, vacant vs occupied counts,
    ICU units, ward-level breakdown, daily pricing, amenities, and scheme coverage
    for a specific hospital or Indian District/State/City.

    Use this tool when:
    - The user asks for hospital beds, vacant beds, ward rates, or bed availability for a specific hospital or an area.
    - The user specifies a hospital name (e.g., 'KEM Memorial', 'Sassoon Hospital', 'Civil Hospital', 'AIIMS').
    - The user is looking for ICU, NICU, Emergency / Casualty, General Ward, Semi-Private, or Isolation beds.
    - The user asks about per-day hospital bed charges, scheme coverage (e.g. Ayushman Bharat / MJPJAY), or ward amenities.
    - The user needs contact numbers and addresses of hospitals with available beds.

    Args:
        hospital_name: Optional filter or search by Hospital Name (e.g., 'KEM Memorial', 'Sassoon', 'Civil Hospital').
        district: Optional filter by District / City (e.g., 'Pune', 'Ahmedabad', 'Bengaluru Urban', 'Mumbai').
        state: Optional filter by Indian State (e.g., 'Maharashtra', 'Gujarat', 'Delhi').
        city: Optional filter by City / Taluk (e.g., 'Shivajinagar', 'Hadapsar').
        ward_type: Optional filter for specific ward name (e.g., 'ICU', 'General Ward', 'Emergency', 'NICU', 'Isolation Ward').

    Returns:
        Structured hospital bed availability and ward data, or fallback search results if not in registry.
    """
    target_str = hospital_name.strip() if hospital_name and hospital_name.strip() else ""
    loc_parts = [p.strip() for p in [city, district, state] if p and p.strip()]
    loc_str = ", ".join(loc_parts) if loc_parts else ""

    if target_str and loc_str:
        query_subject = f"{target_str} ({loc_str})"
    elif target_str:
        query_subject = target_str
    elif loc_str:
        query_subject = loc_str
    else:
        query_subject = "specified location"

    params = {}
    if target_str:
        params["search"] = target_str
    if district and district.strip():
        params["district"] = district.strip()
    if state and state.strip():
        params["state"] = state.strip()
    if city and city.strip():
        params["city"] = city.strip()

    # 1. Query Custom Hospital Bed API
    urls_to_try = []
    if HEALTH_API_BASE_URL:
        urls_to_try.append(f"{HEALTH_API_BASE_URL.rstrip('/')}/api/v1/public/hospital-beds")
    if "https://decodesih-website.onrender.com/api/v1/public/hospital-beds" not in urls_to_try:
        urls_to_try.append("https://decodesih-website.onrender.com/api/v1/public/hospital-beds")

    api_data = None
    for url in urls_to_try:
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                res_json = response.json()
                api_data = res_json.get("data", {})
                break
        except Exception:
            continue

    hospitals = api_data.get("hospitals", []) if api_data else []
    summary = api_data.get("summary", {}) if api_data else {}

    # If live hospital bed data is present in database
    if hospitals and summary.get("totalHospitals", 0) > 0:
        formatted_hospitals = []
        for i, h in enumerate(hospitals, 1):
            h_name = h.get("hospitalName", "Unknown Hospital")
            h_addr = h.get("address", "N/A")
            h_phone = h.get("phone", "N/A")
            total_b = h.get("totalBeds", 0)
            vacant_b = h.get("vacantBeds", 0)
            occ_rate = h.get("occupancyRate", 0)
            min_p = h.get("minPrice")
            max_p = h.get("maxPrice")
            price_range = f"Rs. {min_p} - Rs. {max_p}/day" if (min_p is not None and max_p is not None) else "N/A"

            ward_lines = []
            for w in h.get("wards", []):
                w_name = w.get("displayName") or w.get("wardType") or "Ward"
                # If ward_type filter is given and does not match, skip if filtering requested
                if ward_type and ward_type.lower() not in w_name.lower():
                    continue

                w_total = w.get("totalBeds", 0)
                w_vacant = w.get("vacantBeds", 0)
                w_price = w.get("pricePerDay", "N/A")
                w_occ = w.get("occupancyRate", 0)
                amenities = ", ".join(w.get("amenities", []))
                notes = w.get("notes", "")

                w_info = f"    • {w_name}: {w_vacant} vacant / {w_total} total | Price: Rs. {w_price}/day (Occupancy: {w_occ}%)"
                if amenities:
                    w_info += f"\n      - Amenities: {amenities}"
                if notes:
                    w_info += f"\n      - Note: {notes}"
                ward_lines.append(w_info)

            # If ward_type filter was specified but didn't match any ward for this hospital, include all wards
            if not ward_lines and ward_type:
                for w in h.get("wards", []):
                    w_name = w.get("displayName") or w.get("wardType") or "Ward"
                    w_total = w.get("totalBeds", 0)
                    w_vacant = w.get("vacantBeds", 0)
                    w_price = w.get("pricePerDay", "N/A")
                    ward_lines.append(f"    • {w_name}: {w_vacant} vacant / {w_total} total | Rs. {w_price}/day")

            wards_str = "\n".join(ward_lines) if ward_lines else "    • No ward details listed."

            formatted_hospitals.append(
                f"--- Hospital {i}: {h_name} ---\n"
                f"• Address: {h_addr}\n"
                f"• Phone / Helpline: {h_phone}\n"
                f"• Total Bed Vacancy: {vacant_b} vacant out of {total_b} total beds (Occupancy: {occ_rate}%)\n"
                f"• Daily Price Range: {price_range}\n"
                f"• Wards & Bed Status:\n{wards_str}"
            )

        summary_header = (
            f"Live Hospital Bed Availability for {query_subject}:\n"
            f"• Total Registered Hospitals: {summary.get('totalHospitals', len(hospitals))}\n"
            f"• Overall Available Beds: {summary.get('totalVacantBeds', 0)} vacant / {summary.get('totalBeds', 0)} total\n"
            f"• ICU Available Beds: {summary.get('icuVacantBeds', 0)} vacant / {summary.get('icuTotalBeds', 0)} total\n"
            f"• Area Occupancy Rate: {summary.get('occupancyRate', 0)}%\n\n"
        )

        return summary_header + "\n\n".join(formatted_hospitals)

    # 2. FALLBACK: If hospital bed data is not yet in the database, use Tavily Search
    if target_str and loc_str:
        query = f"{target_str} hospital {ward_type or ''} {loc_str} contact number address"
    elif target_str:
        query = f"{target_str} hospital {ward_type or ''} contact number address"
    else:
        query = f"hospitals {ward_type or ''} near {loc_str or 'India'} contact number address"

    try:
        response = tavily_client.search(
            query=query,
            search_depth="basic",
            max_results=4,
            include_answer=True,
        )

        results = []
        if response.get("answer"):
            results.append(f"Overview: {response['answer']}")

        for item in response.get("results", []):
            title = item.get("title", "Unknown")
            url = item.get("url", "")
            content = item.get("content", "")[:250]
            results.append(f"• {title}\n  Details: {content}\n  Source: {url}")

        if not results:
            return f"No hospitals or bed data found for {query_subject}."

        return (
            f"[NOTE: Real-time bed tracking is currently not linked in the registry for {query_subject} yet.]\n"
            f"Here are verified healthcare facilities found in the area via web search:\n\n"
            + "\n\n".join(results)
            + "\n\nPlease instruct the user to call the hospital helpline directly to verify real-time bed and ICU availability."
        )

    except Exception as e:
        return f"Failed to retrieve hospital bed data: {str(e)}"
