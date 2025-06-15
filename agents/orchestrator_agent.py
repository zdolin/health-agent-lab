from strands import Agent, tool
from agents import triage_agent, rx_agent
from agents.config import bedrock_model

@tool
def triage_tool(patient_text: str) -> str:
    """
    Process patient symptoms through the triage agent.
    
    Args:
        patient_text: Patient's description of symptoms
        
    Returns:
        Triage results including extracted terms and risk assessment
    """
    return triage_agent(patient_text)

@tool
def rx_lookup_tool(term: str) -> str:
    """
    Look up medication information using the rx agent.
    
    Args:
        term: Medication or drug term to look up
        
    Returns:
        Structured drug information from FDA
    """
    return rx_agent(term)

# Create the orchestrator agent with specialized tools
orchestrator_agent = Agent(
    model=bedrock_model,
    system_prompt="""You are a medical information orchestrator. Follow these steps EXACTLY:

1. First use triage_tool to extract high-risk health terms and assess risk

2. For each extracted term that might be a medication, use rx_lookup_tool to get the drug information and quotes from the FDA data.

3. Create patient-friendly explanation with quoted FDA data and API calls made

IMPORTANT:
- Keep the response structured and clear
- Provide real-time updates on the progress of the tool calls and the results of the tool calls
- Include all relevant FDA data and openFDA API URLs used""",
    tools=[triage_tool, rx_lookup_tool]
)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run the orchestrator agent with a patient description.')
    parser.add_argument('description', type=str, help='Patient symptom description')
    args = parser.parse_args()

    # Run the orchestrator agent with the description
    response = orchestrator_agent(args.description)
    print(response) 