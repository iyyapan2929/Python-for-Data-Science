# Print numbers from 1 to 10

for x in range(1, 11):
  print(x)

# Print numbers from 10 to 1 in reverse order

for x in range(10, 0, -1):
    print(x)  

# Print all odd numbers between 1 and 50

for x in range(1, 50, 2):
  print(x)

# print all even numbers between 1 and 50

for x in range(2, 50, 2):
  print(x)

# Print the multiplication table of a number entered by the user

a = int(input("enter number : "))
for i in range(1, 11):
  print(a, "x", i, "=", a*i)

# Calculate the sum of numbers from 1 to 100.

total = 0

for i in range(1, 101):
    total += i

print(total)

# calculate the sum of all even numbers between 1 and 100

total = 0

for i in range(2, 101, 2):
  total += i
print(total)

# Factorial number

number = int(input("enter number : "))
factorial = 1
for i in range(1, number + 1):
  factorial  *= i

print(factorial)

# Fibonacci number

a = 0
b = 1
for i in range(0, 10):
  c = a + b
  a = b
  b = c

  print(c)

# Multiplication tables

a = int(input("Enter number : "))
for i in range(1, 11):
  print(a, "x", i, "=", a*i)

# Count down 

for i in range(10, 0, -1):
  print(i)
  
print("Happy Birthday")

# Sum of 1 to 10


total = 0

array = [2, 3, 4, 9, 33, 45, 66, -3, -5]
print(sum(array))

for i in range(len(array)): # for i in range(0, 9):
    total += array[i]
    
print(total)


sum = 0
for num in array:
  sum += num
print(sum)

array = [2, 3, 4, 9, 33, 45, 66]
x = 33

for num in array:
  if x == num:
    print(array.index(x))
else:
  print("invalid")
  
