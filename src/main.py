from intake_agent import IntakeAgent
from knowledge_triage_agent import KnowledgeTriageAgent
from response_safety_agent import ResponseSafetyAgent


def main():
    intake_agent = IntakeAgent()
    knowledge_triage_agent = KnowledgeTriageAgent()
    response_safety_agent = ResponseSafetyAgent()

    user_input = input("Describe your eye concern: ")

    case_data = intake_agent.run(user_input)
    triage_result = knowledge_triage_agent.run(case_data)
    final_response = response_safety_agent.run(case_data, triage_result)

    print("\n--- STRUCTURED CASE ---")
    print(case_data)

    print("\n--- TRIAGE RESULT ---")
    print(triage_result)

    print("\n--- FINAL RESPONSE ---")
    print(final_response)


if __name__ == "__main__":
    main()