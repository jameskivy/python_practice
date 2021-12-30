# Comparison Operators - are used to compare values

################################################################
# boolean express = True or False

# >   = greater than
# >=  = greater than or equal too
# <   = less than
# <=  = less than or equal too
# ==  = equals
# !=  = not equal

# "bag" > "apple" == True
# "bag" == "BAG" == False

# Conditional Statements = time to make a decision 
# you can have how many elif statements you want

# temperature = 32
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")

# print("Done")


# Ternary Operator 
#############################################

# age = 14
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

# print(message)

# refactored - same as above just a cleaner way
# age = 17
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)


# Logical Operators
# model more complex conditions
# logical operators are short-circuit meaning - checking one condition at a time 
# and = if both conditions are true the result will be true
# or = at least one condition is true the result will be true
# not = inverses the value of a boolean, result will be false

# high_income = False
# good_credit = True
# student = False

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not Eligible")


#chaining comparision operators 
# age should be b/w 18 and 65

# age = 10

# if 18 <= age < 65:
#     print("Eligible")
# if age < 18:
#     print("You are to young")


# For Loops
#########################################
# there are time we may want to repeat a task a number of times
# use loops to create repeation 

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")

# successful = True

# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")


# Nested for loops 
# a loop inside of another loop

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")


# Iterables 
########################################################
# print(type(10))
# print(type(range(5)))
#range is an example of complex types in regards to primitive types
# iterate - we can interate over it

# for x in "Python":
#     print(x)

name = input('What\'s your name? ')
uppercase = name.upper()
letters = len(name)

if name:
    print(f'HELLO, {uppercase}!')
    print(f'You have {letters} letters in your name. Dope!')




