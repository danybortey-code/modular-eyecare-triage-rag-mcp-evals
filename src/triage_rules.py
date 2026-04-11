from typing import Dict


def assign_urgency(case_data: Dict) -> str:
    """
    Assign an urgency label based on structured symptom data.
    """

    symptoms = [s.lower() for s in case_data.get("symptoms", [])]
    pain = case_data.get("pain", False)
    redness = case_data.get("redness", False)
    vision_change = case_data.get("vision_change", False)
    light_sensitivity = case_data.get("light_sensitivity", False)
    duration = (case_data.get("duration") or "").lower()

    # Emergency care
    if vision_change and pain and redness:
        return "Emergency care"

    if "sudden vision loss" in symptoms:
        return "Emergency care"

    # Urgent same-day evaluation
    if "distorted vision" in symptoms:
        return "Urgent same-day evaluation"

    if pain and redness:
        return "Urgent same-day evaluation"

    if vision_change and ("sudden" in duration or "new" in duration):
        return "Urgent same-day evaluation"

    if light_sensitivity and pain:
        return "Urgent same-day evaluation"

    # Routine eye appointment
    if "cloudy vision" in symptoms:
        return "Routine eye appointment"

    if "night glare" in symptoms:
        return "Routine eye appointment"

    if vision_change:
        return "Routine eye appointment"

    if "dryness" in symptoms and "chronic" in duration:
        return "Routine eye appointment"

    # Self-care / education
    if "dryness" in symptoms or "irritation" in symptoms:
        return "Self-care / education"

    return "Routine eye appointment"