from langgraph.graph import StateGraph, START, END

try:
    from agent.nodes import AgentState, weather_node, disease_node, climate_environmental_agent_node, llm_node
except ModuleNotFoundError:
    from nodes import AgentState, weather_node, disease_node, climate_environmental_agent_node, llm_node

builder = StateGraph(AgentState)

builder.add_node("weather_node", weather_node)
builder.add_node("disease_node", disease_node)
builder.add_node("climate_environmental_agent_node", climate_environmental_agent_node)
builder.add_node("llm_node", llm_node)

builder.add_edge(START, "weather_node")
builder.add_edge("weather_node", "disease_node")
builder.add_edge("disease_node", "climate_environmental_agent_node")
builder.add_edge("climate_environmental_agent_node", "llm_node")
builder.add_edge("llm_node", END)

proactive_graph = builder.compile()

