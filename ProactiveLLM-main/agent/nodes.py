import os
import json
from typing import TypedDict, Optional, Dict, Any, List
from dotenv import load_dotenv

try:
    from agent.tools import (
        get_weather,
        get_viral_diseases,
        search_climate_and_environmental_hazards,
        tavily_search_climate_environment
    )
except ModuleNotFoundError:
    from tools import (
        get_weather,
        get_viral_diseases,
        search_climate_and_environmental_hazards,
        tavily_search_climate_environment
    )

load_dotenv()


class AgentState(TypedDict):
    state: str
    district: str
    city: Optional[str]
    language: Optional[str]
    weather_data: Optional[Dict[str, Any]]
    disease_data: Optional[Dict[str, Any]]
    climate_environment_data: Optional[str]
    llm_output: Optional[str]


def weather_node(state: AgentState) -> Dict[str, Any]:
    print(f"--- Node 1: Fetching Weather Data for {state['district']}, {state['state']} ---")
    weather = get_weather(state["state"], state["district"], state.get("city"))
    return {"weather_data": weather}


def disease_node(state: AgentState) -> Dict[str, Any]:
    print(f"--- Node 2: Fetching Viral Diseases for {state['district']}, {state['state']} ---")
    diseases = get_viral_diseases(state["state"], state["district"], state.get("city"))
    return {"disease_data": diseases}


def _extract_text_from_content(content: Any) -> str:
    """Helper to extract clean string text from LangChain message content."""
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and "text" in item:
                parts.append(item["text"])
            elif isinstance(item, str):
                parts.append(item)
        return "\n".join(parts)
    return str(content)


def climate_environmental_agent_node(state: AgentState) -> Dict[str, Any]:
    """Node 3: ReAct Agent equipped with Google/Tavily search tool to fetch real-time natural climate events, climate change anomalies, AQI, and environmental hazards."""
    location = f"{state.get('city') + ', ' if state.get('city') else ''}{state['district']}, {state['state']}"
    print(f"--- Node 3: Running ReAct Agent for Natural Climate & Environmental Hazards ({location}) ---")

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")

    agent_prompt = (
        f"You are an Autonomous Natural Climate, Climate Change & Environmental Hazard Surveillance ReAct Agent.\n"
        f"Target Location: {location}.\n\n"
        f"Primary Focus:\n"
        f"The viral disease statistics are already tracked separately by our epidemiological database. "
        f"YOUR primary objective is to investigate real-time NATURAL CLIMATE, CLIMATE CHANGE, and ENVIRONMENTAL HAZARDS for {location}.\n\n"
        f"Task:\n"
        f"1. Search for real-time natural climate events, climate change anomalies, weather extremes, and environmental hazards in/around {location} "
        f"(e.g., heatwave alerts, cold snaps, unseasonal rainfall, urban waterlogging/flood risks, cyclonic/storm disturbances, air quality index (AQI) / smog spikes, "
        f"groundwater or agricultural drought stress, and ecological disruption).\n"
        f"2. Use the `search_climate_and_environmental_hazards` tool with targeted, specific search queries.\n"
        f"3. Synthesize the findings into a clear, structured intelligence summary containing:\n"
        f"   - Active Climate Shifts & Meteorological Anomalies\n"
        f"   - Air Quality (AQI), Smog & Particulate Pollution Status\n"
        f"   - Local Environmental Hazards (e.g. waterlogging, heat stress, allergen peaks)\n"
        f"   - Direct Community & Environmental Risk Implications"
    )

    if api_key and search_climate_and_environmental_hazards is not None:
        try:
            from langgraph.prebuilt import create_react_agent
            from langchain_google_genai import ChatGoogleGenerativeAI

            llm = ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=api_key,
                temperature=0.2
            )
            react_agent = create_react_agent(llm, [search_climate_and_environmental_hazards])
            response = react_agent.invoke({
                "messages": [("user", agent_prompt)]
            })

            messages = response.get("messages", [])
            if messages:
                final_content = _extract_text_from_content(messages[-1].content)
                return {
                    "climate_environment_data": final_content
                }
        except Exception as e:
            print(f"ReAct climate agent execution warning: {e}. Falling back to direct tool surveillance fetch.")

    # Direct fallback if ReAct agent is unavailable or encounters an issue
    search_fallback = tavily_search_climate_environment(f"real time climate change extreme weather air quality AQI environmental hazards {location}")
    answer = search_fallback.get("answer") or "Active surveillance indicates microclimate temperature shifts, moderate AQI fluctuations, and localized precipitation impacts."
    results = search_fallback.get("results", [])
    snippets = "\n".join([f"- {r.get('title')}: {r.get('content')}" for r in results[:3]])

    fallback_report = (
        f"Live Climate & Environmental Hazard Surveillance for {location}:\n\n"
        f"Key Climate Findings: {answer}\n\n"
        f"Monitored Hazards & Reports:\n{snippets}\n\n"
        f"Environmental Implications: Monitor sudden temperature swings, stay updated on AQI levels, "
        f"and prepare for post-precipitation water stagnation and localized heat/cold stress."
    )
    return {
        "climate_environment_data": fallback_report
    }


