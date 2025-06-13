from strands.agent import Agent
from tools import extract_health_terms, assess_risk

triage_agent = Agent(
    system_prompt="""You are a medical triage assistant. Given a patient's description of symptoms, extract possible health-related terms and assess risk level. Keep your response concise and structured as:

- Extracted Terms: [term1, term2]
- Risk Assessment: [short message]""",
    tools=[extract_health_terms, assess_risk],
    response_format="plain-text"
) 