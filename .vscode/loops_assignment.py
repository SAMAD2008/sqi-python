# Print numbers from 1 to 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Print "Hello" 3 times
# Expected Output:
# Hello
# Hello
# Hello
count = 1
while count <= 3:
    print("Hello")
    count += 1

# count = 0
# while count < 3:
#     print("Hello")
#     count += 1

# Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10
num = 2
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

# Print numbers in reverse from 5 to 1 using a while loop.
# Expected Output:
# 5
# 4
# 3
# 2
# 1
n = 5
while n >= 1:
    print(n)
    n -= 1

# Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
m = 1
while m <= 10:
    if m != 5:
        print(m)
    m += 1

# Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3
# Output:
# ***
# ***
# ***
# Example 2:
# Input: 5
# Output:
# *****
# *****     
# *****
# *****
num_of_stars = int(input('Enter the number of stars: '))
i = 1
while i <= num_of_stars:
    print('*' * num_of_stars)
    i += 1

# Print a right triangle of stars
# Ask the user to enter a number
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****
num = int(input('Enter the number of rows: '))
i = 1
while i <= num:
    print('*' * i)
    i += 1

#  8. 	Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
# Example:
# Input: 5
# Output:
# 5
# 4
# 3
# 2
# 1
# Go!
start = int(input("Enter a number to start the countdown: "))
while start >= 1:
    print(start)
    start -= 1
print("Go!")

#  9. 	Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111
line = ""
count = 1
while count <= 10:
    line += "1"
    count += 1
print(line)

# 10.  Print a list of the first 12 multiples of 3 starting from 3
# multiple = 1
# count = 1
# while count <= 12:
#     print(multiple * 3)
#     multiple += 1
#     count += 1
list_of_multiples = []
i = 3
while len(list_of_multiples) < 12:
    list_of_multiples.append(1)
    i += 3

print(list_of_multiples)    


# Write a program that uses a while loop to print numbers from 1 to 10.
j = 1
while j <= 10:
    print(j)
    j += 1

# Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).
n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)

# Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.
import random
secret_number = random.randint(1, 50)
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    guess = int(input("Guess the secret number between 1 and 50: "))
    attempts += 1
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print("Congratulations! You've guessed the correct number.")
        
# Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.
password = ""
while password != "secret":
    password = input("Enter the password: ")
print("Access granted.")

# Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.
user_input = int(input("Enter a number for countdown: "))
while user_input >= 0:
    print(user_input)
    user_input -= 1

# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
n = int(input("Enter a number: "))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

    



