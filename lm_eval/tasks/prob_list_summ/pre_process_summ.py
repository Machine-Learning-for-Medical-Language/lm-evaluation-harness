# # read shot.txt
# with open("lm_eval/tasks/prob_list_summ/shot.txt", "r") as file:
#     data = file.read()
import json

def process_summ(doc) -> str:
    options = ""
    for k, v in json.loads(doc['choices']).items():
        if v is not None:
            options += k + '. ' + v + '\n'
    return (
        "<Assessment>"
        + "\n"
        + doc["Assessment"].strip()
        + "\n"
        + "<Subjective>"
        + "\n"
        + doc["S"]
        + "\n"
        + options
        + "\nWhich choice is the most suitable one for a summarization of a list of relevant diagnoses or problems based on the information above in the Subjective, and Assessment sections? \n"
        + "Please answer with just A, B, C, D:"
    )
