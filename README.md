# BluaDiagnostics-Sprint-2

Sistema de IA conversacional para transformar o aplicativo Blua da Care Plus em uma plataforma de cuidado remoto proativo.

## Integrantes

- Nathan Teixeira — RM XXXXX
- Integrante 2 — RM XXXXX
- Integrante 3 — RM XXXXX

## Persona Escolhida

### Beneficiário Final em Autoavaliação

A solução foi projetada para atender beneficiários da Care Plus, permitindo a realização de um check-up digital conversacional com coleta de sintomas e sinais vitais.

### Justificativa

- Maior impacto em escala.
- Redução de consultas desnecessárias.
- Identificação precoce de sinais de alerta.
- Experiência integrada ao aplicativo Blua.

## Objetivos da Solução

- Realizar check-up digital conversacional.
- Detectar red flags clínicas.
- Consultar histórico do paciente.
- Verificar interações medicamentosas.
- Agendar teleconsultas automaticamente.

## Stack Técnica

- Python 3.11
- OpenAI GPT-4.1-mini
- LangChain (opcional)
- Google Colab
- JSON para base de conhecimento e tools

## Comparação de Modelos

| Critério | GPT-4.1-mini | Llama 3.1 8B |
|--------:|--------------|-------------|
| Custo | Baixo | Muito baixo |
| Qualidade clínica | Excelente | Boa |
| Function Calling | Nativo | Limitado |
| Contexto | Grande | Médio |
| Privacidade | Cloud | On-premise |
| Latência | Baixa | Média |

### Modelo Escolhido: GPT-4.1-mini

Motivos:
- Excelente suporte a function calling.
- Boa relação custo-benefício.
- Alta confiabilidade em respostas estruturadas.

## Riscos Clínicos e Mitigações

### Alucinação
Mitigação: system prompt restritivo e validação humana.

### Diagnóstico Indevido
Mitigação: agente não fornece diagnóstico definitivo.

### Prescrição Sem Médico
Mitigação: qualquer prescrição depende de aprovação médica.

### LGPD
Mitigação: uso apenas de dados mínimos necessários.

### Jailbreak
Mitigação: casos de teste específicos no eval set.

## Arquitetura

O fluxo completo está documentado em `docs/arquitetura.md`.

## Estrutura do Repositório

- `prompts/`: system prompt.
- `evals/`: conjunto de testes.
- `tools/`: especificação das funções.
- `notebooks/`: PoC funcional.
- `docs/`: fluxograma da arquitetura.

## Execução

1. Abra o notebook `notebooks/sprint1_poc.ipynb` no Google Colab.
2. Configure a variável `OPENAI_API_KEY`.
3. Execute todas as células.

## Resultados Esperados

- Conversa com memória de contexto.
- Chamada automática de tools.
- Respostas seguras e contextualizadas.

## Link do Repositório

https://github.com/seu-usuario/blua-diagnostics
