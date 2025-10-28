person = ['Tobi', 'Dada', 23, 'Lagos', 2025]

person_dict = {
        'firstname': 'Tobi',
        'lastname': 'Dada',
        'age': 23,
        'city': 'Lagos',
        'graduation_year' : 2025
}

print(person_dict)
print(person_dict['firstname'])
print(person_dict['graduation_year'])
print(f"{person_dict['firstname']} {person_dict['lastname']}")

print(person_dict.setdefault('country', 'Nigeria'))
print(person_dict)



