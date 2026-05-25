from langgraph.graph import StateGraph
from src.agents.supervisor_agent import supervisor


def run_graph(user_input):
    return supervisor(user_input)
