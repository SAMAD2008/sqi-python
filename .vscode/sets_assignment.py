# Create a set called fruits with values {"air", "water", "food"}. Check if "food" is in the set and print the result
fruits = {"air", "water", "food"}
print("food" in fruits)

# Create a set called colors with values {"red", "green", "blue"}. Add the color "yellow" to the set and print the updated set
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)

# Given the set animals = {"cat", "dog", "rabbit"}, add multiple items ["horse", "sheep"] to the set and print the updated set
animals = {"cat", "dog", "rabbit"}
animals.update(["horse", "sheep"])
print(animals)

# Create a set called countries with values {"USA", "Canada", "Mexico"}. Remove "Canada" from the set and print the updated set.
countries = {"USA", "Canada", "Mexico"}
countries.remove("Canada")
print(countries)

# Given the set cities = {"New York", "Los Angeles", "Chicago"}, remove "Houston" which is not in the set without raising an error.
cities = {"New York", "Los Angeles", "Chicago"}
cities.discard("Houston")
print(cities)

#Given the list seasons = ["Spring", "Summer", "Fall", "Winter", “Spring”], convert the list to a set to get rid of the duplicate `Spring`.
seasons = ["Spring", "Summer", "Fall", "Winter", "Spring"]
seasons_sets = set(seasons)
print(seasons_sets)

# Create two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}. Use the union method to join the sets and print the result.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_union = set1.union(set2)
print(set_union)

# Given two sets, setA = {"a", "b", "c"} and setB = {"c", "d", "e"}, find the intersection of the sets and print the result.
setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
set_intersection = setA.intersection(setB)
print(set_intersection)

# Create a set called prime_numbers with values {2, 3, 5, 7}. Add the number 11 to the set and print the updated set.
prime_numbers = {2, 3, 5, 7}
prime_numbers.add(11)
print(prime_numbers)

# Given the set odd_numbers = {1, 3, 5, 7, 9}, remove a random item from the set and print the updated set.
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers.pop()
print(odd_numbers)

# Create a set called vowels with values {"a", "e", "i", "o", "u"}. Empty the set and print the result.
vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(vowels)

# Given the set letters = {"a", "b", "c"}, find the difference between `letters` and another set {"b", "c", "d"}. Print the result. Afterwards, find the symmetric difference and print the result.
letters = {"a", "b", "c"}
other_set = {"b", "c", "d"}
difference = letters.difference(other_set)
print(difference)
symmetric_difference = letters.symmetric_difference(other_set)
print(symmetric_difference)





