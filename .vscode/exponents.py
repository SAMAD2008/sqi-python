# crate a text file caled numbers_with_exponents and inside it, youre going to insert the result of numbers between 1-100 and their squares, and their cubes

with open('numbers_with_exponents.txt', 'w') as file:

    for i in range(1, 101):
       file.write(f"{i}, {i ** 2}, {i ** 3}\n")
       



       
       