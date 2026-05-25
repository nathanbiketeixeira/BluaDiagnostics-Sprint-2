from src.rag.retriever import buscar_contexto


def triagem_agent(user_input):
    contexto = buscar_contexto(user_input)

    red_flags = [
        "dor no peito",
        "falta de ar",
        "desmaio",
        "saturação 89"
    ]

    if any(flag in user_input.lower() for flag in red_flags):
        return {
            "agent": "triagem",
            "risco": "alto",
            "acao": "Encaminhamento imediato"
        }

    return {
        "agent": "triagem",
        "risco": "baixo",
        "contexto_rag": contexto
    }
