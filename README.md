# 👁️ Modular Eyecare Triage and Patient Education System

### A Hybrid Clinical Decision-Support Prototype with LLM Intake, RAG, MCP, and Automated Evaluation

> A healthcare-focused educational application that interprets free-text eye symptom descriptions, extracts structured clinical information using a local large language model, retrieves condition-specific knowledge, assigns urgency levels, and provides safe, non-diagnostic recommendations.

---

## Table of Contents

1. Overview
2. Important Clarification
3. Clinical Motivation
4. Problem Statement
5. System Architecture
6. How It Works
7. How the LLM Works
8. Key Design Decisions
9. Key Features
10. Tech Stack
11. Project Structure
12. Prerequisites
13. Installation
14. Running the Application
15. Testing and Validation
16. MCP Integration
17. Example Clinical Scenarios
18. Limitations
19. Future Enhancements
20. Learning Outcomes
21. Author
22. Disclaimer

---

## Overview

This project implements a hybrid AI system for eyecare triage and patient education.

Users describe their eye symptoms in natural language, and the system:

1. Extracts structured clinical information using a local LLM via Ollama.
2. Identifies likely ophthalmic conditions.
3. Retrieves supporting knowledge using Retrieval-Augmented Generation (RAG).
4. Assigns an urgency level.
5. Generates a safe educational recommendation.
6. Exposes reusable tools through Model Context Protocol (MCP).
7. Validates performance using automated evaluations.

The system is intended for educational and triage support purposes only and does not provide medical diagnosis.

---

## Important Clarification

This project combines a real LLM-powered intake agent with deterministic downstream modules.

The `LLMIntakeAgent` uses a local large language model served through Ollama to extract structured clinical information from free-text symptom descriptions.

The downstream triage, retrieval, and response components remain rule-based and fully interpretable. This hybrid design combines the flexibility of LLMs with the transparency and reliability of deterministic clinical logic.

---

## Clinical Motivation

Eye symptoms can range from mild irritation to sight-threatening emergencies.

Examples of serious ophthalmic conditions include:

* Retinal detachment
* Acute angle-closure glaucoma
* Wet age-related macular degeneration
* Corneal ulcer
* Optic neuritis

This project demonstrates how AI systems can support early triage while maintaining strict safety boundaries.

---

## Problem Statement

Develop an educational clinical decision-support system that can:

1. Accept free-text symptom descriptions.
2. Extract structured symptom information.
3. Detect urgent warning signs.
4. Retrieve condition-specific educational knowledge.
5. Assign an urgency category.
6. Generate safe, patient-friendly guidance.
7. Avoid making diagnoses or treatment recommendations.

---

## System Architecture

```text
User Input
    ↓
LLM Intake Agent (llm_intake_agent.py)
    ↓
Ollama Local API
    ↓
Llama 3.2 Model
    ↓
Structured Case Data (JSON)
    ↓
Knowledge + Triage Agent (knowledge_triage_agent.py)
    ↓
RAG Pipeline (rag_pipeline.py)
    ↓
Urgency Assignment (triage_rules.py)
    ↓
Response + Safety Agent (response_safety_agent.py)
    ↓
Final Educational Recommendation
```

---

## How It Works

### Step 1 — Symptom Capture

The user describes an eye concern in natural language.

### Step 2 — LLM-Based Intake

The `LLMIntakeAgent` sends the symptom description to a locally hosted Llama 3.2 model through Ollama.

### Step 3 — Structured JSON Extraction

The model returns structured clinical information including:

* `symptoms`
* `duration`
* `pain`
* `redness`
* `vision_change`
* `discharge`
* `light_sensitivity`
* `known_eye_condition`
* `medication_context`

### Step 4 — Rule-Based Fallback

If the LLM is unavailable, the system automatically falls back to the deterministic `IntakeAgent`.

### Step 5 — Knowledge and Triage

The `KnowledgeTriageAgent`:

* Identifies the most likely ophthalmic topic
* Retrieves supporting educational knowledge
* Assigns an urgency category

### Step 6 — Safety-Aware Response Generation

The `ResponseSafetyAgent` generates a patient-friendly explanation and includes a medical disclaimer.

### Step 7 — Final Output

The system returns:

* Structured case summary
* Retrieved educational knowledge
* Urgency level
* Patient recommendation

---

## How the LLM Works

The `llm_intake_agent.py` module sends the user's symptom description to the local Ollama API:

```text
http://localhost:11434/api/generate
```

The `llama3.2` model is instructed to return structured JSON output.

### Example Input

```text
Straight lines look wavy and the center of my vision looks off.
```

### Example Output

```json
{
  "symptoms": [
    "straight lines look wavy",
    "center of vision looks off"
  ],
  "duration": "unspecified",
  "pain": false,
  "redness": false,
  "vision_change": true,
  "discharge": false,
  "light_sensitivity": false,
  "known_eye_condition": null,
  "medication_context": null
}
```