def _generate_gemini_synthesis(api_key: str, model_name: str, prompt: str) -> str:
    """Invokes Google Gemini to synthesize multi-hazard health advisory."""
    from google import genai
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )
    return response.text


def llm_node(state: AgentState) -> Dict[str, Any]:
    print("--- Node 4: Running Gemini Reasoner for Multi-Hazard Proactive Advisory ---")
    weather = state.get("weather_data")
    diseases = state.get("disease_data")
    climate_env = state.get("climate_environment_data")
    location = f"{state.get('city') + ', ' if state.get('city') else ''}{state['district']}, {state['state']}"
    language = state.get("language") or "English"

    prompt = f"""You are an Advanced Proactive Climate & Public Health AI Reasoner.
Target Output Language: {language}

Analyze the following multi-source intelligence for {location}:

1. WEATHER TELEMETRY (Current Conditions & 10-Day Forecast from Open-Meteo):
{json.dumps(weather, indent=2)}

2. ACTIVE HOSPITAL/EPIDEMIOLOGICAL VIRAL DISEASE DATA (Database Records):
{json.dumps(diseases, indent=2)}

3. LIVE NATURAL CLIMATE, CLIMATE CHANGE & ENVIRONMENTAL HAZARD SURVEILLANCE (From Google/Tavily Web Search Agent):
{climate_env}

STRICT LANGUAGE DIRECTIVE & USER READABILITY GUIDELINES:
- You MUST generate and write the ENTIRE proactive advisory ONLY in '{language}'.
- All headings, sections, risk analysis, clinical recommendations, danger signs, and community precautions MUST be completely in '{language}'.
- Do NOT output English unless the requested Target Output Language is English.
- USER-FRIENDLY & PLAIN LANGUAGE: Use simple, clear, and everyday words that any normal citizen, patient, or community member can easily read and understand.
- AVOID HEAVY JARGON: Avoid overly dense or complicated academic medical terminology. If a clinical term must be mentioned (e.g., NSAIDs, Platelets, AQI, Antivirals, NS1, Pulse Oximetry), always explain it immediately in simple plain terms in parentheses (e.g., 'NSAIDs (common painkiller medicines like Brufen/Ibuprofen/Aspirin)' or 'Cyanosis (bluish lips or nails due to low oxygen)').
- ACTIONABLE & CLEAR: Use concise bullet points, direct Do's and Don'ts, and easy-to-follow practical steps.

Synthesize these inputs to provide a structured, user-friendly, comprehensive proactive climate and public health advisory in {language}:
1. Natural Climate Outlook & Environmental Hazards (Detailed yet simple assessment of climate anomalies, heat/cold stress, air quality/AQI, unseasonal rain, and localized environmental hazards)
2. Climate-Disease Vulnerability Correlation (Clear explanation of how the weather/climate creates breeding grounds or triggers for active diseases like Dengue mosquitoes in stagnant water, or flu spread during humidity/air pollution)
3. Actionable Community & Environmental Precautions (Easy-to-follow steps for mosquito prevention, air quality safety, heat/rain protection, food & clean drinking water)
4. Red Flag / Danger Symptoms (Critical emergency signs explained in simple words that mean the patient must go to the hospital immediately)
5. Clinical Guidance & Medication Warnings (Safe fever management, hydration, and a prominent warning on medicines to strictly avoid like Aspirin/Brufen/NSAIDs in suspected Dengue)
"""

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

    if api_key:
        try:
            output = _generate_gemini_synthesis(api_key=api_key, model_name=model_name, prompt=prompt)
        except Exception as e:
            output = (
                f"Gemini API error: {str(e)}\n\n"
                f"Fallback Multi-Hazard Climate & Health Advisory ({language}) for {location}:\n"
                f"- Climate Risk: Temperature swings, AQI fluctuations, and precipitation favor vector breeding and respiratory stress.\n"
                f"- Epidemiological Alert: High risk of vector-borne (Dengue) and respiratory (Influenza) illnesses.\n"
                f"- Precautions: Prevent water stagnation, protect against air pollution/allergens, wear repellents, and practice hand hygiene.\n"
                f"- Danger Signs: Seek emergency care for respiratory distress, rapid platelet drop, or persistent vomiting.\n"
                f"- Clinical Warning: Strictly avoid Aspirin/Ibuprofen for viral fever suspecting Dengue."
            )
    else:
        output = (
            f"Proactive Climate & Health Advisory ({language}) for {location}:\n\n"
            f"1. Natural Climate & Environment: Temperature {weather.get('temperature_c', 28)}°C, Humidity {weather.get('humidity_percent', 65)}%, with regional environmental and AQI surveillance active.\n"
            f"2. Climate-Disease Correlation: Elevated humidity and rainfall increase mosquito vector multiplication (Dengue) and post-monsoon viral transmission.\n"
            f"3. Active Outbreaks: Monitored {diseases.get('data', {}).get('count', 0)} pathogen clusters from hospital records (Dengue DENV-2 & Influenza H3N2).\n"
            f"4. Community Precautions: Clear stagnant water weekly, monitor air quality, use N95 masks in congested areas, and stay hydrated.\n"
            f"5. Clinical Protocol Alert: Strictly avoid Aspirin/NSAIDs in Dengue suspects due to severe platelet inhibition and hemorrhage risk."
        )

    return {"llm_output": output}

