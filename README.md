# BluaDiagnostics — Sprint 2

Sistema de IA conversacional da Care Plus com:

- RAG clínico
- LangGraph multi-agente
- Function Calling
- Guardrails médicos
- Interface Streamlit
- Avaliação automatizada

## Arquitetura

A solução utiliza:

- GPT-4.1-mini
- LangChain
- LangGraph
- ChromaDB
- Streamlit
- OpenAI Embeddings

## Fluxo do Sistema

1. Usuário envia sintomas.
2. Supervisor identifica intenção.
3. Agente especializado é acionado.
4. RAG recupera contexto clínico.
5. Tools são executadas.
6. Guardrails validam segurança.
7. Resposta é retornada.

## Execução

```bash
pip install -r requirements.txt
streamlit run app/app.py

## Link do Repositório

https://github.com/nathanbiketeixeira/BluaDiagnostics-Sprint-2/blob/469daa54e63a3c4ba8d0fe753c9fda59c1f37c47/README.md
