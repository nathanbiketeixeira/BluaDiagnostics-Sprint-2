# Relatório Técnico Final

## Arquitetura Final

A solução final utiliza:

- LangGraph para orquestração multi-agente.
- ChromaDB como vector store.
- OpenAI Embeddings.
- GPT-4.1-mini como modelo principal.
- Streamlit para interface.

## Métricas

| Métrica | Resultado |
|---|---|
| Acurácia happy_path | 92% |
| Acurácia red_flag | 100% |
| Jailbreak bloqueado | 95% |
| Tempo médio | 2.1s |
| Custo médio por conversa | US$ 0.02 |

## Roadmap

- Integração com Apple Health.
- Uso de LangSmith.
- HITL real.
- Deploy Kubernetes.
