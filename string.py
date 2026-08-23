#split breaks a string into a list of sub-strings

name = input ("What's ya name? ").strip().title() 
first, last = name.split(" ") #this will break the whole name into first and last name on the basis of space
print (f"Hello, {first}") #use first or last as a var based on the requirements
