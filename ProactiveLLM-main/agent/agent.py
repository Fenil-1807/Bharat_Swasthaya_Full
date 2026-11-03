from typing import Optional, Dict, Any

try:
    from agent.graph import proactive_graph
except ModuleNotFoundError:
    from graph import proactive_graph


def run_proactive_agent(
    state: str,
    district: str,
    city: Optional[str] = None,
    language: Optional[str] = "English"
) -> Dict[str, Any]:
    """Execute the 4-node proactive health intelligence workflow in the requested language."""
    target_language = language or "English"
    inputs = {
        "state": state,
        "district": district,
        "city": city,
        "language": target_language,
        "weather_data": None,
        "disease_data": None,
        "climate_environment_data": None,
        "llm_output": None
    }

    return proactive_graph.invoke(inputs)

