# def is used to define (create) a function.

# program 1: no def used for hello; thus we shall see the error when the program is executed



# program 2: creating a hello function to perform the program 1 correctly

def hello(): # ":" tells python that the function’s code block starts here
    print ("Hello") # this belongs to the defined function

name = input ("What is your name? ")
hello ()
print (name)