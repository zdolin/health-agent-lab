from strands import Agent, tool
from agents import triage_agent, rx_agent, explainer_agent
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
    return triage_agent.run(patient_text)

@tool
def rx_lookup_tool(term: str) -> str:
    """
    Look up medication information using the rx agent.
    
    Args:
        term: Medication or drug term to look up
        
    Returns:
        Structured drug information from RxNorm and FDA
    """
    return rx_agent.run(term)

@tool
def explainer_tool(data: dict) -> str:
    """
    Generate patient-friendly explanations using the explainer agent.
    
    Args:
        data: Dictionary containing term, risk assessment, and rx data
        
    Returns:
        Patient-friendly explanation of the information
    """
    return explainer_agent.run(data)

# Create the orchestrator agent with specialized tools
orchestrator_agent = Agent(
    model=bedrock_model,
    system_prompt="""You are a medical information orchestrator. Your role is to:
1. First use triage_tool to extract health terms and assess risk
2. For each extracted term that might be a medication, use rx_lookup_tool
3. Finally, use explainer_tool to create patient-friendly explanations

Keep responses clear and structured. Always maintain the flow: triage -> rx lookup -> explanation.""",
    tools=[triage_tool, rx_lookup_tool, explainer_tool]
)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run the orchestrator agent with a patient description.')
    parser.add_argument('description', type=str, help='Patient symptom description')
    args = parser.parse_args()

    # Run the orchestrator agent with the description
    response = orchestrator_agent(args.description)
    print("\nResponse:")
    print(response) 