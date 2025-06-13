from typing import List
import re
from strands.tools import tool

@tool
def extract_health_terms(text: str) -> List[str]:
    """
    Extract potential health-related terms from input text.
    
    Args:
        text (str): The input text to analyze for health-related terms
        
    Returns:
        List[str]: A list of detected health-related terms
    """
    # Common health-related terms and their variations
    health_terms = {
        'fever': r'\bfever\b|\btemperature\b|\bhot\b',
        'chest pain': r'\bchest\s+pain\b|\bchest\s+discomfort\b',
        'shortness of breath': r'\bshortness\s+of\s+breath\b|\bdifficulty\s+breathing\b|\bbreathing\s+problems\b',
        'headache': r'\bheadache\b|\bhead\s+pain\b',
        'nausea': r'\bnausea\b|\bqueasy\b|\bupset\s+stomach\b',
        'dizziness': r'\bdizziness\b|\bvertigo\b|\blightheaded\b',
        'fatigue': r'\bfatigue\b|\btired\b|\bexhausted\b',
        'cough': r'\bcough\b|\bcoughing\b',
        'sore throat': r'\bsore\s+throat\b|\bthroat\s+pain\b',
        'muscle pain': r'\bmuscle\s+pain\b|\bmuscle\s+ache\b|\bmyalgia\b'
    }
    
    detected_terms = []
    text = text.lower()
    
    for term, pattern in health_terms.items():
        if re.search(pattern, text):
            detected_terms.append(term)
            
    return detected_terms 