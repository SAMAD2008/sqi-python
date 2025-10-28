
from random import randint
score = 0
computer_guess1 = randint(1,20)
computer_guess2 = randint(1,20)
computer_guess3 = randint(1,20)
print(computer_guess1)
print(computer_guess2)
print(computer_guess3)
user_guess = input("Guess three numbers between 1 and 20: ").split()
guess1, guess2, guess3 = user_guess
guess1, guess2, guess3 = int(guess1), int(guess2), int(guess3)
if guess1 == computer_guess1:
    score += 5
    print("Wow!! your guess is correct")

if guess2 == computer_guess2:
    score += 5
    print("Wow!! Your second guess was correct")    

if guess3 == computer_guess3:
    score += 5
    print("Wow!! Your third guess was correct")    
       
if score >= 10:
    print("Wow!! You passed")
else:
    print("Sorry. Try again")   

print(f"Your total score is {score}/15")    





   









