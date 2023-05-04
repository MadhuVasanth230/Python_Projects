print("--------- Welcome to MyQuiz ---------------")
print()
user = input("Enter Your Name : ")
print()
print(f"--------- Hello {user}! ------------------- ")
print()
play = input("Do you want to start the quiz? (Yes/No)")
print()

if play != "Yes":
    quit()

score = 0


# question re-usable function
def question(question, option1, option2, correctAns):
    print(f"--> {question} ?")
    print(f"A) {option1} ")
    print(f"B) {option2}")
    answer = input("Choose an option : ")
    print()
    if answer == correctAns:
        print("--- Correct Answer!")
        return 1
    else:
        print("--- Wrong Answer!")
        return 0


# questions
score += question("what is python", "Programming Language",
                  "Snake", "A")
print()
score += question("What is Interpreter", "Executes each line of code",
                  "Executes all code at once", "A")
print()
score += question("Is Python supports oops", "Yes", "No", "A")
print()
score += question("Python is dynamically typed language",
                  "No", "Yes", "B")
print()
score += question("Lists are mutable", "No", "Yes", "B")
print()
# Score
print(f"{user} -> your score is : {score}")
