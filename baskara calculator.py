"""
im going to try to do a baskara calculator without knowing how to do it previously
all the ideias and codes in this project are made by myself. NO INTERNET LOOKING.
"""

# Printing the message to the user, so he can use it properly
print("This is a baskara calculator, please DO NOT put any decimal numbers! thx")

# Asking the user for the values of the variables
a = int(input("what is the value of a? "))
b = int(input("what is the value of b? "))
c = int(input("what is the value of c? "))

# Doing variables for the equations to discover the response
bhaskara0 = (b * b -4 * a * c)
bhaskara1 = (-b + bhaskara0 **1// 2)
bhaskara2 = (-b - bhaskara0 **1// 2)


# functions for x1 and x2
def x1():
     print("Your first X is: ", bhaskara1)

def x2():

    print("Your second X is: ", bhaskara2)

error = "There is not an answer :( "


# Defining a function to give the answer to the user
def answer():

    if bhaskara0 >= 0:
        x1()
        x2()

    else:
        print(error)

# Calling the function
answer()