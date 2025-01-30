import random
import json
import time


def load_questions():

    with open("questions.json", "r") as f:
        questions = json.load(f) ["questions"]

    return questions


def get_random_questions(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)

    random_questions = random.sample(questions, num_questions)
    return random_questions


def ask_question(question):

    print(f"\n{question['question']}")
    for i, option in enumerate(question["options"]):
        print( f"{i+1}. {option}")

    # number = validate_number()
    number = int(input("\nYour Answer: "))
    if number < 1 or number > len(question["options"]):
        print("\nInvalid choice, defulting to wrong answer.")
        return False
    
    correct = question["options"] [number - 1] == question["answer"]
    return correct



# MAIN - Start Here -------------------------------------------------------------------------

questions = load_questions()

total_questions = int(input("\nEnter the Number of Questions: "))

random_questions = get_random_questions(questions, total_questions)

correct = 0

start_time = time.time()

for question in random_questions:
    is_correct = ask_question(question)
    if is_correct:
        correct += 1

    print("----------------------")

completed_time = time.time() - start_time
print("Summary")
print("Total Questions: ", total_questions)
print("Correct Answers: ", correct)
print(f"Score: {round(((correct / total_questions) * 100), 2)}%" )
print("Time: ", round( completed_time, 2), "mili-seconds")

















def validate_number():

    while True:
        number = input("\nSelect the Correct Number: ")
        try: 
            return float(number)
        except:
            print("Invalid number, try again")