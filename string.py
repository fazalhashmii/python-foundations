#writing two str funcs together in short

#method 1
name = input ("What's ya name? ")
name = name.strip().title() 
print (f"Hello, {name}")

#method 2
name = input ("What's ya name? ").strip().title() 
print (f"Hello, {name}")