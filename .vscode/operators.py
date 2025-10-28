#brand = "Nike"
#vowels = "aeiou"
#brand_last = brand[-1]
#print(brand_last in vowels)


from getpass import getpass




#word = input("Enter your word: ").replace(" ", "")

#reversed_word = word[::-1]

#is_palindrome = word == reversed_word

#print(f"It is {is_palindrome} that {word} is a palindrome.")



print("********* PERSONAL INFORMATION *******")
fname = input ("First Name: ")
email = input ("Your Email: ")
password = getpass("Password: ")

print(f"""
      
 Your first name is {fname}
 And your email is {email}


 And your password is {password}    


""")