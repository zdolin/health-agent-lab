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
        'fever': r'\bfever\b|\btemperature\b|\bhot\b|\bchills\b|\bsweating\b',
        'chest pain': r'\bchest\s+pain\b|\bchest\s+discomfort\b|\bchest\s+pressure\b|\bchest\s+tightness\b',
        'shortness of breath': r'\bshortness\s+of\s+breath\b|\bdifficulty\s+breathing\b|\bbreathing\s+problems\b|\bbreathless\b|\bout\s+of\s+breath\b',
        'headache': r'\bheadache\b|\bhead\s+pain\b|\bmigraine\b|\bpounding\s+head\b|\bthrobbing\s+head\b',
        'nausea': r'\bnausea\b|\bqueasy\b|\bupset\s+stomach\b|\bfeel\s+sick\b|\bwant\s+to\s+vomit\b',
        'dizziness': r'\bdizziness\b|\bvertigo\b|\blightheaded\b|\bwoozy\b|\bunsteady\b',
        'fatigue': r'\bfatigue\b|\btired\b|\bexhausted\b|\bworn\s+out\b|\bweak\b|\blethargic\b',
        'cough': r'\bcough\b|\bcoughing\b|\bhacking\b|\bdry\s+cough\b|\bwet\s+cough\b',
        'sore throat': r'\bsore\s+throat\b|\bthroat\s+pain\b|\bscratchy\s+throat\b|\bswollen\s+throat\b',
        'muscle pain': r'\bmuscle\s+pain\b|\bmuscle\s+ache\b|\bmyalgia\b|\bjoint\s+pain\b|\bback\s+pain\b',
        'rash': r'\brash\b|\bskin\s+irritation\b|\bhives\b|\bitchy\s+skin\b|\bblisters\b',
        'abdominal pain': r'\babdominal\s+pain\b|\bstomach\s+pain\b|\bbelly\s+ache\b|\bcramps\b|\bbloating\b',
        'diarrhea': r'\bdiarrhea\b|\bloose\s+stools\b|\bwatery\s+bowel\b|\brunning\s+stomach\b',
        'constipation': r'\bconstipation\b|\bhard\s+stools\b|\bcant\s+go\b|\bblocked\b',
        'insomnia': r'\binsomnia\b|\bcant\s+sleep\b|\bsleep\s+problems\b|\btrouble\s+sleeping\b',
        'anxiety': r'\banxiety\b|\bnervous\b|\bworried\b|\bpanic\b|\bstress\b',
        'depression': r'\bdepression\b|\bsad\b|\bdown\b|\bhopeless\b|\bempty\b',
        'vision problems': r'\bblurred\s+vision\b|\bvision\s+problems\b|\bdouble\s+vision\b|\beye\s+pain\b',
        'ear pain': r'\bear\s+pain\b|\bearache\b|\bpressure\s+in\s+ear\b|\bpopping\s+ears\b',
        'urinary problems': r'\burinary\s+problems\b|\bfrequent\s+urination\b|\bburning\s+urination\b|\bblood\s+in\s+urine\b',
        'stroke symptoms': r'\bstroke\b|\bnumbness\b|\bweakness\b|\bparalysis\b|\bfacial\s+droop\b|\bslurred\s+speech\b|\bconfusion\b|\bsevere\s+headache\b',
        'seizure': r'\bseizure\b|\bconvulsion\b|\bfit\b|\buncontrollable\s+shaking\b|\bblack\s+out\b',
        'severe bleeding': r'\bsevere\s+bleeding\b|\bheavy\s+bleeding\b|\buncontrollable\s+bleeding\b|\bblood\s+loss\b',
        'severe pain': r'\bsevere\s+pain\b|\bexcruciating\s+pain\b|\bworst\s+pain\b|\bunbearable\s+pain\b',
        'loss of consciousness': r'\bloss\s+of\s+consciousness\b|\bpassed\s+out\b|\bfainted\b|\bblacked\s+out\b|\bunresponsive\b',
        'sudden confusion': r'\bsudden\s+confusion\b|\bdisorientation\b|\bmental\s+status\s+change\b|\bdelirium\b',
        'severe allergic reaction': r'\banaphylaxis\b|\bsevere\s+allergic\s+reaction\b|\bswelling\s+of\s+face\b|\bswelling\s+of\s+throat\b|\bdifficulty\s+swallowing\b',
        'high fever': r'\bhigh\s+fever\b|\bfever\s+over\s+103\b|\bsevere\s+fever\b|\bvery\s+high\s+temperature\b',
        'severe dehydration': r'\bsevere\s+dehydration\b|\bnot\s+urinating\b|\bdark\s+urine\b|\bvery\s+thirsty\b|\bdry\s+mouth\b',
        'poisoning': r'\bpoisoning\b|\boverdose\b|\bingested\s+poison\b|\bchemical\s+exposure\b|\btoxic\s+substance\b'
    }
    
    detected_terms = []
    text = text.lower()
    
    for term, pattern in health_terms.items():
        if re.search(pattern, text):
            detected_terms.append(term)
            
    return detected_terms 