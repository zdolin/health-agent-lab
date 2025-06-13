from strands import Agent
from tools.triage_tool import extract_health_terms
from tools.risk_tool import assess_risk
from agents.config import bedrock_model

triage_agent = Agent(
    model=bedrock_model,
    system_prompt="""You are a medical triage assistant. Given a patient's description of symptoms, extract possible health-related terms and assess risk level. Keep your response concise and structured as:

- Extracted Terms: [term1, term2]
- Risk Assessment: [short message]""",
    tools=[extract_health_terms, assess_risk]
) 