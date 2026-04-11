from typing import Dict


class ResponseSafetyAgent:
    """
    Generate the final patient-friendly and safety-aware response.
    """

    def run(self, case_data: Dict, triage_result: Dict) -> str:
        topic = triage_result["retrieved_topic"]
        urgency = triage_result["urgency_label"]
        knowledge = triage_result["supporting_knowledge"]

        intro = "Here’s a simple summary of what your symptoms may mean.\n\n"

        if urgency == "Self-care / education":
            next_step = (
                "This sounds more like a mild issue that may be appropriate for self-care and monitoring. "
                "If symptoms continue, get worse, or start affecting your vision, schedule an eye appointment."
            )
        elif urgency == "Routine eye appointment":
            next_step = (
                "This does not sound like an emergency, but it would be a good idea to schedule a routine eye appointment "
                "for proper evaluation."
            )
        elif urgency == "Urgent same-day evaluation":
            next_step = (
                "Your symptoms sound like something that should be checked as soon as possible, ideally the same day."
            )
        else:
            next_step = (
                "Your symptoms may represent a serious eye problem. Please seek emergency care immediately, especially "
                "if the vision change is sudden or severe."
            )

        safety_note = (
            "\n\nThis assistant is for education and triage support only. "
            "It does not provide a medical diagnosis."
        )

        knowledge_text = "Relevant eyecare information:\n- " + "\n- ".join(knowledge)

        return intro + knowledge_text + "\n\nUrgency: " + urgency + "\n\n" + next_step + safety_note