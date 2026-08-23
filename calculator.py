#we will cover 3 programs which will highlight the basic arithmetic operations, common mistake and finally a useful calculator

#program 1 - simple calculation
x = 1
y = 2
z = x + y
print (z) #output = 3. simple

#program 2 - common mistake
x = input ("x= ")
y = input ("y= ")

z = x + y #if x=1.y=2 then the output will be 12 and not 3 because input() always returns a string, so + joins "1" and "2" as "12" instead of adding them as numbers.
print(z) 

#program 3 - calculator
x = input ("x= ")
y = input ("y= ")

z = int(x) + int(y) #if x=1, y=2 then the output will be 3 because int() converts the input strings "1" and "2" into numbers 1 and 2, so + performs addition and gives 3.
print (z)

#method 2 of writing program 3 using function nesting
x = int(input("x= ")) #similar to maths where we solve the innermost parenthesis first and then the outermost one. Python will first execute the input func and then convert the str into int when the int func is executed
y = int(input("y= "))
print (x+y)
