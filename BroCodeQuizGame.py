#BroCode Quiz Game

questions = ("What is the most common cattle breed used for beef production in South Africa?",
             "Which province in South Africa is known for large-scale cattle farming?",
             "What is the primary purpose of Nguni cattle in South African farming?",
             "Which factor is most important for maintaining healthy cattle?",
             "What is a common disease affecting cattle in South Africa?")

options = (("A. Nguni", "B. Brahman", "C. Hereford", "D. Simmental"),
           ("A. Gauteng", "B. KwaZulu-Natal", "C. Western Cape", "D. Northern Cape"),
           ("A. Meat production", "B. Leather production", "C. Draught power", "D. Hides and ceremonial use"),
           ("A. Regular vaccinations", "B. Keeping them in small spaces", "C. Feeding only grass", "D. Avoiding all supplements"),
           ("A. Foot-and-mouth disease", "B. Common cold", "C. Malaria", "D. Tuberculosis"))

answers = ("A", 
           "D", 
           "D", 
           "A", 
           "A")


guesses = []

score = 0

question_num = 0


for question in questions:
    print("-----------------------------------------------------------------------------")
    print(question, "\n")
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("---------------------")
print("     RESULTS     ")
print("---------------------")


print("Answers: ", end="")
for answer in answers: 
    print(answer, end=" ")
print()


print("Quesses: ", end="")
for guess in guesses: 
    print(guess, end=" ")
print()

score = round( (score / len(questions) * 100) , 2)
print(f"Score: { score }%" )