---

## Key Design Decisions

### Hybrid AI Architecture

Combines probabilistic LLM reasoning with deterministic clinical logic.

### Structured JSON Output

Constrains the model to return machine-readable data for transparency and downstream processing.

### Rule-Based Fallback

If the LLM fails or times out, the system automatically reverts to the original deterministic intake module.

### Safety-First Approach

Educational guidance only; no diagnosis or treatment recommendations.

### Local Inference with Ollama

Runs entirely on the local machine, eliminating API costs and improving privacy.

### Modular Design

Each component has a single responsibility and can be independently upgraded.

---

## Key Features

* Ollama-powered natural language symptom interpretation
* Local Llama 3.2 model
* Structured JSON extraction
* Automatic rule-based fallback
* Retrieval-Augmented Generation (RAG)
* Rule-based urgency classification
* Response safety layer
* MCP server integration
* Automated evaluation framework
* Public GitHub repository

---

## Tech Stack

| Component            | Technology                      |
| -------------------- | ------------------------------- |
| Programming Language | Python 3                        |
| LLM Runtime          | Ollama                          |
| Model                | Llama 3.2                       |
| API Interface        | Local REST API using `requests` |
| Retrieval Layer      | Local text files                |
| Protocol Layer       | FastMCP                         |
| Evaluation           | JSONL + Python                  |
| Version Control      | Git and GitHub                  |
| IDE                  | VS Code                         |

---

## Project Structure

```text
modular-eyecare-triage-rag-mcp-evals/
├── data/
│   ├── glaucoma/
│   ├── cataract/
│   ├── amd/
│   ├── dry_eye/
│   └── red_flags/
│
├── evals/
│   └── eval_cases.jsonl
│
├── mcp_server/
│   └── server.py
│
├── src/
│   ├── intake_agent.py
│   ├── llm_intake_agent.py
│   ├── knowledge_triage_agent.py
│   ├── rag_pipeline.py
│   ├── triage_rules.py
│   ├── response_safety_agent.py
│   ├── main.py
│   └── run_evals.py
│
├── README.md
└── .gitignore
```

---

## Prerequisites

Before running the project, ensure you have:

* Python 3.10 or later
* Ollama installed
* The `llama3.2` model downloaded
* Git installed

---

## Installation

```bash
git clone https://github.com/danybortey-code/modular-eyecare-triage-rag-mcp-evals.git
cd modular-eyecare-triage-rag-mcp-evals
pip install requests fastmcp
ollama pull llama3.2
```

---

## Running the Application

### 1. Start Ollama

```bash
ollama run llama3.2
```

### 2. Run the Main Pipeline

```bash
python src/main.py
```

### 3. Run Automated Evaluations

```bash
python src/run_evals.py
```

### 4. Start the MCP Server

```bash
python mcp_server/server.py
```

---

## Testing and Validation

The project includes a structured evaluation dataset:

```text
evals/eval_cases.jsonl
```

Each test case contains:

* User input
* Expected topic
* Expected urgency

### Example Results

* Topic Accuracy: **4/4 (100%)**
* Urgency Accuracy: **4/4 (100%)**

---

## MCP Integration

The MCP server exposes reusable tools:

* `search_eye_knowledge(topic)`
* `get_red_flag_rules()`
* `get_patient_education(topic)`

These tools allow external AI systems to interact with the project programmatically.

---

## Example Clinical Scenarios

### AMD

**Input:** "Straight lines look wavy and the center of my vision looks off."

**Output:**

* Topic: AMD
* Urgency: Urgent same-day evaluation

### Acute Red Eye

**Input:** "My eye is red and painful and my vision is blurry since yesterday."

**Output:**

* Topic: Acute Red Eye
* Urgency: Emergency care


---

## Future Enhancements

* Expand the ophthalmology knowledge base
* Add image and PDF interpretation
* Build a Streamlit web interface
* Increase the size of the evaluation dataset
* Integrate external clinical data sources

---

## Learning Outcomes

This project provided hands-on experience in:

* Large Language Model (LLM) integration
* Prompt engineering and structured JSON extraction
* Retrieval-Augmented Generation (RAG)
* Rule-based clinical reasoning
* Model Context Protocol (MCP)
* Automated evaluation frameworks
* Git and GitHub project management


* GitHub: [https://github.com/danybortey-code](https://github.com/danybortey-code)
* Repository: [https://github.com/danybortey-code/modular-eyecare-triage-rag-mcp-evals](https://github.com/danybortey-code/modular-eyecare-triage-rag-mcp-evals)

---

## Disclaimer

This application is intended solely for educational and triage support purposes and should not be used as a substitute for professional medical advice, diagnosis, or treatment.
