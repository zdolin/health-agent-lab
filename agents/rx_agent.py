from strands import Agent
from strands_tools import http_request
from agents.config import bedrock_model

# Create the rx agent at module level so it can be imported
rx_agent = Agent(
    model=bedrock_model,
    system_prompt="""You are a prescription drug lookup assistant that uses the openFDA API to generate a very brief response.

MUST DO:
1. ALWAYS make the API call first using http_request like this:
{
"method": "GET",
"url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name:advil&limit=1",
"headers": {"Accept": "application/json"},
"metrics": true
}

2. Keep response very brief and structured:
```
Drug Information for [Drug Name]:
- Purpose: [purpose]
- Usage: [usage]
- Warnings: [warnings]
- Side Effects: [side effects]

Citations:
API Call: [URL used]
Source: openFDA API
Data Retrieved: [timestamp]
```

""",
    tools=[http_request]
)

def rx_handler(query: str) -> str:
    """
    Handle drug information queries using the rx agent.
    
    Args:
        query: The drug query (e.g., "what does the fda say about paxil")
        
    Returns:
        Drug information with FDA data and citations
    """
    response = rx_agent(query)
    return str(response)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run the rx agent with a drug query.')
    parser.add_argument('query', type=str, help='Drug query (e.g., "what does the fda say about paxil")')
    args = parser.parse_args()

    # Run the rx agent with the query
    response = rx_handler(args.query)
    print("\nResponse:")
    print(response)
