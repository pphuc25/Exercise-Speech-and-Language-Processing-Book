import re

class AnswerCase:
    def __init__(self) -> None:
        self.negative_case_pattern = r".*I.*(?:feeling|feel|felt).*(depressed|sad|down|upset|irrated|mad|crazy|angry|anxious|stressed|bad|blue).*"
        self.positive_case_pattern = r".*I.*(?:feeling|feel|felt).*(glad|happy|grateful|up|optimistic|good|excited|great|well).*"

    def postive_case(self, user_sentence):
        comp = re.compile(self.negative_case_pattern)
        output = comp.sub(r"I'm glad to hear that. Why do you feel \1?", user_sentence)
        return output.capitalize()

    def negative_case(self, user_sentence):
        comp = re.compile(self.negative_case_pattern)
        output = comp.sub(r"Why do you think you feel \1?", user_sentence)
        return output.capitalize()
    
    def don_know_case(self):
        output = "I don't understand too much about what you talking"
        return output
    
def return_match_case(all_cases, user_sentence):
    for case in all_cases:
        if re.match(case, user_sentence):
            case_choice = all_cases.index(case)
            break
        else:
            case_choice = None
    return case_choice

def excecute_cases_fn(cases, case_choice):
    call_function_cases = {
        0: cases.postive_case(user_sentence), 
        1: cases.negative_case(user_sentence),
    }
    answer = call_function_cases.get(case_choice, cases.don_know_case())
    return answer

def main(user_sentence, cases):
    all_cases = [cases.positive_case_pattern, cases.negative_case_pattern]
    case_choice = return_match_case(all_cases, user_sentence)
    answer = excecute_cases_fn(cases, case_choice)
    print(answer)
    
if __name__ == "__main__":
    cases = AnswerCase()
    user_sentence = "I am feeling sad today."
    while True:
        main(user_sentence, cases)
        break
