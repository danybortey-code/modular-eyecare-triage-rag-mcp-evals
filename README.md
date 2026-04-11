# Multi-Agent Eyecare Triage and Patient Education System

### (RAG + MCP + Automated Evals)

---

## Overview

This project implements a **multi-agent AI system** for eyecare triage and patient education. The system processes natural language descriptions of eye symptoms, extracts structured clinical signals, retrieves relevant medical knowledge, assigns an urgency level, and generates safe, patient-friendly guidance.

The architecture combines:

* **Multi-agent reasoning**
* **Retrieval-Augmented Generation (RAG)**
* **Model Context Protocol (MCP) tools**
* **Automated evaluation (Evals)**

---

## Motivation

Eye-related symptoms can range from mild irritation to serious emergencies. This project demonstrates how AI systems can assist in:

* Early triage decisions
* Patient education
* Safety-aware guidance

while maintaining clear boundaries (no diagnosis).

---

## System Architecture

### 1. Intake Agent

The Intake Agent extracts structured clinical information from user input using rule-based pattern matching.

**Outputs:**

* Symptoms (e.g., redness, pain, distorted vision)
* Duration (e.g., sudden, chronic)
* Known conditions (e.g., glaucoma, AMD)
* Medication context (e.g., missed drops)

This transforms unstructured text into machine-readable features.

---

### 2. Knowledge + Triage Agent

This agent performs two key tasks:

#### a. Topic Identification

Maps symptoms to likely conditions:

* Dry Eye
* Cataract
* Glaucoma
* Age-related Macular Degeneration (AMD)
* Acute Red Eye (red flag category)

#### b. Urgency Classification

Assigns one of four levels:

* Self-care / education
* Routine eye appointment
* Urgent same-day evaluation
* Emergency care

This logic is implemented using interpretable clinical rules.

---

### 3. Response + Safety Agent

Generates the final output:

* Simple, patient-friendly explanation
* Relevant medical knowledge
* Clear next steps
* Safety disclaimer

This ensures the system is **usable and responsible**.

---

## Retrieval-Augmented Generation (RAG)

Instead of hardcoding medical knowledge, the system retrieves information from structured text files:

```
data/
├── glaucoma/
├── cataract/
├── amd/
├── dry_eye/
└── red_flags/
```

### Benefits:

* Modular and extensible knowledge base
* Easy to update without changing code
* Transparent data sources

---

## MCP (Model Context Protocol) Integration

The project includes an MCP server exposing reusable tools:

### Available Tools

* `search_eye_knowledge(topic)`
* `get_red_flag_rules()`
* `get_patient_education(topic)`

### Why MCP?

MCP enables:

* Tool-based architecture
* Separation of reasoning and execution
* Integration with external AI systems

This makes the system **modular, scalable, and production-ready**.

---

## Evaluation Framework (Evals)

The project includes automated evaluation using structured test cases:

```
evals/eval_cases.jsonl
```

### Metrics:

* Topic classification accuracy
* Urgency classification accuracy

### Example Results:

* Topic accuracy: **4/4 (100%)**
* Urgency accuracy: **4/4 (100%)**

### Run evals:

```
python src/run_evals.py
```

---

## Running the System

### Main pipeline:

```
python src/main.py
```

### MCP server:

```
python mcp_server/server.py
```

---

## Example

### Input:

```
Straight lines look wavy and the center of my vision looks off
```

### Output:

* Topic: AMD
* Urgency: Urgent same-day evaluation
* Explanation: Distortion of central vision may indicate macular degeneration

---

## Design Principles

* **Safety-first**: No diagnosis, only guidance
* **Interpretability**: Rule-based logic for transparency
* **Modularity**: Agents + tools + data separation
* **Extensibility**: Easy to add new conditions or rules

---

## Future Improvements

* Integrate real medical APIs or databases
* Replace rule-based extraction with NLP models
* Add user interface (Streamlit / web app)
* Expand evaluation dataset (20–50 cases)
* Connect MCP tools to LLM orchestration

---

## Disclaimer

This system is intended for **educational and triage support purposes only**.
It does **not provide medical diagnosis or treatment**.
Users should consult a qualified healthcare professional for medical advice.

---

## Author

Daniel Bortey
Graduate Student – Data Science
Background: Optometry

---
