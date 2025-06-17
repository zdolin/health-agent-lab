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
    max_parallel_tools=2,
    system_prompt="""You are a medical information orchestrator. Follow these steps and EXPLAIN your reasoning at each step:

1. First, explain your plan to investigate the health concern
2. Use triage_tool to extract high-risk health terms and assess risk
- Explain why you're using this tool
- Output the terms discovered
3. For the primary term that is a medication:
- Use rx_lookup_tool to get the drug information
- Explain what you're looking for in the FDA data
4. Create a patient-friendly explanation in paragraph format with:
- A heading that denotes the official start of the explanation
- Clear explanation of your findings and FDA data
5. Document all openFDA API calls made by the rx_lookup_tool
- openFDA API Call: [URL used]

IMPORTANT:
- Do NOT ask follow up questions.
- ALWAYS explain your reasoning before and after each tool use
- Provide real-time updates on your thought process
- You MUST include all relevant FDA data and openFDA API URLs used
""",
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