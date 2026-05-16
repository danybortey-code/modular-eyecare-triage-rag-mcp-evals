import json
import requests
from intake_agent import IntakeAgent


class LLMIntakeAgent:
    """
    Uses a local Ollama model to extract structured symptom information.
    Falls back to the rule-based IntakeAgent if Ollama is unavailable.
    """

    def __init__(self, model="llama3.2"):
        self.model = model
        self.ollama_url = "http://localhost:11434/api/generate"
        self.fallback_agent = IntakeAgent()

    def to_bool(self, value) -> bool:
        """
        Convert LLM outputs like yes/no/none into real Python booleans.
        """
        if isinstance(value, bool):
            return value

        if value is None:
            return False

        if isinstance(value, str):
            value = value.strip().lower()
            if value in ["yes", "true", "present", "positive", "1"]:
                return True
            if value in ["no", "false", "none", "absent", "negative", "0", "unknown"]:
                return False

        return False

    def normalize_duration(self, value) -> str:
        if value is None:
            return "unspecified"

        value = str(value).strip().lower()

        if value in ["unknown", "none", "null", ""]:
            return "unspecified"

        return value

    def run(self, user_input: str) -> dict:
        prompt = f"""
You are an eyecare intake agent.

Extract structured symptom information from the patient message.

Return ONLY valid JSON with these exact keys:
symptoms, duration, pain, redness, vision_change, discharge,
light_sensitivity, known_eye_condition, medication_context.

Important:
- pain, redness, vision_change, discharge, and light_sensitivity must be true or false.
- duration should be a short string.
- symptoms should be a list of short symptom phrases.
- use null when known_eye_condition or medication_context is unknown.
- do not diagnose.

Patient message:
{user_input}
"""

        payload = {
            "model": self.model,
            "prompt": prompt,
            "format": "json",
            "stream": False
        }

        try:
            response = requests.post(
                self.ollama_url,
                json=payload,
                timeout=120
            )
            response.raise_for_status()

            result = response.json()
            raw_json = result["response"]
            parsed = json.loads(raw_json)

            return {
                "symptoms": parsed.get("symptoms", []),
                "duration": self.normalize_duration(parsed.get("duration")),
                "pain": self.to_bool(parsed.get("pain")),
                "redness": self.to_bool(parsed.get("redness")),
                "vision_change": self.to_bool(parsed.get("vision_change")),
                "discharge": self.to_bool(parsed.get("discharge")),
                "light_sensitivity": self.to_bool(parsed.get("light_sensitivity")),
                "known_eye_condition": parsed.get("known_eye_condition"),
                "medication_context": parsed.get("medication_context"),
                "intake_source": "ollama_llm"
            }

        except Exception as e:
            case_data = self.fallback_agent.run(user_input)
            case_data["intake_source"] = f"rule_based_fallback ({e})"
            return case_data