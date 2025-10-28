# Project Overview:
# Develop a simple Computer-Based Testing (CBT) program in Python that hardcodes a set of 
# at least 5 objective questions and their answers. The program should ask these questions 
# to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Answers:
# Create at least 5 objective questions (multiple choice or true/false).
# Hardcode these questions and their correct answers in your program.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Compare the user's answers with the correct answers.
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score.
# Sample Questions:
# What is 2 + 2?
# a) 3
# b) 4
# c) 5
# d) 6
# What color is the sky on a clear day?
# a) Red
# b) Blue
# c) Green
# d) Yellow
# How many legs does a spider have?
# a) 6
# b) 7
# c) 8
# d) 9
# What sound does a cow make?
# a) Meow
# b) Bark
# c) Moo
# d) Quack
# What is the opposite of 'hot'?
# a) Warm
# b) Cold
# c) Cool
# d) Boiling
# Sample Execution:

# 1. What is 2 + 2?
# a) 3
# b) 4
# c) 5
# d) 6

# Enter an option from a to d: b

# 2. What color is the sky on a clear day?
# a) Red
# b) Blue
# c) Green
# d) Yellow

# Enter an option from a to d: b

# 3. How many legs does a spider have?
# a) 6
# b) 7
# c) 8
# d) 9

# Enter an option from a to d: c
# Sample Execution Cont’d:

# 4. What sound does a cow make?
# a) Meow
# b) Bark
# c) Moo
# d) Quack

# Enter an option from a to d: c

# 5. What is the opposite of 'hot'?
# a) Warm
# b) Cold
# c) Cool
# d) Boiling

# Enter an option from a to d: b
# At the end of the CBT exam, you scored 5 points.

questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "answer": "b"
    },
    {
        "question": "What color is the sky on a clear day?",
        "options": ["a) Red", "b) Blue", "c) Green", "d) Yellow"],
        "answer": "b"
    },
    {
        "question": "How many legs does a spider have?",
        "options": ["a) 6", "b) 7", "c) 8", "d) 9"],
        "answer": "c"
    },
    {
        "question": "What sound does a cow make?",
        "options": ["a) Meow", "b) Bark", "c) Moo", "d) Quack"],
        "answer": "c"
    },
    {
        "question": "What is the opposite of 'hot'?",
        "options": ["a) Warm", "b) Cold", "c) Cool", "d) Boiling"],
        "answer": "b"
    }
]

score = 0
for question in questions:
    print(question["question"])
    options = question["options"]
    print("\n".join(options))
    user_answer = input("Enter an option from a to d: ")
    if user_answer == question["answer"]:
        score += 1
    else:
        print('Incorrect')


print(f'At the end of the CBT test. You scored {score} points.')