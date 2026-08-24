#round off to second digit

#method 1
x = float(input("x= "))
y = float(input("y= "))
z = round (x/y,2) #round(number, ndigits) > number: the number you want to round > ndigits: how many decimal places you want.
print (z)

#method 2
x = float(input("x= "))
y = float(input("y= "))
z = x/y
print (f"{z:.2f}") # ".2f" display z as a floating-point number with 2 decimal places.
