import ast

# String representation of a dictionary
string = "{'A': 'Direct', 'B': 'Not Relevant', 'C': 'Indirect', 'D': 'Neither'}"

# Converting the string to a dictionary and constructing the options string
options = ''.join(f"{k}. {v}\n" for k, v in ast.literal_eval(string).items() if v is not None)

def process_ap(doc) -> str:
    return (
        '<Assessment>\n'
        + doc["Assessment"].strip()
        + "\n"
        +'<Plan Subsection>\n'
        + doc["Plan Subsection"].strip()
        + "\n"
        + options
        + "\nPlease determine the relationship between given Assessment and Plan Subsection: \n"
        + "Answer:"
    )
