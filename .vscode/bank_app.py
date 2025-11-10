# Project Overview:
# You are tasked with creating a command-line banking application that simulates the basic operations
# of a real bank. This application will allow users to register, log in, and perform various banking transactions. Your application will use SQL to interact with a database, ensuring data persistence
# and secure handling of user information. 
# Objective: The goal of this project is to design and implement a functional banking application that securely handles user data and transactions. You will gain hands-on experience in integrating Python with SQL, managing user authentication, and performing basic banking operations like deposits, withdrawals, and balance checks.

# Operations:
# Your application should support the following operations:
# 1. User Registration:
# - Users should be able to create a new account by providing necessary details such as full name, username, password, and initial deposit and be assigned an account number automatically.
# - Store user data securely in the database.

# 2. User Login:
# - Registered users should be able to log in using their username and password.
# - Validate credentials against the data stored in the database.

# 3. Banking Transactions:
# - Deposit: Allow logged in users to deposit money into their account.
# - Withdrawal: Allow logged in users to withdraw money, ensuring sufficient balance.
# - Balance Inquiry: Display the current balance of the logged in user's account.
# - Transaction History: Provide a history of all transactions performed by the logged in user.
# - Transfer: Allow logged in users to transfer money to other users’ accounts using their account    
#   Number.
# - Account Details: The user should be able to check their account details at once i.e their full name, username, account number.
# User Interface:
# - The application should run entirely in the terminal, with clear and user-friendly prompts.
# - ENSURE INPUT VALIDATION AND ERROR HANDLING THROUGHOUT THE APPLICATION.
# - Display informative messages for successful operations or errors.

# Additional Guidelines:
# - Use SQL (with sqlite3) to manage user accounts and transaction records.
# - Ensure that passwords are securely stored and not in plain text.
# - Handle edge cases like incorrect login details, insufficient funds, and invalid inputs.

# Note:
# - Users need to be logged in to perform any banking transactions.
# - You will need another table to store the transactions performed by users (tip - create a foreign key relationship between the users table and the transactions table).

# Resources:
# If you need help working with Python and SQL, check out this video on Python and SQL integration.
# Or check out this article.
# This project will challenge your understanding of Python, databases, and user interaction, giving you practical skills that are essential for real-world application development.
# User Registration Validation:
# Full Name:
# - Ensure the full name only contains alphabetic characters (letters and spaces).
# - Reject empty names. Minimum length for full name is 4 characters. Max is 255.

# Username:
# - Check that the username is not empty and is unique (no duplicates in the database).
# - Enforce length constraints (i.e., between 3 and 20 characters).
# - Ensure only valid characters are used (alphanumeric, underscores).

# Password:
# - Enforce a minimum length (i.e., 8 characters) and maximum length of 30 characters.
# - Ensure it contains at least one uppercase letter, one lowercase letter, one number, and one special character.
# - Use the getpass module for blind typing the password.

# Initial Deposit:
# - Ensure it is a numeric value.
# - Check that the deposit is above the minimum balance required (i.e., minimum of 2000 naira to open an account).
# - Reject negative values.
# Account number:
# - Generate a random account number of 8 digits.
# - Make sure that the generated account number does not already belong to an existing user.
# 2. User Login Validation
# Username:
# - Ensure the username exists in the database.
# - Validate against allowed characters i.e. (alphanumeric, underscores)..

# Password:
# - Ensure the password is entered and matches the stored hashed password for the given username.
# - Reject blank passwords (i.e. empty or just whitespace).

# 3. Deposit Transaction Validation
# Deposit Amount:
# - Ensure the amount is a valid positive number (no negative values or letters).
# - Reject blank deposit amounts (i.e. empty or just whitespace)
# 4. Withdrawal Transaction Validation
# Withdrawal Amount:
# - Ensure the amount is a valid positive number.
# - Validate that the amount does not exceed the available balance.
# - Reject non-numeric or negative values.
# - Reject blank withdrawal amounts (i.e. empty or just whitespace)
# 5. Transaction History
# - If there are no transactions, display that there are no transactions.
# - If there are transactions, display them nicely
# 6. Transfer Validation
# Recipient Account Number:
# - Ensure that the account number is numeric and exists in the database.
# - Ensure that the recipient account number is not the same as the logged-in user's account number (prevent self-transfers).

