from typing import Dict, List


class IntakeAgent:
    """
    Extract structured symptom information from a user's message.
    """

    def __init__(self):
        self.symptom_keywords = {
            "redness": ["red", "redness", "bloodshot"],
            "pain": ["pain", "painful", "ache", "hurts", "hurting"],
            "blurry vision": ["blurry", "blurred vision", "vision is blurry"],
            "dryness": ["dry", "dryness", "gritty", "burning"],
            "light sensitivity": ["light sensitive", "photophobia", "sensitive to light"],
            "discharge": ["discharge", "pus", "watering", "watery"],
            "cloudy vision": ["cloudy", "foggy vision"],
            "night glare": ["glare", "headlights bother me", "night driving"],
            "distorted vision": [
                "wavy lines",
                "lines look wavy",
                "straight lines look wavy",
                "distorted",
                "distortion",
                "center looks off",
                "center of my vision looks off",
            ],
            "sudden vision loss": ["sudden vision loss", "can't see suddenly", "lost vision suddenly"],
        }

    def extract_symptoms(self, user_input: str) -> List[str]:
        text = user_input.lower()
        found = []

        for symptom, keywords in self.symptom_keywords.items():
            if any(keyword in text for keyword in keywords):
                found.append(symptom)

        return found

    def detect_duration(self, user_input: str) -> str:
        text = user_input.lower()

        if "since yesterday" in text:
            return "since yesterday"
        if "sudden" in text:
            return "sudden"
        if "today" in text:
            return "today"
        if "for weeks" in text or "for a few weeks" in text:
            return "for weeks"
        if "for months" in text:
            return "for months"
        if "chronic" in text:
            return "chronic"

        return "unspecified"

    def detect_known_condition(self, user_input: str) -> str | None:
        text = user_input.lower()

        if "glaucoma" in text:
            return "glaucoma"
        if "cataract" in text or "cataracts" in text:
            return "cataract"
        if "amd" in text or "macular degeneration" in text:
            return "amd"
        if "dry eye" in text:
            return "dry eye"

        return None

    def detect_medication_context(self, user_input: str) -> str | None:
        text = user_input.lower()

        if "missed my drops" in text or "missed my glaucoma drops" in text:
            return "missed glaucoma drops"
        if "eye drops" in text:
            return "eye drops"

        return None

    def run(self, user_input: str) -> Dict:
        symptoms = self.extract_symptoms(user_input)
        duration = self.detect_duration(user_input)
        known_condition = self.detect_known_condition(user_input)
        medication_context = self.detect_medication_context(user_input)

        case_data = {
            "symptoms": symptoms,
            "duration": duration,
            "pain": "pain" in symptoms,
            "redness": "redness" in symptoms,
            "vision_change": any(
                s in symptoms
                for s in ["blurry vision", "cloudy vision", "distorted vision", "sudden vision loss"]
            ),
            "discharge": "discharge" in symptoms,
            "light_sensitivity": "light sensitivity" in symptoms,
            "known_eye_condition": known_condition,
            "medication_context": medication_context,
        }

        return case_data