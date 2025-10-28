
# Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
robot_grid = [
    ["R2", ["battery", [98]]],
    ["R5", ["status", "active"]],
    ["X1", [["joint", "loose"], "error"]]
]
print(robot_grid[2][1][0][1][1] * 2)
print(robot_grid[0][1][1][0])

# Get the Five in the Jazz song title and Get the duration of the Jazz song
playlist = [
    ["Jazz", ["Take Five", 5.24]],
    ["Pop", ["Blinding Lights", 3.20]],
    ["Rock", ["Bohemian Rhapsody", 5.55]]
]
print(playlist[0][1][0][5:])
print(playlist[0][1][1])

# Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
animals = [
    ["Elephant", ["Herbivore"]],
    ["Tiger", ["Carnivore"]],
    ["Frog", ["Amphibian"]]
]
print(animals[1][1][0][5])
print(animals[2][1][0][0])  



