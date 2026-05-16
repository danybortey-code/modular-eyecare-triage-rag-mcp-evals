from typing import Dict


def assign_urgency(case_data: Dict) -> str:
    """
    Assign an urgency label based on structured symptom data.
    """

    symptoms = [s.lower() for s in case_data.get("symptoms", [])]
    symptom_text = " ".join(symptoms)

    pain = case_data.get("pain", False)
    redness = case_data.get("redness", False)
    vision_change = case_data.get("vision_change", False)
    light_sensitivity = case_data.get("light_sensitivity", False)
    duration = (case_data.get("duration") or "").lower()

    # Emergency care
    if vision_change and pain and redness:
        return "Emergency care"

    if "sudden vision loss" in symptom_text:
        return "Emergency care"

    # Urgent same-day evaluation
    if (
        "distorted vision" in symptom_text
        or "wavy" in symptom_text
        or "center of my vision" in symptom_text
        or "center of vision" in symptom_text
        or "central vision" in symptom_text
    ):
        return "Urgent same-day evaluation"

    if pain and redness:
        return "Urgent same-day evaluation"

    if vision_change and ("sudden" in duration or "new" in duration):
        return "Urgent same-day evaluation"

    if light_sensitivity and pain:
        return "Urgent same-day evaluation"

    # Routine eye appointment
    if "cloudy vision" in symptom_text:
        return "Routine eye appointment"

    if "night glare" in symptom_text:
        return "Routine eye appointment"

    if vision_change:
        return "Routine eye appointment"

    if "dryness" in symptom_text and "chronic" in duration:
        return "Routine eye appointment"

    # Self-care / education
    if "dryness" in symptom_text or "irritation" in symptom_text:
        return "Self-care / education"

    return "Routine eye appointment"