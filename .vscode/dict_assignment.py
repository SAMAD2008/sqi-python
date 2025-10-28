# Access and print the name of the teacher of "class2".school = {
#    "class1": {
#        "students": ["Alice", "Bob"],
#       "teacher": "Mr. Smith"
#    },
#    "class2": {
#        "students": ["Charlie", "David"],
#        "teacher": "Ms. Johnson"
#    }
# }
school = {
    "class1": {"students": ["Alice", "Bob"], "teacher": "Mr. Smith"},
    "class2": {"students": ["Charlie", "David"], "teacher": "Ms. Johnson"},
}
print(school["class2"]["teacher"])

# Access and print the second employee in the "Engineering" department.company = {
#    "HR": ["Alice", "Bob"],
#    "Engineering": ["Charlie", "David"]
# }
company = {"HR": ["Alice", "Bob"], "Engineering": ["Charlie", "David"]}
print(company["Engineering"][1])

# Access and print the name of the second assistant.
# university = {
#    "faculty": {
#        "professors": ["Dr. Smith", "Dr. Brown"],
#        "assistants": ["Ms. Green", "Mr. White"]
#    },
#    "students": ["John", "Jane", "Alice", "Bob"]
# }
university = {
    "faculty": {
        "professors": ["Dr. Smith", "Dr. Brown"],
        "assistants": ["Ms. Green", "Mr. White"],
    },
    "students": ["John", "Jane", "Alice", "Bob"],
}
print(university["faculty"]["assistants"][1])

# Access and print the price of the third fruit.	store = {
#    "fruits": [
#        {"name": "apple", "price": 0.5},
#        {"name": "banana", "price": 0.2},
#        {"name": "cherry", "price": 1.5
#     ],
#    "vegetables":
#         {"name": "carrot", "price": 0.3},
#        {"name": "lettuce", "price": 1.0},
#        {"name": "onion", "price": 0.4}
#    ]
# }
store = {
    "fruits": [
        {"name": "apple", "price": 0.5},
        {"name": "banana", "price": 0.2},
        {"name": "cherry", "price": 1.5},
    ],
    "vegetables": [
        {"name": "carrot", "price": 0.3},
        {"name": "lettuce", "price": 1.0},
        {"name": "onion", "price": 0.4},
    ],
}
print(store["fruits"][2]["price"])

# Access and print the second non-fiction book.	library = {
#    “fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
#    "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"]
# }
library = {
    "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
    "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"],
}
print(library["non-fiction"][1])

# Access and print the age of the first child.	family = {
#    "parents": ["John", "Jane"],
#    "children": [
#        {"name": "Tom", "age": 5},
#        {"name": "Lucy", "age": 8}
#    ]
# }
family = {
    "parents": ["John", "Jane"],
    "children": [{"name": "Tom", "age": 5}, {"name": "Lucy", "age": 8}],
}
print(family["children"][0]["age"])

# Access and print the name of the second main course.
restaurant = {
    "menu": {
        "appetizers": ["soup", "salad"],
        "main_courses": ["steak", "pasta"],
        "desserts": ["cake", "ice cream"],
    },
    "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"],
}
print(restaurant["menu"]["main_courses"][1])

# Access and print the department of the user of the first desk.
workspace = {
    "desks": [
        {"user": "Alice", "department": "HR"},
        {"user": "Bob", "department": "Engineering"},
    ],
    "equipment": {"computers": 20, "printers": 10},
}
print(workspace["desks"][0]["department"])

# Access and print the name of the second designer.
team = {
    "developers": ["Dev A", "Dev B"],
    "designers": ["Designer X", "Designer Y"],
    "projects": ["Project 1", "Project 2"],
}
print(team["designers"][1])

# Access and print the second international destination.
travel = {
    "domestic": ["Boston", "Chicago"],
    "international": ["Paris", "Tokyo"],
    "expenses": {"flights": 1500, "hotels": 2000},
}
print(travel["international"][1])
