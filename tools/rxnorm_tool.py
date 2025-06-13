from typing import Dict, Any
from strands.tools import tool
from strands_tools.utils import http_request
import json

@tool
def fetch_rxnorm_data(term: str) -> Dict[str, Any]:
    """
    Fetch RxNorm data for a given medication term using the RxNav API.
    
    Args:
        term (str): The medication name or term to search for
        
    Returns:
        Dict[str, Any]: A dictionary containing the RxNorm data, including:
            - rxcui: The RxNorm Concept Unique Identifier if found
            - status: Success or error message
            - error: Error details if any
            
    Example:
        >>> result = fetch_rxnorm_data("aspirin")
        >>> print(result)
        {'rxcui': '1191', 'status': 'success'}
    """
    try:
        # Construct the API URL
        url = f"https://rxnav.nlm.nih.gov/REST/rxcui.json?name={term}"
        
        # Make the HTTP request
        response = http_request(url)
        
        # Parse the JSON response
        data = json.loads(response)
        
        # Check if we got a valid response with an RxCUI
        if 'idGroup' in data and 'rxnormId' in data['idGroup']:
            return {
                'rxcui': data['idGroup']['rxnormId'][0],
                'status': 'success'
            }
        else:
            return {
                'status': 'not_found',
                'error': f"No RxNorm data found for term: {term}"
            }
            
    except Exception as e:
        return {
            'status': 'error',
            'error': f"Failed to fetch RxNorm data: {str(e)}"
        } 