from checkpointer import checkpointer
from langgraph.graph import StateGraph, START, END
from state import State
from agent import solveBharatSwasthya
from guardrail import input_guardrail,output_guardrail,route_after_input


graph = StateGraph(State)

graph.add_node("chatbot",solveBharatSwasthya )
graph.add_node("input_checker",input_guardrail)
graph.add_node("output_checker",output_guardrail)

graph.add_edge(START, "input_checker")
graph.add_conditional_edges("input_checker",route_after_input,{
    "continue":"chatbot",
    "blocked":END
})
graph.add_edge("chatbot","output_checker")
graph.add_edge("output_checker",END)


workflow = graph.compile(
    checkpointer=checkpointer
)