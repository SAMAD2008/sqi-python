favorites = ()
fav1 = input('Enter fav1: ')
fav2 = input('Enter fav2: ')
list_fav = list(favorites)
list_fav.append(fav1)
list_fav.append(fav2)
favorites = tuple(list_fav)
print(favorites)

dimensions = 10, 20, 30
length, width, height = dimensions
print(length)
print(width)
print(height)


info = ("product123", ("Electronics", 299.9), (20, 5, 2022))
product_ID, (category, price), (day, month, year) = info
print(f"The product belongs to {category} category and was manufactured in year {year}")


# gradient of a line
point1 = (43, 82)
point2 = (8, 80)

line = ((4, 9), (8, 15))
(x1, y1), (x2, y2) = line
gradient = (y2 - y1) / (x2 - x1)
print(f"The gradient of {line} is {gradient}")

numbers = [33, 4, 34, 23, 45, 34, 45, 3, 34]
print(sum(numbers))
print(min(numbers))
print(max(numbers))
avg = sum(numbers) / len(numbers)
print(f"The average of {numbers} is : {avg}")





