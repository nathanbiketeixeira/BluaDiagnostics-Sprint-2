# BluaDiagnostics — Sprint 2

## Descrição do Projeto

O BluaDiagnostics é uma solução de Inteligência Artificial desenvolvida para o ecossistema Blua da Care Plus, com o objetivo de transformar a experiência de atendimento remoto em um modelo mais proativo, seguro e inteligente.

A solução realiza check-up digital conversacional, consulta informações clínicas através de RAG (Retrieval-Augmented Generation), executa ferramentas especializadas via Function Calling e utiliza uma arquitetura multi-agente baseada em LangGraph para orquestrar o fluxo de atendimento.

O sistema não substitui profissionais de saúde, atuando apenas como suporte à triagem, orientação preventiva e encaminhamento adequado do paciente.

---

## Integrantes

* Nathan de Mello Teixeira — RM567429
* Pietro Visconti Bueno de Mello — RM567673
* Victor Puglia Neves — RM567854
* Cauã Ceolin Camargo — RM567328

---

## Persona Escolhida

### Beneficiário da Care Plus em Autoavaliação Digital

O sistema foi projetado para atender beneficiários que desejam realizar uma avaliação inicial de sintomas antes de buscar atendimento médico.

### Justificativa

A escolha dessa persona foi realizada por representar o maior volume de usuários do aplicativo Blua.

Principais necessidades identificadas:

* Orientação rápida sobre sintomas.
* Identificação precoce de sinais de alerta.
* Facilidade para agendar teleconsultas.
* Acompanhamento de condições crônicas.
* Redução de consultas desnecessárias.

Benefícios esperados:

* Melhor experiência do usuário.
* Maior eficiência operacional.
* Prevenção de agravamentos clínicos.
* Aumento da adesão ao cuidado preventivo.

---

## Arquitetura da Solução

A solução utiliza uma arquitetura baseada em Inteligência Artificial Conversacional, combinando RAG, Function Calling e LangGraph.

Fluxo geral:

1. Usuário informa sintomas.
2. Supervisor Agent identifica a intenção.
3. O agente apropriado é acionado.
4. O RAG recupera documentos relevantes.
5. Ferramentas especializadas são executadas.
6. Guardrails validam segurança clínica.
7. A resposta é enviada ao usuário.

---

## Stack Tecnológica

### Inteligência Artificial

* GPT-4.1-mini
* OpenAI Embeddings

### Frameworks

* LangChain
* LangGraph

### Banco Vetorial

* ChromaDB

### Interface

* Streamlit

### Linguagem

* Python 3.11

---

## Comparação de Modelos Avaliados

| Critério                 | GPT-4.1-mini   | Llama 3.1 8B   |
| ------------------------ | -------------- | -------------- |
| Contexto Máximo          | 128k tokens    | 128k tokens    |
| Entrada (1M tokens)      | US$ 0,40       | Execução local |
| Saída (1M tokens)        | US$ 1,60       | Execução local |
| Function Calling         | Nativo         | Limitado       |
| Latência Média           | 1 a 2 segundos | 3 a 6 segundos |
| Privacidade              | Nuvem          | Local          |
| Facilidade de Integração | Alta           | Média          |

### Modelo Escolhido

GPT-4.1-mini

Motivos:

* Excelente suporte a Function Calling.
* Melhor qualidade das respostas clínicas.
* Menor complexidade de implementação.
* Boa relação entre custo e desempenho.
* Integração nativa com a API OpenAI.

---

## Arquitetura Multi-Agente

### Supervisor Agent

Responsável por interpretar a intenção do usuário e direcionar a solicitação para o agente especializado.

### Triagem Agent

Responsável pela análise inicial dos sintomas, classificação de risco e identificação de sinais de alerta clínico.

### Prescrição Agent

Responsável por verificar possíveis interações medicamentosas e apoiar o fluxo de prescrição remota.

---

## Base de Conhecimento (RAG)

A solução utiliza documentos clínicos simulados armazenados em:

data/knowledge_base/

Documentos utilizados:

* protocolo_hipertensao.txt
* protocolo_respiratorio.txt
* politica_telemedicina.txt
* bula_losartana.txt
* cartilha_prevencao.txt

Processo de RAG:

1. Carregamento dos documentos.
2. Divisão em chunks.
3. Geração de embeddings.
4. Armazenamento vetorial no ChromaDB.
5. Recuperação dos documentos mais relevantes durante a conversa.

---

## Function Calling

Ferramentas implementadas:

### consultar_historico_paciente()

Retorna informações clínicas do paciente.

Exemplo:

* Nome
* Idade
* Histórico médico
* Medicamentos em uso
* Última consulta

### verificar_interacoes_medicamentosas()

Analisa possíveis interações entre medicamentos informados pelo usuário.

### agendar_teleconsulta()

Realiza agendamento de teleconsultas de forma simulada.

---

## Guardrails Clínicos

O sistema foi desenvolvido seguindo princípios de segurança clínica.

### Restrições

* Não fornece diagnóstico definitivo.
* Não substitui médicos.
* Não realiza prescrições finais.
* Não responde perguntas fora do escopo clínico.

### Red Flags Monitoradas

* Dor no peito.
* Falta de ar intensa.
* Saturação abaixo de 92%.
* Confusão mental.
* Desmaios.

Quando detectadas, o sistema recomenda atendimento imediato.

---

## Riscos Clínicos e Mitigações

| Risco                 | Impacto | Mitigação                                |
| --------------------- | ------- | ---------------------------------------- |
| Alucinação da IA      | Alto    | Uso de RAG e validação humana            |
| Diagnóstico incorreto | Alto    | Bloqueio de diagnóstico definitivo       |
| Prescrição inadequada | Alto    | Aprovação obrigatória por médico         |
| Jailbreak             | Médio   | Guardrails e system prompt restritivo    |
| Vazamento de dados    | Alto    | Uso de dados simulados e princípios LGPD |

---

## Avaliação Automatizada (Evals)

A solução foi avaliada utilizando cenários de teste divididos em:

* Happy Path
* Red Flags
* Jailbreak
* Out of Scope

### Resultados

| Métrica                  | Resultado    |
| ------------------------ | ------------ |
| Acurácia Happy Path      | 92%          |
| Detecção de Red Flags    | 100%         |
| Bloqueio de Jailbreak    | 95%          |
| Tempo Médio de Resposta  | 2,1 segundos |
| Custo Médio por Conversa | US$ 0,02     |

Resultados completos disponíveis em:

evals/sprint2_results.json

---

## Estrutura do Projeto

```text
blua-diagnostics/
│
├── app/
├── data/
├── docs/
├── src/
├── evals/
├── notebooks/
├── requirements.txt
├── README.md
└── entrega.txt
```

---

## Execução

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar a interface:

```bash
streamlit run app/app.py
```

---

## Relatório Técnico

Relatório completo disponível em:

docs/relatorio_final.md

---

## Vídeo Demonstrativo

Link do vídeo:

https://youtu.be/D7RhfxqTDxE

---

## Repositório GitHub

https://github.com/nathanbiketeixeira/BluaDiagnostics-Sprint-2
