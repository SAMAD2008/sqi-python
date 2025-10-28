# #Collect two numbers as input from the user and assign as variables, a and b, write an if 
# #statement that prints "a and b are both positive" if both a and b are positive, prints 
# #"Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# #neither is positive.
# user_input = input("Enter two numbers: ")
# a = int(user_input[0])
# b = int(user_input[1])
# if a > 0 and b > 0:
#     print("a and b are both positive")
# elif a > 0 or b > 0:
#     print("Only one is positive")
# else:
#     print("Neither is positive")    

# #Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
# user_input = input("Enter three numbers: ")
# x = int(user_input[0])
# y = int(user_input[1])
# z = int(user_input[2])
# if x < y < z:
#     print("Increasing order")
# elif x > y > z:
#     print("Decreasing order")
# else:
#     print("Neither")    

#Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
palindrome = input("Enter a string: ").lower().replace(' ', '')
if palindrome == palindrome[::-1]:
    print("Is a palindrome")
else:
    print("Not a palindrome")

#You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x == y == z:
    print("All same")
elif x == y or x == z or y == z:
    print("Two are equal")
else:
    print("All different")        


#Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))
if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("Valid triangle")    
else:
    print("Invalid triangle")

#You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
ch = input("Enter a character: ")
if ch in vowel:
    print("Vowel")
else:
    print("Consonant")    

#Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".
primary_colors = ['red', 'blue', 'yellow']
color1 = input("Enter first color: ")
color2 = input("Enter second color: ")
color3 = input("Enter third color: ")
if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
    print("All primary colors")
else:
    print("Not all primary colors")    

#You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".
modes = ['manual', 'automatic', 'off']
mode = input("Enter mode: ")
if mode == modes[0]:
    print("Manual mode activated")
elif mode == modes[1]:
    print("Automatic mode activated")
elif mode == modes[2]:
    print("System is off")        
else:
    print("System is off")        

#Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".
message = input("Enter your message: ")
if "urgent" in message or "important" in message or "immediate" in message:
    print("High priority message")
else:
    print("Normal message")    

#You have two variables, status1 and status2, provided through user input, each of 
#	which can be "active", “inactive", or "pending". Write an if statement to print 
#	"Both active" if both statuses are "active", "One active" if exactly one is "active",
#	and "None active" if neither is "active".
statuses = ['active', 'inactive', 'pending']
status1 = input("Enter first status: ")
status2 = input("Enter second status: ")
if status1 == statuses[0] and status2 == statuses[0]:
    print("Both active")
elif status1 == statuses[0] or status2 == statuses[0]:
    print("One active")
else:
    print("None active")            

#Given a string `filename` supplied by the user, write an if statement to check if the
#	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
#	print "Not an image file".
filename = input("Enter filename: ")
if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.gif'):
    print("Image file")
else:
    print("Not an image file")

#You have a variable `access_level` provided through user input which can be "admin",
# 	"user", or "guest". Write an if statement that prints "Full access" if access_level is
#	"admin", "Limited access" if it is "user", and "No access" if it is "guest".
access_levels = ['admin', 'user', 'guest']
access_level = input("Enter access level: ")
if access_level == access_levels[0]:
    print("Full access")
elif access_level == access_levels[1]:
    print("Limited access")
elif access_level == access_levels[2]:
    print("No access")        
            
#Given a string `email` collected from the user, write an if statement to check if the
#	email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
#	print "Invalid email".
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")    

#You have a variable `day` provided by user input which can be any day of the week 
#	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
#	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = input("Enter a day: ")
if day == days[5] or day == days[6]:
    print("Weekend")
else:
    print("Weekday")    

#Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
#	input from the user and prints the greatest number. Use conditional statements
#	to determine which number is the greatest. Bonus point if you can do it without `else` 
#	statements.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"The greatest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The greatest number is: {num2}")
elif num3 >= num1 and num3 >= num2:
    print(f"The greatest number is: {num3}")


