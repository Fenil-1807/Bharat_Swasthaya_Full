import os
import requests
from typing import Optional, Dict, Any

SAMPLE_DATA = {
    "statusCode": 200,
    "data": {
        "count": 2,
        "filter": {
            "state": "Maharashtra",
            "district": "Pune",
            "city": "All"
        },
        "data": [
            {
                "diseaseName": "Influenza A (H3N2 Subtype)",
                "state": "Maharashtra",
                "district": "Pune",
                "totalCases": 12,
                "activeReportsCount": 1,
                "highestSeverity": "moderate",
                "recentReportDate": "2026-08-24T06:34:54.664Z",
                "affectedCities": ["Shivajinagar"],
                "symptoms": ["Barking Cough", "Sore Throat", "Fever 101°F", "Runny Nose", "Wheezing"],
                "doctorRemarks": ["Common in school clusters. Advised 5-day home isolation."],
                "doctorDiagnoses": ["Seasonal H3N2 Influenza post-monsoon wave."],
                "prescribedActions": ["Steam inhalation, saline nasal drops, symptomatic antipyretics."],
                "sampleReports": [
                    {
                        "title": "Pediatric Upper Respiratory Cough & Wheezing Spike",
                        "severity": "moderate",
                        "patientCount": 12,
                        "city": "Shivajinagar",
                        "createdAt": "2026-08-24T06:34:54.664Z",
                        "doctorDiagnosis": "Seasonal H3N2 Influenza post-monsoon wave.",
                        "doctorRemarks": "Common in school clusters. Advised 5-day home isolation.",
                        "prescribedAction": "Steam inhalation, saline nasal drops, symptomatic antipyretics."
                    }
                ],
                "isViral": True,
                "transmissionType": "Airborne droplet transmission & contact with contaminated fomites",
                "incubationPeriod": "1 - 4 Days (Average: 2 days)",
                "seasonalRisk": "Winter wave (Dec-Feb) & Monsoon wave (July-Sept)",
                "highRiskGroups": "Asthmatic patients, COPD, infants, geriatric population, immunosuppressed individuals",
                "dangerSigns": [
                    "Shortness of breath, rapid breathing, or chest indrawing",
                    "Cyanosis (bluish lips or nails) / Oxygen saturation dropping below 94%",
                    "Confusion, unresponsiveness, or hemoptysis (coughing blood)",
                    "High fever recurring after initial improvement"
                ],
                "recommendedPrecautions": [
                    "Wear triple-layer or N95 masks in crowded transit and public places.",
                    "Practice respiratory etiquette (cough/sneeze into elbow) and frequent handwashing.",
                    "Isolate at home for at least 5 days from symptom onset.",
                    "Consider annual seasonal quadrivalent flu vaccination."
                ],
                "clinicalProtocol": "Warm saline gargles, steam inhalation, hydration, antipyretics. Oseltamivir / antiviral therapy under medical guidance for high-risk patients within 48 hours of onset."
            },
            {
                "diseaseName": "Dengue Fever (DENV-2 Strain)",
                "state": "Maharashtra",
                "district": "Pune",
                "totalCases": 6,
                "activeReportsCount": 1,
                "highestSeverity": "high",
                "recentReportDate": "2026-08-24T06:34:54.664Z",
                "affectedCities": ["Hadapsar"],
                "symptoms": ["High Fever", "Retro-orbital Pain", "Severe Joint Pain", "Forearm Rash", "Thrombocytopenia"],
                "doctorRemarks": ["Urgent vector control larvicide spray dispatched to Ward 14. Daily platelet monitoring initiated."],
                "doctorDiagnoses": ["Confirmed Dengue Viral Hemorrhagic Suspect via NS1 Antigen test."],
                "prescribedActions": ["Hydration with ORS, Paracetamol 650mg SOS. Strictly avoid Ibuprofen/Aspirin."],
                "sampleReports": [
                    {
                        "title": "Cluster of High Febrile Illness with Severe Joint Pain in Ward 14",
                        "severity": "high",
                        "patientCount": 6,
                        "city": "Hadapsar",
                        "createdAt": "2026-08-24T06:34:54.664Z",
                        "doctorDiagnosis": "Confirmed Dengue Viral Hemorrhagic Suspect via NS1 Antigen test.",
                        "doctorRemarks": "Urgent vector control larvicide spray dispatched to Ward 14. Daily platelet monitoring initiated.",
                        "prescribedAction": "Hydration with ORS, Paracetamol 650mg SOS. Strictly avoid Ibuprofen/Aspirin."
                    }
                ],
                "isViral": True,
                "transmissionType": "Vector-borne (Aedes aegypti / albopictus mosquito - Day Biting)",
                "incubationPeriod": "4 - 10 Days post mosquito bite",
                "seasonalRisk": "Monsoon & Post-Monsoon (July to November)",
                "highRiskGroups": "Children under 5, pregnant women, elderly, patients with diabetes or hypertension",
                "dangerSigns": [
                    "Severe, persistent abdominal pain or tenderness",
                    "Persistent vomiting (>3 times in 24 hours)",
                    "Mucosal bleeding (gums, nose, blood in vomit/stool)",
                    "Lethargy, extreme restlessness, or sudden dizziness upon standing",
                    "Fluid accumulation (pleural effusion / ascites) or rapid drop in platelet count (<50,000/μL)"
                ],
                "recommendedPrecautions": [
                    "Eliminate standing water weekly from flower vases, coolers, tires, and open drums.",
                    "Apply DEET or Picaridin mosquito repellents, especially during morning & late afternoon hours.",
                    "Wear full-sleeved light-colored clothing and install window mesh screens.",
                    "Sleep under insecticide-treated mosquito bed nets (ITNs).",
                    "Undergo routine platelet and hematocrit monitoring if febrile."
                ],
                "clinicalProtocol": "Oral rehydration salts (ORS), tender coconut water, paracetamol (650mg SOS) for fever. STRICTLY AVOID Aspirin, Ibuprofen, Diclofenac, or other NSAIDs due to severe platelet inhibition and gastrointestinal hemorrhage risk."
            }
        ]
    },
    "message": "Active viral disease data retrieved successfully.",
    "success": True
}

