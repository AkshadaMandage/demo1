#a)
x = 5
if x > 0:
	print("x is positive")
elif x < 0:
	print("x is negative")
else:
    print("x is zero")
    
#b)
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
	print(fruit)
	
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
           if fruit == "banana":
           	break
           print(fruit)
           
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
         if fruit == "banana":
         	continue
         print(fruit)
         
 #c) 
i = 0

while i < 5:

    print(i)

    i += 1
    
def add_numbers(x, y):
	return x + y
result = add_numbers(3, 5)
print(result)

def add_numbers(x, y):

      result = x + y

      return result
sum = add_numbers(5, 7)

print(sum)

#d)
def greet(name, greeting="Hello"):

       print(greeting + ", " + name + "!")
greet("Alice")
#e)
from builtins import *

def calculate_average(*numbers):

      total = sum(numbers)

      count = len(numbers)

      average = total / count

      return average

result = calculate_average(2, 4, 6, 8)

print(result)
#f)
def get_name_and_age():

     name = "Alice"

     age = 30

     return name, age
name, age = get_name_and_age()

print(name) 
print(age)

# output
#x is positive
#apple
#banana
#cherry
#apple
#apple
#cherry
#0
#1
#2
#3
#4
#8
#12
#Hello, Alice!
#5.0
#Alice
#30
