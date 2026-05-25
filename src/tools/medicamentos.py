
def verificar_interacoes_medicamentosas(medicamentos):
    if "ibuprofeno" in [m.lower() for m in medicamentos]:
        return {
            "risco": "moderado",
            "descricao": "Ibuprofeno pode reduzir efeito da losartana"
        }

    return {
        "risco": "baixo",
        "descricao": "Nenhuma interação grave encontrada"
    }
