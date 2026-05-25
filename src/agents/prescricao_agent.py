from src.tools.medicamentos import verificar_interacoes_medicamentosas


def prescricao_agent(medicamentos):
    interacoes = verificar_interacoes_medicamentosas(medicamentos)

    return {
        "agent": "prescricao",
        "interacoes": interacoes,
        "necessita_medico": True
    }
