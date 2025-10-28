# Write a Python program that works as a quote generator. The program should display all available categories of quotes to the user. The user can then choose a category, and the program will show a quote that belongs to that category. If the user enters a category that does not exist, the program should let them know that the category is invalid.
from random import randint, choice  
quotes = {
    "inspirational": [
        "The best way to get started is to quit talking and begin doing. - Walt Disney",
        "Don't let yesterday take up too much of today. - Will Rogers",
        "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi"
    ],
    "humor": [
        "I'm on a whiskey diet. I've lost three days already. - Tommy Cooper",
        "I used to think I was indecisive, but now I'm not too sure. - Unknown",
        "I told my wife she was drawing her eyebrows too high. She looked surprised. - Unknown"
    ],
    "life": [
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "Get busy living or get busy dying. - Stephen King"
    ]
}
print("Welcome to the Quote Generator!")
user_choice = input ("Please choose a category: ").lower()
if user_choice in quotes:
    print(choice(quotes[user_choice]))
else:
    print("Invalid category. Please choose from the available categories.")    



# Write a Python program that generates a random password for the user. The program should allow the user to choose what type of characters they want in their password. The options are: only numbers; letters and numbers; or letters, numbers, and symbols. Once the user makes a choice, the program should generate and display a password that matches their selection.
import string 
import random
digits = string.digits
punctuations =string.punctuation
letters = string.ascii_letters

option = int(input("""
1. Digits only
2. Digits and letters                              
3. Digits, Letters and punctuations               
               """))

if option == 1:
    password = random.sample(digits, 8)
    password_string = ''.join(password)
    print("Your password is: ", password_string)
elif option == 2:
    letters = ''.join(random.sample(letters, 5))
    numbers = ''.join(random.sample(digits, 3))   
    
    password = list(letters + numbers)
    random.shuffle(password) 
    password = ''.join(password)
    print(password)



# Modify your quiz program to include more questions in the list. And instead of selecting questions randomly, update the program so that a user can choose which question number they want to answer. For example, if the user enters the number 3, the program should display the third question in the list for them to answer. (I suggest you copy the quiz code and modify it instead of touching the exact one we did in the class).
from random import choice
print("*******WELCOME TO QUIZ GAME********")
quiz_questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["Tuple", "List", "String", "Integer"],
        "answer": "List"
    },
    {
        "question": "How do you create a dictionary in Python?",
        "options": ["Using curly braces {}", "Using square brackets []", "Using parentheses ()", "Using angle brackets <>"],
        "answer": "Using curly braces {}"
    },
    {
        "question": "What is the output of print(len('Hello World'))?",
        "options": ["10", "11", "12", "13"],
        "answer": "11"
    }
]
random_quiz = choice(quiz_questions)
question = random_quiz["question"]
options = random_quiz["options"]
answer = random_quiz["answer"]
print(question)
print("Choose the correct option: ")
print('\n'.join(options))
choice = input()
if choice == answer:
    print("Correct answer!")
else:
    print("Wrong answer. Try again!")    



