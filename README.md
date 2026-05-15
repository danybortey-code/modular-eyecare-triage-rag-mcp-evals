# Modular Eyecare Triage and Patient Education System
### (RAG + MCP + Automated Evals)

---

## Overview

This project implements a modular, agent-inspired system for eyecare triage and patient education. The system processes natural language descriptions of eye symptoms, extracts structured clinical signals, retrieves relevant medical knowledge, assigns an urgency level, and generates safe, patient-friendly guidance.

The architecture combines:

- Modular rule-based components
- Retrieval-Augmented Generation (RAG)
- Model Context Protocol (MCP) tools
- Automated evaluation (Evals)

---

## Important Clarification

This project uses an agent-inspired modular architecture rather than autonomous LLM agents. The Intake, Triage, and Response components are implemented as deterministic Python modules with specialized responsibilities.

This design was chosen to provide a transparent, interpretable baseline suitable for a healthcare-related use case. The architecture is intentionally structured so that these rule-based modules can be replaced with LLM-powered agents in future versions.

---

## Motivation

Eye-related symptoms can range from mild irritation to serious emergencies. This project demonstrates how AI systems can assist in:

- Early triage decisions
- Patient education
- Safety-aware guidance

while maintaining clear boundaries (no diagnosis).

---

## System Architecture

### 1. Intake Agent

The Intake Agent extracts structured clinical information from user input using rule-based pattern matching.

**Outputs:**
- Symptoms (e.g., redness, pain, distorted vision)
- Duration (e.g., sudden, chronic)
- Known conditions (e.g., glaucoma, AMD)
- Medication context (e.g., missed drops)

This transforms unstructured text into machine-readable features.

---

### 2. Knowledge + Triage Agent

This component performs two key tasks.

#### a. Topic Identification

Maps symptoms to likely conditions:

- Dry Eye
- Cataract
- Glaucoma
- Age-related Macular Degeneration (AMD)
- Acute Red Eye (red flag category)

#### b. Urgency Classification

Assigns one of four levels:

- Self-care / education
- Routine eye appointment
- Urgent same-day evaluation
- Emergency care

This logic is implemented using interpretable clinical rules.

---

### 3. Response + Safety Agent

Generates the final output:

- Simple, patient-friendly explanation
- Relevant medical knowledge
- Clear next steps
- Safety disclaimer

This ensures the system is usable and responsible.

---

## Retrieval-Augmented Generation (RAG)

Instead of hardcoding medical knowledge, the system retrieves information from structured text files:

```text
data/
├── glaucoma/
├── cataract/
├── amd/
├── dry_eye/
└── red_flags/