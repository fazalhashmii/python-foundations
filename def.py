#pass the default value if the programmer forgets to put the argument in the hello call function

def hello (x="null"): #null is the default value
    print("Hello,", x)

name = input ("What's your name? ")
hello () #no argument assigned
