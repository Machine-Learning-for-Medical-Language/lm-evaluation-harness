# String representation of a dictionary
options = '''
Question: Which of the following statements is correct about the text above?
A. the text describes chief complaint, history of present illness, medical history, surgical history, family history, social history, review of systems, current medications or allergies.
B. the text describes vital signs, physical exam findings, laboratory data, imaging results, other diagnostic data, recognition and review of the documentation of other clinicians.
C. the text describes the problems and diagnosis for the patient. (d). the text describes the future testing and consultation needed for the
patient.
D. none of them is correct
Answer: 
''' 

def process_soap(doc) -> str:
    return (
        doc["input"].strip()
        + "\n"
        + options
    )