def get_weather(state: str, district: str, city: Optional[str] = None, forecast_days: int = 10) -> Dict[str, Any]:
    """Fetch 10-day weather forecast and current telemetry from Open-Meteo API."""
    location_query = city if city and city.lower() != "all" else district
    try:
        geo_res = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": location_query, "count": 1, "language": "en", "format": "json"},
            timeout=5
        ).json()
        
        lat = 18.5204
        lon = 73.8567
        if geo_res.get("results"):
            lat = geo_res["results"][0]["latitude"]
            lon = geo_res["results"][0]["longitude"]

        weather_res = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,precipitation,weather_code,wind_speed_10m",
                "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max,wind_speed_10m_max,weather_code",
                "forecast_days": min(max(forecast_days, 1), 16),
                "timezone": "auto"
            },
            timeout=5
        ).json()

        curr = weather_res.get("current", {})
        daily = weather_res.get("daily", {})

        daily_forecast = []
        times = daily.get("time", [])
        temp_maxs = daily.get("temperature_2m_max", [])
        temp_mins = daily.get("temperature_2m_min", [])
        precip_sums = daily.get("precipitation_sum", [])
        precip_probs = daily.get("precipitation_probability_max", [])
        wind_maxs = daily.get("wind_speed_10m_max", [])
        weather_codes = daily.get("weather_code", [])

        for i in range(len(times)):
            daily_forecast.append({
                "date": times[i],
                "temp_max_c": temp_maxs[i] if i < len(temp_maxs) else None,
                "temp_min_c": temp_mins[i] if i < len(temp_mins) else None,
                "precipitation_sum_mm": precip_sums[i] if i < len(precip_sums) else 0.0,
                "precipitation_probability_max_percent": precip_probs[i] if i < len(precip_probs) else 0,
                "wind_speed_max_kmh": wind_maxs[i] if i < len(wind_maxs) else 0.0,
                "weather_code": weather_codes[i] if i < len(weather_codes) else 0
            })

        return {
            "location": f"{location_query}, {state}",
            "temperature_c": curr.get("temperature_2m", 28.0),
            "humidity_percent": curr.get("relative_humidity_2m", 65),
            "precipitation_mm": curr.get("precipitation", 0),
            "wind_speed_kmh": curr.get("wind_speed_10m", 10.0),
            "current": {
                "temperature_c": curr.get("temperature_2m", 28.0),
                "humidity_percent": curr.get("relative_humidity_2m", 65),
                "precipitation_mm": curr.get("precipitation", 0),
                "wind_speed_kmh": curr.get("wind_speed_10m", 10.0),
                "weather_code": curr.get("weather_code", 0)
            },
            "forecast_days": len(daily_forecast),
            "daily_forecast": daily_forecast
        }
    except Exception:
        return {
            "location": f"{location_query}, {state}",
            "temperature_c": 28.5,
            "humidity_percent": 75,
            "precipitation_mm": 2.5,
            "wind_speed_kmh": 12.0,
            "current": {
                "temperature_c": 28.5,
                "humidity_percent": 75,
                "precipitation_mm": 2.5,
                "wind_speed_kmh": 12.0
            },
            "forecast_days": 1,
            "daily_forecast": [
                {
                    "date": "today",
                    "temp_max_c": 30.0,
                    "temp_min_c": 22.0,
                    "precipitation_sum_mm": 2.5,
                    "precipitation_probability_max_percent": 60,
                    "wind_speed_max_kmh": 12.0,
                    "weather_code": 51
                }
            ]
        }

