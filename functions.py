# Writing your own functions (defining functions)
# built in functions are print() and round()
# def = define
# function name is greet = use lowercase when naming functions and _ if multiple words

# def greet(first_name, last_name):
#     print('Hi there')
#     print('Welcome aboard')


# greet('James', 'Ivy') # this is how you call a function


# Arguments

##########################################
# a parameter is an input you define for your function
# difference b/w greet() and print() is print() takes an input and greet does not.
# we have to pass a values when calling functions such as arguments(is the actual value for a given parameter)

# def greet(first_name, last_name):  # parameters
#     print(f"Hi {first_name} {last_name}")
#     print('Welcome aboard')


# greet('James', 'Ivy')  # arguments to the greet() function(passing values)
# greet('James', 'Smith') # we are reusing the function here, we are just calling it again. functions are reusable

# Types of Functions
#####################################

# functions either:
# 1- perform a task - see greet() and print()
# 2- return a value - see round(1.9) - calculate and return a value

# performing a task
# locked to print something in a terminal
# def greet(name):
#     print(f'Hi{name}')


# # returning a value with function
# # this function is not tied to printing something in the terminal
# def get_greeting(name):
#     return f"Hi, {name}"  # return a value from this function


# # bc it returns a value we are able to assign it to the variable message
# # we can print it to the terminal or we can use built in open and write message to file, or send it in an email
# message = get_greeting("James")


# Keyword Arguments
##########################################

def increment(number, by):
    return number + by

print(increment(2, by=10)) # including by makes it easier to understand if someone else is reading our code

# Default Arguments p5
##########################################
