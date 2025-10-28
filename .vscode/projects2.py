# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print('FizzBuzz') 
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz') 
#     else:
#         print(i)       
        
# # acronym generator
# user_input  = input('Enter a phrase: ').split() 
# acronym = []
# for input in user_input:
#     acronym.append(input[0].upper())
# print(''.join(acronym))

# # password generator
# from getpass import getpass
# user_password = getpass('Enter a phrase: ')
# system_password = 'abdussamad2007'
# if user_password == system_password:
#     print('Access granted')
# else:
#     print('Access denied')


# Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.
user_password = input('Enter password: ')
while len(user_password) >= 8 and len(user_password) <= 25:
    print('password is accepted')
    break

# Write a program that asks for the user's age and keeps prompting them until they 
# enter a valid age (greater than or equal to 0).
# Sample Input and Output:
# Enter your age: -5
# Invalid age. Please enter a valid age.
# Enter your age: 25
# Age accepted.
user_age = input('Enter your age')

# Write a program that tracks the inventory of items in a store. The user should be able 
# to add or remove items and the program should display the current inventory after each
# operation. The program stops when the user decides to exit.
# The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# Sample Input and Output:
# Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit





