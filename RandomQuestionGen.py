import random   # Importing random module for selecting random questions
import json     # Importing json module for reading questions from a JSON file
import time     # Importing time module for tracking the quiz duration

# Function to load questions from a JSON file
def load_questions():
    # Open the questions.json file in read mode
    with open("questions.json", "r") as f:
        # Load the JSON data and extract the "questions" list
        questions = json.load(f)["questions"]
    
    return questions  # Return the list of questions


# Function to randomly select a specified number of questions
def get_random_questions(questions, num_questions):
    # Ensure that num_questions does not exceed the available questions
    if num_questions > len(questions):
        num_questions = len(questions)

    # Select 'num_questions' random questions from the list
    random_questions = random.sample(questions, num_questions)
    return random_questions  # Return the selected random questions


# Function to display a question and get the user's answer
def ask_question(question):
    # Print the question text
    print(f"\n{question['question']}")
    
    # Print each option with its number
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    # Get user input for answer selection
    number = int(input("\nYour Answer: "))
    
    # Validate if the input is within the range of available options
    if number < 1 or number > len(question["options"]):
        print("\nInvalid choice, defaulting to wrong answer.")
        return False  # Return False as an incorrect answer
    
    # Check if the selected answer matches the correct answer
    correct = question["options"][number - 1] == question["answer"]
    return correct  # Return True if correct, False otherwise


# ---------------- MAIN PROGRAM STARTS HERE ----------------

# Load the list of questions from the JSON file
questions = load_questions()

# Ask the user how many questions they want in the quiz
total_questions = int(input("\nEnter the Number of Questions: "))

# Select a random subset of questions based on user input
random_questions = get_random_questions(questions, total_questions)

correct = 0  # Variable to store the count of correct answers

start_time = time.time()  # Record the start time of the quiz

# Loop through each randomly selected question
for question in random_questions:
    is_correct = ask_question(question)  # Ask the question and check the answer
    if is_correct:
        correct += 1  # Increase correct count if the answer is correct
    
    print("----------------------")  # Separator for readability

# Calculate the total time taken for the quiz
completed_time = time.time() - start_time

# Display the quiz summary
print("Summary")
print("Total Questions: ", total_questions)
print("Correct Answers: ", correct)
print(f"Score: {round(((correct / total_questions) * 100), 2)}%" )
print("Time: ", round(completed_time, 2), "milliseconds")  # Time taken for the quiz


# Function to validate that the user enters a number
def validate_number():
    while True:
        number = input("\nSelect the Correct Number: ")  # Prompt the user for input
        try: 
            return float(number)  # Convert input to float and return
        except:
            print("Invalid number, try again")  # Handle invalid input and ask again
