#WAP to print the square of x using scope and return function

def main (): #intended line 4th and 5th belongs to main ()
    x = int(input("x= "))
    print ("x sqaured is", square(x)) #it will call the square () and pass the value of x to it

def square (n): #n is a param of this new function. n has local inside the sqaure ()
    return n*n #if x=2; 2*2=4. Also, we can use "return n**2" or "return pow (n,2)"

main()