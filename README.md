# 👁️ Modular Eyecare Triage and Patient Education System
### A Rule-Based Clinical Decision-Support Prototype with RAG, MCP, and Automated Evaluation

> A healthcare-focused educational application that interprets free-text eye symptom descriptions, extracts structured clinical information, retrieves condition-specific knowledge, assigns urgency levels, and provides safe, non-diagnostic recommendations.

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

This project implements a modular, agent-inspired system for eyecare triage and patient education.

Users describe their eye symptoms in natural language, and the system:

1. Extracts structured clinical information.
2. Identifies likely ophthalmic conditions.
3. Retrieves supporting knowledge using Retrieval-Augmented Generation (RAG).
4. Assigns an urgency level.
5. Generates a safe educational recommendation.
6. Exposes reusable tools through Model Context Protocol (MCP).
7. Validates performance using automated evaluations.

The system is intended for educational and triage support purposes only and does not provide medical diagnosis.

---

## Important Clarification

This project uses an agent-inspired modular architecture rather than autonomous LLM agents.

The Intake, Triage, and Response components are implemented as deterministic Python modules with specialized responsibilities. This design provides a transparent, interpretable baseline appropriate for a healthcare use case.

The architecture is intentionally structured so that these rule-based modules can be replaced with LLM-powered agents in future versions.

---

## Clinical Motivation

Eye symptoms can range from mild irritation to sight-threatening emergencies.

Examples of serious ophthalmic conditions include:

- Retinal detachment
- Acute angle-closure glaucoma
- Wet age-related macular degeneration
- Corneal ulcer
- Optic neuritis

This project demonstrates how AI-inspired systems can support early triage while maintaining strict safety boundaries.

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
Intake Agent
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

“My vision is cloudy and headlights bother me at night.”

Step 2 — Intake Agent

The IntakeAgent extracts structured clinical features including:

Symptoms
Duration
Known eye conditions
Medication context

Step 3 — Knowledge + Triage Agent

The KnowledgeTriageAgent:

Maps symptoms to likely conditions
Assigns an urgency level
Calls the RAG pipeline to retrieve educational content

Step 4 — Retrieval-Augmented Generation (RAG)

The rag_pipeline.py module retrieves condition-specific information from the data/ directory.

Step 5 — Response + Safety Agent

The ResponseSafetyAgent generates a patient-friendly explanation and includes a medical disclaimer.

Step 6 — Final Output

The system returns:

Structured case summary
Retrieved knowledge
Urgency level
Educational recommendation
Key Design Decisions
Modular Architecture

Each component has a focused responsibility.

Rule-Based Clinical Logic

Transparent, interpretable, and deterministic.

Retrieval-Based Knowledge

Medical content is stored in structured text files rather than hardcoded into responses.

Safety-First Design

Educational guidance only; no diagnosis or treatment recommendations.

Automated Evaluation

Built-in testing framework for objective performance assessment.

Key Features
Modular agent-inspired architecture
Structured symptom extraction
Rule-based urgency classification
Retrieval-Augmented Generation (RAG)
MCP tool server
Automated evaluation framework
Safety disclaimers
Professional GitHub documentation
Tech Stack
Component	Technology
Programming Language	Python 3
Retrieval Layer	Local text files
Protocol Layer	FastMCP
Evaluation	JSONL + Python
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
git clone https://github.com/danybortey-code/modular-eyecare-triage-rag-mcp-evals.git
cd modular-eyecare-triage-rag-mcp-evals
pip install fastmcp
Running the Application
Main Pipeline
python src/main.py
MCP Server
python mcp_server/server.py
Run Automated Evaluations
python src/run_evals.py
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

Input: “My eyes feel dry after staring at screens all day.”

Output:

Topic: Dry Eye
Urgency: Self-care / education
Cataract

Input: “My vision is cloudy and headlights bother me at night.”

Output:

Topic: Cataract
Urgency: Routine eye appointment
AMD

Input: “Straight lines look wavy and the center of my vision looks off.”

Output:

Topic: AMD
Urgency: Urgent same-day evaluation
Acute Red Eye

Input: “My eye is red and painful and my vision is blurry since yesterday.”

Output:

Topic: Acute Red Eye
Urgency: Emergency care
Limitations
Rule-based rather than LLM-driven
Limited number of supported conditions
Educational only
No image or PDF interpretation
Not clinically validated
Future Enhancements
Replace rule-based modules with LLM-powered agents
Expand the ophthalmology knowledge base
Build a Streamlit user interface
Add multimodal image analysis
Increase evaluation dataset size
Learning Outcomes

This project provided hands-on experience in:

Modular AI system design
Rule-based clinical reasoning
Retrieval-Augmented Generation (RAG)
Model Context Protocol (MCP)
Automated evaluation frameworks
Git and GitHub project management


GitHub: https://github.com/danybortey-code
Repository: https://github.com/danybortey-code/modular-eyecare-triage-rag-mcp-evals
Disclaimer

This application is intended solely for educational and triage support purposes and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

