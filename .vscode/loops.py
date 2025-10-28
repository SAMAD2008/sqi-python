# program that accepts an input four times
x = 1
while x <= 4:
      input("Enter a word: ")
      x += 1

#multiplication table 15
i = 1
while i <= 12:
      print(f"15 * {i} = {i * 15}")      
      i += 1

#all numbers between 1 and 200 divisible by 3
a = 1
while a <= 200:
      if a % 3 == 0:
            print(a)
      a += 1          

#program that calculates sum of all odd numbers between 1 and 490
j = 1
total = 0
while j <= 490:
        if j % 2 != 0:
            total += j
        j += 1


print(total)        
        
    


