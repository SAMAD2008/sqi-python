
# file = open('words.txt')

# content = file.read().split()

# print(len(content))


# print(dir(file))

# print(file.read())

# print('************ READING LINE *************')
# print(file.readline())
# print(file.readline())


# print('************* READING LINES *************')
# print(file.readlines())
# Write
# append
# Read



# Create a file called paragraphs_of_text.txt and write a very long text inside it. Then create a python file called file_reader.py. Open that paragraph_of_text.txt and find out HOW MANY WORDS are there in that file.


# file = open('words.txt')

# content = file.read().split()

# print(len(content))





# file = open('words.txt')

# for line in file.readlines():
#     print(line)



# Get the student data from student_data.txt and display them in tabular format

# file = open('student_data.txt')
# print(f"Name\t\t\tMatric\t\t\tCourse")

# for line in file.readlines():
#     # print(line)
#     name, matric, course = line.split(',')

#     print(f"{name}\t\t{matric}\t\t\t{course}")


# From that file, find out how many words start with a vowel


# file = open('words.txt', 'r+')

# file.write("Wrote first linex\n")
# file.write("Wrote second linex\n")
# file.write("Wrote third linex\n")

# print(file.readlines())





# # context manager

# with open('words.txt') as myfile:
#     print(myfile.read())



# A program that asks a teacher to provide the names, scores, and subjects of their students and then store all these details into a file called scores.txt


# with open('scores.txt', 'w') as file:

#     for i in range(4):
#         name = input('Enter student name: ')
#         subject = input('Enter student subject: ') 
#         score = input('Enter student score: ') 

#         file.write(f"{name},{subject},{score}\n")


# with open('pins_log.txt', 'w') as file:

#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 for m in range(10):
#                     file.write(f"{i}{j}{k}{m}\n")



# Create a text file called numbers_with_exponents.txt and inside it, you're going to insert the result of numbers between 1-100 and their squares, and their cubes
