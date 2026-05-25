from src.agents.triagem_agent import triagem_agent
from src.agents.prescricao_agent import prescricao_agent


def supervisor(user_input):
    if "medicamento" in user_input.lower() or "tomar" in user_input.lower():
        return prescricao_agent(["losartana", "ibuprofeno"])

    return triagem_agent(user_input)