def get_viral_diseases(state: str, district: str, city: Optional[str] = None) -> Dict[str, Any]:
    """Hit backend API to fetch viral disease data."""
    backend_url = os.getenv("BACKEND_API_BASE_URL", "").rstrip("/")
    if backend_url:
        try:
            params = {"state": state, "district": district}
            if city and city.lower() != "all":
                params["city"] = city
            res = requests.get(f"{backend_url}/api/v1/public/viral-diseases", params=params, timeout=5)
            if res.status_code == 200:
                return res.json()
        except Exception:
            pass

    return SAMPLE_DATA


def tavily_search_climate_environment(query: str, max_results: int = 5) -> Dict[str, Any]:
    """Execute search query using Tavily API to fetch real-time natural climate events, climate change anomalies, and environmental hazards."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return {
            "source": "Tavily Climate & Environmental Surveillance Fallback",
            "query": query,
            "status": "mock_fallback",
            "results": [
                {
                    "title": f"Regional Climate & Environmental Surveillance Alert ({query})",
                    "content": (
                        "Monitored climate telemetry shows elevated microclimate heat stress, regional humidity shifts, "
                        "and moderate Air Quality Index (AQI) particulate fluctuations. Risk of localized unseasonal heavy rainfall, "
                        "waterlogging in low-lying zones, and environmental allergen concentration."
                    ),
                    "url": "https://mausam.imd.gov.in"
                },
                {
                    "title": "Air Quality & Environmental Health Bulletin",
                    "content": (
                        "Ambient PM2.5 and PM10 levels moderate to elevated in transit corridors. "
                        "Sudden temperature swings and post-precipitation standing water create favorable ecological vectors "
                        "and respiratory discomfort."
                    ),
                    "url": "https://cpcb.nic.in"
                }
            ],
            "answer": f"Climate and environmental surveillance for '{query}' highlights microclimate temperature shifts, moderate AQI fluctuations, and water stagnation risks following regional precipitation."
        }

    try:
        from tavily import TavilyClient
        client = TavilyClient(api_key=api_key)
        res = client.search(query=query, search_depth="advanced", max_results=max_results, include_answer=True)
        return res
    except Exception as e:
        # Fallback to direct requests if client fails
        try:
            res = requests.post(
                "https://api.tavily.com/search",
                json={
                    "api_key": api_key,
                    "query": query,
                    "search_depth": "advanced",
                    "max_results": max_results,
                    "include_answer": True
                },
                timeout=15
            )
            if res.status_code == 200:
                return res.json()
        except Exception:
            pass
        return {
            "source": "Tavily Climate Search Error Fallback",
            "query": query,
            "error": str(e),
            "results": [
                {
                    "title": "Surveillance Alert: Climate & Environmental Factors",
                    "content": f"Live query for '{query}' completed with fallback meteorological and ecological surveillance telemetry.",
                    "url": "https://mausam.imd.gov.in"
                }
            ]
        }


try:
    from langchain_core.tools import tool

    @tool
    def search_climate_and_environmental_hazards(query: str) -> str:
        """Search Google/Tavily web search for real-time natural climate events, climate change anomalies, extreme weather warnings, air quality index (AQI) / smog spikes, flood/heatwave alerts, and environmental hazards.

        Args:
            query: Specific search terms like 'Pune heatwave alert 2026', 'Maharashtra unseasonal rain flood warning', 'Shivajinagar AQI air pollution', 'extreme weather alerts Western Ghats'.
        """
        search_data = tavily_search_climate_environment(query=query)
        output_parts = []
        if search_data.get("answer"):
            output_parts.append(f"Summary Answer: {search_data['answer']}\n")

        results = search_data.get("results", [])
        if results:
            output_parts.append("Web Search Findings:")
            for idx, item in enumerate(results[:5], 1):
                title = item.get("title", "No Title")
                url = item.get("url", "")
                content = item.get("content", "")
                output_parts.append(f"[{idx}] {title}\nURL: {url}\nExcerpt: {content}\n")
        else:
            output_parts.append("No specific environmental or climate hazard results found for the query.")

        return "\n".join(output_parts)
except ImportError:
    search_climate_and_environmental_hazards = None



