#number formatting using commas

#method 1
x = float(input("x= "))
y = float(input("y= "))
z = round(x+y)
print (f"{z:,}") # ":" applies a formatting rule to z and "," adds commas as thousands separators

#method 2
x = float(input("x= "))
y = float(input("y= "))
print (f"{round(x+y):,}")

# Think of it like this: 
# f"{variable:format}"
# {z} puts the value of z
# : start formatting instructions
# , format the numbner with commas
# f"{z:,}" = Put z here, and display it with commas