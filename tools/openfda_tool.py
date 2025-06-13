from typing import Dict, Any
from strands.tools import tool
from strands_tools.utils import http_request
import json

@tool
def fetch_drug_label(term: str) -> Dict[str, Any]:
    """
    Fetch drug label information from the OpenFDA API for a given medication term.
    
    Args:
        term (str): The medication name to search for
        
    Returns:
        Dict[str, Any]: A dictionary containing the drug label information:
            - brand_name: The brand name of the medication
            - generic_name: The generic name of the medication
            - purpose: The purpose/indications of the medication
            - warnings: Any warnings associated with the medication
            - status: Success or error message
            - error: Error details if any
            
    Example:
        >>> result = fetch_drug_label("aspirin")
        >>> print(result)
        {
            'brand_name': 'Bayer Aspirin',
            'generic_name': 'aspirin',
            'purpose': ['Pain reliever', 'Fever reducer'],
            'warnings': ['May cause stomach bleeding...'],
            'status': 'success'
        }
    """
    try:
        # Construct the API URL
        url = f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:{term}&limit=1"
        
        # Make the HTTP request
        response = http_request(url)
        
        # Parse the JSON response
        data = json.loads(response)
        
        # Check if we got any results
        if not data.get('results'):
            return {
                'status': 'not_found',
                'error': f"No drug label found for term: {term}"
            }
            
        # Extract the first result
        result = data['results'][0]
        
        # Extract relevant information
        response_data = {
            'status': 'success',
            'brand_name': result.get('openfda', {}).get('brand_name', ['Unknown'])[0],
            'generic_name': result.get('openfda', {}).get('generic_name', ['Unknown'])[0],
            'purpose': result.get('purpose', ['Not specified']),
            'warnings': result.get('warnings', ['No warnings specified'])
        }
        
        return response_data
            
    except Exception as e:
        return {
            'status': 'error',
            'error': f"Failed to fetch drug label: {str(e)}"
        } 