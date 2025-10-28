# Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables length, width, and height, and print each variable
dimensions = 10, 20, 30
length, width, height = dimensions
print(length)
print(width)
print(height)

# Given the tuple coordinates:
#coordinates = (1.5, 2.5, 3.5)
#Unpack the tuple into variables x, y, and z, and print the value of y.
coordinates = (1.5, 2.5, 3.5)
x, y, z = coordinates
print(y)

# Create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession, and print the value of profession
person = ("John", 25, "Engineer")
name, age, profession = person
print(profession)


# Given the nested tuple data:
#data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
#Unpack the first element of data into variables student1 and student2, and print student2.
data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
(student1, student2), (subject1, subject2), (score1, score2) = data
print(student2)

# Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2, and print both variables
colors = ("red", "green", "blue", "yellow")
color1, color2, *others = colors
print(color1)
print(color2)

# Given the tuple record:
#record = ("Jane", (32, "Manager"), ["HR", "Finance"])
#Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
record = ("Jane", (32, "Manager"), ["HR", "Finance"])
name, (age, position), departments = record
print(age)
print(departments[0])

# Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable
triplet = ("one", "two", "three")
first, second, third = triplet
print(second)

# Given the tuple info:
#info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
#Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year
info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
product_ID, (category, price), (day, month, year) = info
print(category)
print(year)
print(f"The product belongs to {category} category and was manufactured in year {year}")

# Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). Unpack the nested tuples into individual variables and print the second value of the third tuple.
nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
(first1, second1), (first2, second2), (first3, second3) = nested_tuple
print(second3)
print(nested_tuple[2][1])  

# Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
#Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas
inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
(fruit1, qty1), (fruit2, qty2), (fruit3, qty3) = inventory
print(qty2)
print(f"The quantity of bananas is: {qty2}")