# Transfer Amount:
# - Ensure the amount is a positive number.
# - Check that the amount does not exceed the sender’s balance.
# - Reject non-numeric or negative values or blank values.

# 7. General Input Validations
# Session Validation: Ensure the user is logged in before accessing any features except for registration and login.

# 8. SQL Injection Prevention:
# Ensure all inputs are validated and properly handled using parameterized queries to avoid SQL injection attacks. I.e. use the ? for parameters in sql queries.

# 9. Program Flow
# - Use time.sleep() for a slight delay after different actions to simulate the waiting/loading time in a real bank application.
# - When user registers, take them straight to log in, not to the main menu.
# - Redisplay the menu after every completed action, so the user does not have to scroll to see what numbers correspond to different options.
import sqlite3
import hashlib
import getpass
import re
import random
import time
from datetime import datetime

class BankingApp:
    def __init__(self):
        self.conn = sqlite3.connect('banking.db')
        self.cursor = self.conn.cursor()
        self.current_user = None
        self.setup_database()
    
    def setup_database(self):
        """Initialize database tables"""
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                account_number TEXT UNIQUE NOT NULL,
                balance REAL NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
     
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                amount REAL NOT NULL,
                recipient_account TEXT,
                balance_after REAL NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        self.conn.commit()
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def generate_account_number(self):
        """Generate unique 8-digit account number"""
        while True:
            account_number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
            self.cursor.execute('SELECT account_number FROM users WHERE account_number = ?', (account_number,))
            if not self.cursor.fetchone():
                return account_number
    
    def validate_full_name(self, name):
        """Validate full name"""
        if not name or name.strip() == '':
            return False, "Full name cannot be empty."
        
        name = name.strip()
        if len(name) < 4:
            return False, "Full name must be at least 4 characters long."
        if len(name) > 255:
            return False, "Full name must not exceed 255 characters."
        
        if not re.match(r'^[a-zA-Z\s]+$', name):
            return False, "Full name can only contain letters and spaces."
        
        return True, name
    
    def validate_username(self, username):
        """Validate username"""
        if not username or username.strip() == '':
            return False, "Username cannot be empty."
        
        username = username.strip()
        if len(username) < 3 or len(username) > 20:
            return False, "Username must be between 3 and 20 characters."
        
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscores."
        
        self.cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
        if self.cursor.fetchone():
            return False, "Username already exists. Please choose another."
        
        return True, username
    
    def validate_password(self, password):
        """Validate password strength"""
        if not password or len(password) == 0:
            return False, "Password cannot be empty."
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        if len(password) > 30:
            return False, "Password must not exceed 30 characters."
        
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter."
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter."
        if not re.search(r'\d', password):
            return False, "Password must contain at least one number."
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False, "Password must contain at least one special character."
        
        return True, password
    
    def validate_amount(self, amount_str, allow_zero=False):
        """Validate numeric amount"""
        if not amount_str or amount_str.strip() == '':
            return False, "Amount cannot be empty.", 0
        
        try:
            amount = float(amount_str.strip())
            if amount < 0:
                return False, "Amount cannot be negative.", 0
            if not allow_zero and amount == 0:
                return False, "Amount must be greater than zero.", 0
            return True, "", amount
        except ValueError:
            return False, "Invalid amount. Please enter a numeric value.", 0
    
    def register(self):
        """Register a new user"""
        print("\n" + "="*50)
        print("USER REGISTRATION")
        print("="*50)
  
        while True:
            full_name = input("\nEnter your full name: ").strip()
            valid, result = self.validate_full_name(full_name)
            if valid:
                full_name = result
                break
            print(f"Error: {result}")

        while True:
            username = input("Enter username: ").strip()
            valid, result = self.validate_username(username)
            if valid:
                username = result
                break
            print(f"Error: {result}")
  
        while True:
            password = getpass.getpass("Enter password: ")
            valid, result = self.validate_password(password)
            if valid:
                confirm_password = getpass.getpass("Confirm password: ")
                if password != confirm_password:
                    print("Error: Passwords do not match. Please try again.")
                    continue
                password = result
                break
            print(f"Error: {result}")
     
        while True:
            deposit_str = input("Enter initial deposit (minimum ₦2000): ").strip()
            valid, msg, deposit = self.validate_amount(deposit_str)
            if not valid:
                print(f"Error: {msg}")
                continue
            if deposit < 2000:
                print("Error: Minimum deposit of ₦2000 is required to open an account.")
                continue
            break
        
        account_number = self.generate_account_number()
       
        hashed_password = self.hash_password(password)
        
        try:
            self.cursor.execute('''
                INSERT INTO users (full_name, username, password, account_number, balance)
                VALUES (?, ?, ?, ?, ?)
            ''', (full_name, username, hashed_password, account_number, deposit))
            
            user_id = self.cursor.lastrowid
          
            self.cursor.execute('''
                INSERT INTO transactions (user_id, transaction_type, amount, balance_after)
                VALUES (?, ?, ?, ?)
            ''', (user_id, 'DEPOSIT', deposit, deposit))
            
            self.conn.commit()
            
            print("\n" + "="*50)
            print("REGISTRATION SUCCESSFUL!")
            print("="*50)
            print(f"Account Number: {account_number}")
            print(f"Initial Balance: ₦{deposit:,.2f}")
            print("\nPlease log in to continue.")
            time.sleep(2)
            
            return True
        except sqlite3.Error as e:
            print(f"Error: Registration failed. {e}")
            self.conn.rollback()
            return False
    
    def login(self):
        """Login user"""
        print("\n" + "="*50)
        print("USER LOGIN")
        print("="*50)
        
        username = input("\nEnter username: ").strip()
       
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            print("Error: Invalid username format.")
            time.sleep(1)
            return False
        
        password = getpass.getpass("Enter password: ")
    
        if not password or password.strip() == '':
            print("Error: Password cannot be blank.")
            time.sleep(1)
            return False
        
        hashed_password = self.hash_password(password)
        
        self.cursor.execute('''
            SELECT id, full_name, account_number, balance 
            FROM users 
            WHERE username = ? AND password = ?
        ''', (username, hashed_password))
        
        user = self.cursor.fetchone()
        
        if user:
            self.current_user = {
                'id': user[0],
                'full_name': user[1],
                'username': username,
                'account_number': user[2],
                'balance': user[3]
            }
            print("\n" + "="*50)
            print("LOGIN SUCCESSFUL!")
            print("="*50)
            print(f"Welcome back, {self.current_user['full_name']}!")
            time.sleep(2)
            return True
        else:
            print("Error: Invalid username or password.")
            time.sleep(1)
            return False
    
    def deposit(self):
        """Deposit money"""
        print("\n" + "="*50)
        print("DEPOSIT")
        print("="*50)
        
        amount_str = input("\nEnter amount to deposit: ₦").strip()
        valid, msg, amount = self.validate_amount(amount_str)
        
        if not valid:
            print(f"Error: {msg}")
            time.sleep(1)
            return
        
        try:
            new_balance = self.current_user['balance'] + amount
            
            self.cursor.execute('''
                UPDATE users SET balance = ? WHERE id = ?
            ''', (new_balance, self.current_user['id']))
            
            self.cursor.execute('''
                INSERT INTO transactions (user_id, transaction_type, amount, balance_after)
                VALUES (?, ?, ?, ?)
            ''', (self.current_user['id'], 'DEPOSIT', amount, new_balance))
            
            self.conn.commit()
            self.current_user['balance'] = new_balance
            
            print("\n" + "="*50)
            print("DEPOSIT SUCCESSFUL!")
            print("="*50)
            print(f"Amount Deposited: ₦{amount:,.2f}")
            print(f"New Balance: ₦{new_balance:,.2f}")
            time.sleep(2)
        except sqlite3.Error as e:
            print(f"Error: Transaction failed. {e}")
            self.conn.rollback()
            time.sleep(1)
    
    def withdraw(self):
        """Withdraw money"""
        print("\n" + "="*50)
        print("WITHDRAWAL")
        print("="*50)
        print(f"Current Balance: ₦{self.current_user['balance']:,.2f}")
        
        amount_str = input("\nEnter amount to withdraw: ₦").strip()
        valid, msg, amount = self.validate_amount(amount_str)
        
        if not valid:
            print(f"Error: {msg}")
            time.sleep(1)
            return
        
        if amount > self.current_user['balance']:
            print("Error: Insufficient funds.")
            time.sleep(1)
            return
        
        try:
            new_balance = self.current_user['balance'] - amount
            
            self.cursor.execute('''
                UPDATE users SET balance = ? WHERE id = ?
            ''', (new_balance, self.current_user['id']))
            
            self.cursor.execute('''
                INSERT INTO transactions (user_id, transaction_type, amount, balance_after)
                VALUES (?, ?, ?, ?)
            ''', (self.current_user['id'], 'WITHDRAWAL', amount, new_balance))
            
            self.conn.commit()
            self.current_user['balance'] = new_balance
            
            print("\n" + "="*50)
            print("WITHDRAWAL SUCCESSFUL!")
            print("="*50)
            print(f"Amount Withdrawn: ₦{amount:,.2f}")
            print(f"New Balance: ₦{new_balance:,.2f}")
            time.sleep(2)
        except sqlite3.Error as e:
            print(f"Error: Transaction failed. {e}")
            self.conn.rollback()
            time.sleep(1)
    
    def check_balance(self):
        """Display current balance"""
        # Refresh balance from database
        self.cursor.execute('SELECT balance FROM users WHERE id = ?', (self.current_user['id'],))
        balance = self.cursor.fetchone()[0]
        self.current_user['balance'] = balance
        
        print("\n" + "="*50)
        print("BALANCE INQUIRY")
        print("="*50)
        print(f"Account Number: {self.current_user['account_number']}")
        print(f"Current Balance: ₦{balance:,.2f}")
        time.sleep(2)
    
    def transaction_history(self):
        """Display transaction history"""
        print("\n" + "="*50)
        print("TRANSACTION HISTORY")
        print("="*50)
        
        self.cursor.execute('''
            SELECT transaction_type, amount, recipient_account, balance_after, timestamp
            FROM transactions
            WHERE user_id = ?
            ORDER BY timestamp DESC
        ''', (self.current_user['id'],))
        
        transactions = self.cursor.fetchall()
        
        if not transactions:
            print("\nNo transactions found.")
        else:
            print(f"\nTotal Transactions: {len(transactions)}\n")
            for txn in transactions:
                txn_type, amount, recipient, balance_after, timestamp = txn
                print("-" * 50)
                print(f"Type: {txn_type}")
                print(f"Amount: ₦{amount:,.2f}")
                if recipient:
                    print(f"Recipient Account: {recipient}")
                print(f"Balance After: ₦{balance_after:,.2f}")
                print(f"Date: {timestamp}")
        
        time.sleep(3)
    
    def transfer(self):
        """Transfer money to another account"""
        print("\n" + "="*50)
        print("TRANSFER FUNDS")
        print("="*50)
        print(f"Current Balance: ₦{self.current_user['balance']:,.2f}")
        
        # Validate recipient account number
        recipient_account = input("\nEnter recipient account number: ").strip()
        
        if not recipient_account.isdigit() or len(recipient_account) != 8:
            print("Error: Invalid account number format.")
            time.sleep(1)
            return
        
        if recipient_account == self.current_user['account_number']:
            print("Error: Cannot transfer to your own account.")
            time.sleep(1)
            return
        
        self.cursor.execute('SELECT id, full_name FROM users WHERE account_number = ?', (recipient_account,))
        recipient = self.cursor.fetchone()
        
        if not recipient:
            print("Error: Recipient account not found.")
            time.sleep(1)
            return
        
        recipient_id, recipient_name = recipient
        print(f"Recipient: {recipient_name}")
        
        # Validate transfer amount
        amount_str = input("Enter amount to transfer: ₦").strip()
        valid, msg, amount = self.validate_amount(amount_str)
        
        if not valid:
            print(f"Error: {msg}")
            time.sleep(1)
            return
        
        if amount > self.current_user['balance']:
            print("Error: Insufficient funds.")
            time.sleep(1)
            return
       
        confirm = input(f"\nTransfer ₦{amount:,.2f} to {recipient_name}? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Transfer cancelled.")
            time.sleep(1)
            return
        
        try:
            new_sender_balance = self.current_user['balance'] - amount
            self.cursor.execute('UPDATE users SET balance = ? WHERE id = ?', 
                              (new_sender_balance, self.current_user['id']))
            
            self.cursor.execute('SELECT balance FROM users WHERE id = ?', (recipient_id,))
            recipient_balance = self.cursor.fetchone()[0]
            new_recipient_balance = recipient_balance + amount
            self.cursor.execute('UPDATE users SET balance = ? WHERE id = ?', 
                              (new_recipient_balance, recipient_id))
            
            self.cursor.execute('''
                INSERT INTO transactions (user_id, transaction_type, amount, recipient_account, balance_after)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.current_user['id'], 'TRANSFER_OUT', amount, recipient_account, new_sender_balance))
            
            self.cursor.execute('''
                INSERT INTO transactions (user_id, transaction_type, amount, recipient_account, balance_after)
                VALUES (?, ?, ?, ?, ?)
            ''', (recipient_id, 'TRANSFER_IN', amount, self.current_user['account_number'], new_recipient_balance))
            
            self.conn.commit()
            self.current_user['balance'] = new_sender_balance
            
            print("\n" + "="*50)
            print("TRANSFER SUCCESSFUL!")
            print("="*50)
            print(f"Amount Transferred: ₦{amount:,.2f}")
            print(f"Recipient: {recipient_name}")
            print(f"New Balance: ₦{new_sender_balance:,.2f}")
            time.sleep(2)
        except sqlite3.Error as e:
            print(f"Error: Transfer failed. {e}")
            self.conn.rollback()
            time.sleep(1)
    
    def account_details(self):
        """Display account details"""
        print("\n" + "="*50)
        print("ACCOUNT DETAILS")
        print("="*50)
        print(f"Full Name: {self.current_user['full_name']}")
        print(f"Username: {self.current_user['username']}")
        print(f"Account Number: {self.current_user['account_number']}")
        print(f"Current Balance: ₦{self.current_user['balance']:,.2f}")
        time.sleep(2)
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Transfer Funds")
        print("6. Account Details")
        print("7. Logout")
        print("="*50)
    
    def run(self):
        """Main application loop"""
        print("\n" + "="*50)
        print("WELCOME TO PYTHON BANKING APP")
        print("="*50)
        
        while True:
            if not self.current_user:
                print("\n1. Register")
                print("2. Login")
                print("3. Exit")
                
                choice = input("\nEnter your choice: ").strip()
                
                if choice == '1':
                    if self.register():
                        self.login()
                elif choice == '2':
                    self.login()
                elif choice == '3':
                    print("\nThank you for using Python Banking App!")
                    self.conn.close()
                    break
                else:
                    print("Invalid choice. Please try again.")
                    time.sleep(1)
            else:
                self.show_menu()
                choice = input("\nEnter your choice: ").strip()
                
                if choice == '1':
                    self.deposit()
                elif choice == '2':
                    self.withdraw()
                elif choice == '3':
                    self.check_balance()
                elif choice == '4':
                    self.transaction_history()
                elif choice == '5':
                    self.transfer()
                elif choice == '6':
                    self.account_details()
                elif choice == '7':
                    print(f"\nGoodbye, {self.current_user['full_name']}!")
                    self.current_user = None
                    time.sleep(1)
                else:
                    print("Invalid choice. Please try again.")
                    time.sleep(1)

if __name__ == "__main__":
    app = BankingApp()
    app.run()









