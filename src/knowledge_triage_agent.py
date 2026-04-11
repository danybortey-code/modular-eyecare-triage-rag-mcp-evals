from typing import Dict
from triage_rules import assign_urgency
from rag_pipeline import RAGPipeline


class KnowledgeTriageAgent:
    """
    Determine likely topic, retrieve supporting knowledge,
    and assign urgency.
    """

    def __init__(self):
        self.rag_pipeline = RAGPipeline()

    def identify_topic(self, case_data: Dict) -> str:
        symptoms = case_data.get("symptoms", [])
        known_condition = case_data.get("known_eye_condition")
        medication_context = case_data.get("medication_context")

        if known_condition == "glaucoma" or medication_context == "missed glaucoma drops":
            return "glaucoma"

        if known_condition == "cataract" or "cloudy vision" in symptoms or "night glare" in symptoms:
            return "cataract"

        if known_condition == "amd" or "distorted vision" in symptoms:
            return "amd"

        if known_condition == "dry eye" or "dryness" in symptoms:
            return "dry eye"

        if "redness" in symptoms and "pain" in symptoms:
            return "acute red eye"

        return "dry eye"

    def get_supporting_knowledge(self, topic: str) -> list[str]:
        return self.rag_pipeline.load_topic_text(topic)

    def run(self, case_data: Dict) -> Dict:
        topic = self.identify_topic(case_data)
        urgency = assign_urgency(case_data)
        supporting_knowledge = self.get_supporting_knowledge(topic)

        return {
            "retrieved_topic": topic,
            "supporting_knowledge": supporting_knowledge,
            "urgency_label": urgency,
            "reasoning_summary": f"The case was matched to '{topic}' and classified as '{urgency}'."
        }