
import random
from getpass import getpass
print("******LOG IN DETAILS*******")
user_name = input("Enter your username: ")
password = getpass("Enter your password: ")
email = input("Enter your email: ")

computer_OTP = random.randint(1000,9999)
print(computer_OTP)
user_OTP = int(input("Enter the OTP sent to your email: "))
if user_OTP == computer_OTP:
    print(f"You have successfully logged in. Your username is {user_name} and your password is {password}. Your OTP is {user_OTP}")    
else:
    print("Invalid OTP. Try again")  

