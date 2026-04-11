import json
from pathlib import Path

from intake_agent import IntakeAgent
from knowledge_triage_agent import KnowledgeTriageAgent


def main():
    intake_agent = IntakeAgent()
    knowledge_triage_agent = KnowledgeTriageAgent()

    eval_file = Path(__file__).resolve().parent.parent / "evals" / "eval_cases.jsonl"

    correct_topic = 0
    correct_urgency = 0
    total = 0

    with eval_file.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            case = json.loads(line)
            total += 1

            user_input = case["user_input"]
            expected_topic = case["expected_topic"]
            expected_urgency = case["expected_urgency"]

            case_data = intake_agent.run(user_input)
            triage_result = knowledge_triage_agent.run(case_data)

            predicted_topic = triage_result["retrieved_topic"]
            predicted_urgency = triage_result["urgency_label"]

            topic_match = predicted_topic == expected_topic
            urgency_match = predicted_urgency == expected_urgency

            if topic_match:
                correct_topic += 1

            if urgency_match:
                correct_urgency += 1

            print(f"\nCASE {case['case_id']}")
            print(f"Input: {user_input}")
            print(f"Expected topic: {expected_topic}")
            print(f"Predicted topic: {predicted_topic}")
            print(f"Topic correct: {topic_match}")
            print(f"Expected urgency: {expected_urgency}")
            print(f"Predicted urgency: {predicted_urgency}")
            print(f"Urgency correct: {urgency_match}")

    print("\n--- EVAL SUMMARY ---")
    print(f"Total cases: {total}")
    print(f"Topic accuracy: {correct_topic}/{total}")
    print(f"Urgency accuracy: {correct_urgency}/{total}")


if __name__ == "__main__":
    main()