countries = ['nigeria', 'belgium', 'benin', 'laos', 'ghana', 'ethiopia']
# vowels = 'aeiou'
# for country in countries:
#     if country[1] not in vowels:
#         print('There is a country whose second letter is not a vowel')
#         break
# countries_with_vowel_last = []
# for country in countries:
#     if country[-1] in 'aeiou':
#         countries_with_vowel_last.append(country)

# print(countries_with_vowel_last)  

# uppercase_countries = []
# for country in countries:
#     uppercase_countries.append(country.upper())

# print(uppercase_countries)    

# numbers = [2, 5, 2, 28, 68, 28, 19, 25, 35, 29, 40, 82]
# muliple_of_5 = []
# for number in numbers:
#     if number % 5 == 0:
#         muliple_of_5.append(number)
# print(muliple_of_5)        

name = 'ouwatobi'

list_of_letters = []

for ch in name:
    list_of_letters.append(ch.isupper())

if any(list_of_letters):
    print('There is at least a letter in uppercase')
else:
    print('There is none in uppercase')        