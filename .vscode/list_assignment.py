# Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
fruits = ['apple', 'banana', 'orange']
print(fruits[0])

# Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing
colors = ['red', 'green', 'blue']
print(colors[-1])

# Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7 (inclusive of index 3, exclusive of 8)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:8])

# Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' 'r' 's' 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(alphabets[-3:])

# Create a list called ages with items 20, 30, 40. Change the value of the second item to 35
ages = [20, 30, 40]
ages[1] = 35
print(ages)

# Create a list called grades with items "A", "B", "C", "D". Replace the items from index 1 (inclusive) to index 3 (exclusive) with "X"
grades = ['A', 'B', 'C', 'D']
grades[1] = 'X'
grades[2] = 'X'
print(grades)

# Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list
cities = ['New York', 'London', 'Paris']
cities.insert(0, 'Tokyo')
print(cities)

# Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list
fruits2 = ['apple', 'banana', 'cherry']
print(len(fruits2))

# Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list
prices = [10.5, 20.0, 15.75]
print(type(prices))

# Create a list called mixed with items 10, "apple", True. Print the list
mixed = [10, "apple", True]
print(mixed)    

# Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list
books = ['Python', 'Java']
books.append('Javascript')
print(books)

# Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1
names = ['Alice', 'Bob', 'Eve']
names.insert(1, 'Charlie')
print(names)

# Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)

# Create a list called colors with items "red", "green", "blue". Remove "green" from the list
colors2 = ['red', 'green', 'blue']
colors2.remove('green')
print(colors2)
