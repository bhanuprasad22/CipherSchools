# -*- coding: utf-8 -*-
"""Lecture 14 - Functions, Lambda Expressions, And Error Handling

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11E1oSTqwhSU3zqhyNriwuhsg4d83yyta
"""

#Simple Function
def add_numbers(a,b):
  return a + b

print(add_numbers(1,2))

def square(a):
  return a**2

a = int(input("Enter the value of a: "))
c = (square(a))
print("c = ", c)

#Function with default arguments

def greet(name,message = "Hello"):
  return f"{message},{name}!"

print(greet("Bob"))
print(greet("Alice","Hi"))

#Function with Variable-Length arguments

def sum_all(*args):
  return sum(args)

print(sum_all(1,2,3,4,5))

#Function with keyword arguments

def display_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} : {value}")

display_info(name = "John", age = 30, city = "New York")

#High order Function

def apply_function(func,x,y):
  return func(x,y)

def multiply(x,y):
  return x * y

print(apply_function(multiply,6,7))

"""# Lambda Expressions

defination: Also known as anonymous functions, are small, unnamed functions defined using the lambda keyword.They are often used for short, throw away functions.
"""

#Simple lambda function

square = lambda x: x**2

print(square(5))

#Lambda function in 'map'

numbers = [1,2,3,4,5]
squares = list(map(lambda x: x * x, numbers))

print(squares)

# Lambda function with 'Filter'

numbers = [1,2,3,4,5,6]
even_numbers = list(filter(lambda x: x % 2 == 0,numbers ))

print(even_numbers)

# Lambda function in 'sorted'

students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key = lambda student: student[1])

print(sorted_students)

"""# Error Handling

Definition: try,except,else and finally blocks. It allows you to handle exceptions gracefully and ensure that the program continues to run.
"""

try:
  result = 10/0

except ZeroDivisionError:
  print("Error: Division by zero!")

#Try-Except-Else Block

try:
  result = 10/2
except ZeroDivisionError:
  print("Division by Zero not possible!")
else:
  print("Result: ", result)

#Try-Except-Else-Finally Block

try:
  result = 10 /2
except ZeroDivisionError:
  print("Division by Zero not possible!")
else:
  print("Result: ", result)
finally:
  print("Finally block executed")

#Handling multiple Exceptions

try:
  n = int(input("Enter a number: "))
  result = 10/n

except ZeroDivisionError:
  print("Number cannot be divided by zero")

except ValueError:
  print("Invalid input! Please enter a number")

finally:
  print(result)

#Raising Exceptions

def check_positive(number):
  if number <= 0:
    raise ValueError("Number must be positive")
  else:
    print(number)

try:
  check_positive(-5)
except ValueError as e:
  print(e)