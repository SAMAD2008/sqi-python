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
import random
import getpass
import re
import time
import hashlib
import sys
from datetime import datetime
