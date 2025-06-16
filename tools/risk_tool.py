from typing import List
from strands.tools import tool

@tool
def assess_risk(symptoms: List[str]) -> str:
    """
    Assess the risk level based on reported symptoms.
    
    Args:
        symptoms (List[str]): List of symptoms to assess
        
    Returns:
        str: A message indicating the risk level and recommended action
    """
    high_risk_symptoms = {
        'chest pain',
        'shortness of breath',
        'severe bleeding',
        'loss of consciousness',
        'severe head injury',
        'stroke symptoms',
        'seizure',
        'severe allergic reaction',
        'high fever',
        'severe pain',
        'sudden confusion',
        'severe dehydration',
        'poisoning',
        'severe abdominal pain',
        'severe vomiting',
        'severe diarrhea',
        'severe burns',
        'severe trauma',
        'severe neck pain',
        'severe back pain'
    }
    
    # Check if any high-risk symptoms are present
    high_risk_found = any(symptom in high_risk_symptoms for symptom in symptoms)
    
    if high_risk_found:
        return ("CAUTION: High-risk symptoms detected. "
                "Please seek immediate medical attention or call emergency services.")
    else:
        return ("These symptoms appear non-urgent. "
                "However, if symptoms worsen or new symptoms develop, "
                "please consult with a healthcare provider.") 