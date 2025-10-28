text = input("Enter a text: ")
phrase_word = text[-4:].replace(' ', '').lower()
palindrome = phrase_word[::-1]
if phrase_word == palindrome:
    print(f"last four characters of {text} is a palindrome")
else:
    print(f"last four characters of {text} is not a palindrome")
    
primary_colors = {'red', 'blue', 'yellow'}
colors = set(input("Enter three primary colors: ").split(', '))
if colors == primary_colors:
    print('All are primary colors')
else:
    print('Not all primary colors')    





