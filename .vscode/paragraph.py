# Write a program that takes a paragraph of a text from a user. Then tell them the total word count, and also tell them the number of unique words in that paragraph
text = input("Please enter a paragraph of text: ")
words = text.lower().split()
total_word_count = len(words)
unique_words = set(words)
unique_word_count = len(unique_words)
print(f"The total number of words in {text} are: {total_word_count}")
print(f"The number of unique words are: {unique_word_count}")

