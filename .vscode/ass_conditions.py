from getpass import getpass

# A customer has ₦10,000 in their bank account. Write a program that asks how much they want to withdraw. If the withdrawal is greater than the balance, print “Insufficient funds.” If it is equal to the balance, print “Account will be empty.” Otherwise, print “Withdrawal successful. New balance is …”   Example: If they enter 6000, display “Withdrawal successful. New balance is 4000.”
balance = 10000
withdrawal = int(input("Enter amount to withdraw: ")) 
new_balance = balance - withdrawal
if withdrawal > balance:
    print("Insufficient funds.")
elif withdrawal == balance:
    
    print("Account will be empty.")
else:
    print(f"Withdrawal successful. New balance is {new_balance}.")        

# The price of an item is ₦5,000. Ask the user for a coupon code. If they enter "SAVE10", give a 10% discount. If they enter "SAVE20", give a 20% discount. Otherwise, print the full price. Example: If they enter SAVE20, display “Final price: ₦4000.”
price = 5000
coupon = input("Enter coupon code: ")
if coupon == "SAVE10":
    final_price = price * 0.9
    print(f"Final price: ₦{final_price}")
elif coupon == "SAVE20":
    final_price = price * 0.8
    print(f"Final price: ₦{final_price}")
else:
    print(f"Final price: ₦{price}")        

# Have a variable called user that stores login details, e.g. user = {"username": "user11", "password": "pass@word"}. Ask the user to enter a username and password. If it matches the already stored data, print “Login Successful,” otherwise, print "Account not found."  Example: If they enter user11 and pass@wo, display “Account not found”
user = {"username": "user11", "password": "pass@word"}
username = input("Enter username: ")
password = getpass("Enter password: ")

if username == user["username"] and password == user["password"]:
    print("Login Successful")
else:
    print("Account not found.")        

# The dictionary students_payment_status = {"Ada": True, "Bolu": False, "Chioma": True} stores students and whether they have paid their school fees. Ask for a student’s name. If the student has paid, print “Fee paid.” If not, print “Fee not paid.” If the name is not found, print “Student not registered.” Example: If they enter Bolu, display “Fee not paid.”
students_payment_status = {"Ada": True, "Bolu": False, "Chioma": True}
name = input("Enter student name: ")
if name not in students_payment_status:
    print(f'{name} does not exist among your students')
    exit()

if students_payment_status[name] == True:
    print('Fee paid')
else:
    print("Fee not paid.")            

# Ask the user how much airtime they want to recharge. If the amount is ₦1,000 or more, give 20% bonus. If it is ₦500 or more, give 10% bonus. Otherwise, no bonus. Print the bonus and the total airtime received. Example: If they enter 1200, say “You got ₦240 bonus, total ₦1440.”
amount = int(input("Enter amount to recharge: "))
if amount >= 1000:
    bonus = amount * 0.2
    total = amount + bonus
    print(f"You got ₦{bonus} bonus, total ₦{total}.")
elif amount >= 500:
    bonus = amount * 0.1
    total = amount + bonus
    print(f"You got ₦{bonus} bonus, total ₦{total}.")
else:
    bonus = 0
    total = amount + bonus
    print(f"You got ₦{bonus} bonus, total ₦{total}.")        

 