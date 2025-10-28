# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]
squares = []
for num in digits:
    squares.append(num ** 2)
print(squares)


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]
# names_with_a = []
# for name in names:
#     if 'a' in name:
#         names_with_a.append(name)
# print(names_with_a)

names_with_a = [name for name in names if 'a' in name]
print(names_with_a)

# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
values = [5, 12, 3, 18, 7]
greater_than_10 = []
for value in values:
    greater_than_10.append(value > 10)
print(greater_than_10)


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
animals = ["dog", "cat", "lion", "tiger"]
last_characters = []
for animal in animals:
    last_characters.append(animal[-1])
print(last_characters)

# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
# values = [5, 12, 3, 18, 7]
# for value in values:
#     if all(value > 10):
        


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
names = ["John", "Sara", "Mike", "Amanda"]
any_name_with_a = False
for name in names:
    if 'a' in name:
        any_name_with_a = True
        break
print(any_name_with_a)

# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False


# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
words = ["apple", "zebra", "mango", "lemon"]
any_starts_with_z = False
for word in words:
    if word.lower().startswith('z'):
        any_starts_with_z = True
        break
print(any_starts_with_z)

# 9. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
any_org_email = False
for email in emails:
    if '.org' in email:
        any_org_email = True
        break
print(any_org_email)

# 10. Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True
values = [1, 3, 5, 7, 9]
all_odd = True
for value in values:
    if value % 2 == 0:
        all_odd = False
        break
print(all_odd)

# 11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
words = ["hi", "dog", "go", "sun"]
all_longer_than_2 = True
for word in words:
    if len(word) <= 2:
        all_longer_than_2 = False
        break
print(all_longer_than_2)

# 16. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True
numbers = [5, 4, 3, 3, 8]
any_less_than_0 = False
for number in numbers:
    if number < 0:
        any_less_than_0 = True
        break
print(any_less_than_0)

# 17. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
items = ["sky", "tree", "rock", "stone"]
words_with_e = []
for item in items:                      
    if 'e' in item or 'E' in item:
        words_with_e.append(item)                                               
print(words_with_e)

# 18. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
names = ["Alice", "Bob", "charlie", "David"]
all_start_with_uppercase = True
for name in names:
    if not name[0].isupper():
        all_start_with_uppercase = False
        break
print(all_start_with_uppercase)

# 19. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True
sentences = ["Short one", "This is a much longer sentence", "Okay"]
any_longer_than_20 = False
for sentence in sentences:
    if len(sentence) > 20:
        any_longer_than_20 = True
        break
print(any_longer_than_20)










