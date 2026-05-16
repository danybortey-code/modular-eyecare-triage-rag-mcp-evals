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
7. Key Design Decisions
8. Key Features
9. Tech Stack
10. Project Structure
11. Installation
12. Running the Application
13. Testing and Validation
14. MCP Integration
15. Example Clinical Scenarios
16. Limitations
17. Future Enhancements
18. Learning Outcomes
19. Author
20. Disclaimer

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

- Retinal detachment
- Acute angle-closure glaucoma
- Wet age-related macular degeneration
- Corneal ulcer
- Optic neuritis

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
LLM Intake Agent (Ollama)
    ↓
Structured Case Data
    ↓
Knowledge + Triage Agent
    ↓
RAG Pipeline
    ↓
Urgency Assignment
    ↓
Response + Safety Agent
    ↓
Final Educational Recommendation

How It Works

Step 1 — Symptom Capture

The user enters a free-text description of their eye symptoms, such as:

"Straight lines look wavy and the center of my vision looks off."

Step 2 — LLM Intake Agent

The LLMIntakeAgent sends the symptom description to a local Ollama model (llama3.2) and extracts:

Symptoms
Duration
Pain
Redness
Vision change
Discharge
Light sensitivity
Known eye conditions
Medication context

If the LLM is unavailable, the system automatically falls back to the rule-based IntakeAgent.

Step 3 — Knowledge + Triage Agent

The KnowledgeTriageAgent:

Maps symptoms to likely conditions.
Retrieves condition-specific knowledge.
Assigns a triage category.

Step 4 — Retrieval-Augmented Generation (RAG)

The rag_pipeline.py module retrieves educational information from local ophthalmology text files.

Step 5 — Response + Safety Agent

The ResponseSafetyAgent generates a patient-friendly explanation and includes a medical disclaimer.

Step 6 — Final Output

The system returns:

Structured case summary
Retrieved knowledge
Urgency level
Educational recommendation
Key Design Decisions
Hybrid Architecture

Combines LLM-powered extraction with deterministic downstream logic.

Rule-Based Clinical Reasoning

Provides transparent and interpretable triage decisions.

Retrieval-Based Knowledge

Medical content is stored in modular text files rather than hardcoded responses.

Safety-First Design

Educational guidance only; no diagnosis or treatment recommendations.

Automated Evaluation

Built-in testing framework for objective validation.

Key Features
Local LLM-powered symptom extraction using Ollama

Automatic rule-based fallback if the LLM is unavailable

Retrieval-Augmented Generation (RAG)

Rule-based urgency classification

MCP tool server

Automated evaluation framework

Safety disclaimers

Professional GitHub documentation

Tech Stack

Component	Technology

Programming Language	Python 3

Local LLM	Ollama (llama3.2)

Retrieval Layer	Local text files

Protocol Layer	FastMCP

Evaluation	JSONL + Python

HTTP Client	requests

Version Control	Git & GitHub

IDE	VS Code

Project Structure

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

Installation
1. Clone the Repository
git clone https://github.com/danybortey-code/modular-eyecare-triage-rag-mcp-evals.git
cd modular-eyecare-triage-rag-mcp-evals

2. Install Python Dependencies
pip install requests fastmcp

3. Install Ollama

Download and install Ollama from:

https://ollama.com/download

4. Download the Model
ollama pull llama3.2
Running the Application
Start the Ollama Model
ollama run llama3.2

Keep this terminal open.

Run the Main Pipeline
python src/main.py
Run Automated Evaluations
python src/run_evals.py
Start the MCP Server
python mcp_server/server.py
Testing and Validation

The project includes a structured evaluation dataset:

evals/eval_cases.jsonl

Each test case contains:

User input
Expected topic
Expected urgency
Example Results
Topic Accuracy: 4/4 (100%)
Urgency Accuracy: 4/4 (100%)
MCP Integration

The MCP server exposes reusable tools:

search_eye_knowledge(topic)
get_red_flag_rules()
get_patient_education(topic)

These tools allow external AI systems to interact with the project programmatically.

Example Clinical Scenarios
Dry Eye

Input: "My eyes feel dry after staring at screens all day."

Output:

Topic: Dry Eye
Urgency: Self-care / education
Cataract

Input: "My vision is cloudy and headlights bother me at night."

Output:

Topic: Cataract
Urgency: Routine eye appointment
AMD

Input: "Straight lines look wavy and the center of my vision looks off."

Output:

Topic: AMD
Urgency: Urgent same-day evaluation
Acute Red Eye

Input: "My eye is red and painful and my vision is blurry since yesterday."

Output:

Topic: Acute Red Eye
Urgency: Emergency care

Future Enhancements
Expand the ophthalmology knowledge base.
Add image and PDF interpretation.
Build a Streamlit web interface.
Increase the size of the evaluation dataset.
Integrate external clinical data sources.
Learning Outcomes

This project provided hands-on experience in:

Large Language Model (LLM) integration
Prompt engineering and structured JSON extraction
Retrieval-Augmented Generation (RAG)
Rule-based clinical reasoning
Model Context Protocol (MCP)
Automated evaluation frameworks
Git and GitHub project management


GitHub: https://github.com/danybortey-code
Repository: https://github.com/danybortey-code/modular-eyecare-triage-rag-mcp-evals
Disclaimer

This application is intended solely for educational and triage support purposes and should not be used as a substitute for professional medical advice, diagnosis, or treatment.