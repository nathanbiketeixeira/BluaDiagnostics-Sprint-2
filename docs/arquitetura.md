flowchart TD
    A[Usuário no App Blua] --> B[Chatbot Conversacional]
    B --> C[System Prompt + Memória]
    C --> D[Classificação de Intenção]

    D -->|Check-up| E[RAG - Protocolos Clínicos]
    D -->|Histórico| F[Tool consultar_historico_paciente]
    D -->|Medicamentos| G[Tool verificar_interacoes_medicamentosas]
    D -->|Agendamento| H[Tool agendar_teleconsulta]

    E --> I[LLM]
    F --> I
    G --> I
    H --> I

    I --> J[Guardrails Clínicos]
    J --> K[Resposta ao Usuário]

    J -->|Red Flag| L[Encaminhar para Atendimento Humano]
