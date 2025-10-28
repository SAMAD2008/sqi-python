sentence = "There is a very powerful language called Python"

# 1. Print that sentence all in upper case
sentence = "There is a very powerful language called Python"
print(sentence.upper())

# 2. Print the first letter of that sentence concatenated with the second and the last letter
print(sentence[0] + sentence[1] + sentence[-1])

# 3. Turn last letter to uppercase
print(sentence[:-1] + sentence[-1].upper())


# 4. Extract and display only the word "very"
print(sentence.split()[3])

# 5. Extract "Python" in uppercase
print(sentence.split()[-1].upper()) 

# 6. Display 4th to 45th character
print(sentence[3:45])

# 7. If a string has 19 characters, index of last character?
str_example = "aB3xY9kLmN7pQrT2zVw"
print(str_example.find("w"))

# 8. Print the first 20 characters of the sentence in UPPER CASE and the remaining characters in lower case.
print(sentence[:20].upper() + sentence[20:].lower())

# 9. Replace every letter 'a' in the sentence with '*'.
print(sentence.replace("a", "*"))

# 10. Replace the word "powerful" with "*****".
print(sentence.replace("powerful", "*****"))

# 11. Display the sentence like this: "There Is A Very Powerful Language Called Python"
print(sentence.title())

# 12. Turn the sentence into a list of words.
print(sentence.split())

# 13. Turn the sentence into a list of UPPER CASE and also TITLED words.
words_upper = sentence.upper()
words_titled = sentence.title()
print(words_upper.split())
print(words_titled.split())

# 14. Have a variable remark = "The luck that guy has really sucks!!". Replace "luck" with "l***" and "sucks" with "s***s".
remark = "The luck that guy has really sucks!!"
print(remark.replace("luck", "l***").replace("sucks", "s***s"))

# 15. Have variables fm, years = 106.5, 26. Then use concatenation to print "Faaji FM with frequency 106.5 is 26 years old today"
fm, years = 106.5, 26
print("Faaji FM with frequency " + str(fm) + " is " + str(years) + " years old today")

# 16. Create variables num1, num2 = 70, 80. Then print 70 * 80 = 5600 using CONCATENATION. And on the next line use INTERPOLATION to do it.
num1, num2 = 70, 80
print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
print(f"{num1} * {num2} = {num1 * num2}")
















































































































































































