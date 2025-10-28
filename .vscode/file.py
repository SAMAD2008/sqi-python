file = open('project.txt')
vowel = 'aeiou'
num_of_vowel = 0
num_of_words = 0
words = file.read().split()
for word in words:
    if word[0] in vowel:
     num_of_vowel += 1
    if len(word) >= 5:
        num_of_words += 1

print(num_of_vowel)        
print(num_of_words)


