# BASICS

#####################################################################
# What is an expression?
#  a piece of code that produces a value
# "*" * 3 = "***"

# What is a syntax error?
#  bad grammar in the code

# What does a linter do?
# check our code for bad grammar or syntax before the code is ran.


# PRIMITIVE TYPES = numbers, booleans, or strings

#################################################################################

# Variables - we use variables to store data into computers memory

students_count = 1000 # integer
rating = 4.99 # floating number
is_published = False # boolean - helps make decisions in our programs
course_name = "Python Programming"  # strings

message = """
Hi John,
This is a message.
"""

# functions are a reusable piece of code that carries out a task.

course_name = "Python Programming"
print(len(course_name))  # calling this functions

# ##string slicing

print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])


# Escape sequences or escape character

# \"" = double quote
# \' = single quote
# \\ = backslash
# \n = new line
# \t = tab

course = "Python \"Programming"
course_one = "Python \'Programming"
course_two = "Python \\Programming"
course_three = "Python \nProgramming"
course_four = "Python \tProgramming"
print(course)
print(course_one)
print(course_two)
print(course_three)
print(course_four)

# formatted strings

first = "James"
last = "Ivy"
# full = first + " " + last  #concat two strings
full = f"{len(first)} {2 + 2}"
full_one = f"{first} {last}"
print(full)
print(full_one)

# string method 

course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find('pro'))
print(course.replace('p', 'j'))


# Type Conversion 

x = input("x: ")
# print(type(x)) = return what type x is 
y = int(x) + 1
print(f"x: {x}, y: {y}")

# int(x) = integer 
# float(x) = float
# bool(x) = boolean
# str(x) = string

# Quiz 

# What are the primitive types in python?
# strings, numbers, booleans
# numbers = integers, floats, complex numbers

fruit = "Apple"
print(fruit[1])
# this expression will return second character which is p = index starts with 0. will print p!

# print(10 % 3) = 1
# % is a modulus operator and returns the remainder of a division

print(bool("False"))
