# # Write a program that takes an integer input from the user and uses a loop to calculate 
# # the sum of its digits. Print the sum. Example:
# # Input: 1234
# # Output: 10 (1+2+3+4)
# num = int(input("Enter an integer: "))
# sum_of_digits = 0
# for digit in str(num):
#     sum_of_digits += int(digit)
# print(f'Sum of digits: {sum_of_digits}')
# # Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# # Input: "hello world"
# # Output: Vowels: 3, Consonants: 7
# user_input = input("Enter a string: ").lower()
# vowels = "aeiou"
# vowel_count = 0
# consonant_count = 0
# for char in user_input:
#     if char in vowels:
#         vowel_count += 1
#     else:
#         consonant_count += 1
# print(f'Vowels: {vowel_count}, Consonants: {consonant_count}')

# # Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# # Input: 5
# # Output:
# # 5 x 1 = 5
# # 5 x 2 = 10
# # 5 x 3 = 15
# # ...
# # 5 x 12 = 60
# num = int(input("Enter an integer for multiplication table: "))
# for i in range(1, 13):
#     print(f'{num} x {i} = {num * i}')

# Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"
# user_input = input("Enter a string to reverse: ")

# reversed_string = ""
# for i in range(len(user_input) - 1,  -1, -1):
#     # print(f'Character: {user_input[i]}')
#     reversed_string += user_input[i]
# print(f'Reversed string: {reversed_string}')


# Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]
# user_input = input("Enter a list of numbers (comma-separated): ")
# num_list = user_input.split(',')
# unique_list = []
# for num in num_list:
#     if num not in unique_list:
#         unique_list.append(num)
# print(f'List without duplicates: {unique_list}')

# # Collect a list of numbers from the user (entered as comma-separated values) and use a 
# # loop to find and print the largest number in the list. Don’t use the built-in max 
# # function or anything similar.
# # Input: "10, 20, 5, 15"
# # Output: 20
# user_input = input("Enter a list of numbers (comma-separated): ")
# num_list = [int(num) for num in user_input.split(',')]
# largest_num = num_list[0]
# for num in num_list:
#     if num > largest_num:
#         largest_num = num
# print(f'Largest number: {largest_num}')

# Write a program that takes an integer n from the user and calculates the sum of all 
# even numbers from 1 to n. Print the sum.
# Input: 10
# Output: 30 (2 + 4 + 6 + 8 + 10)
