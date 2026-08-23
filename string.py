#title mcapitalize the first letter of every word in a str
name = input ("What's ya name? ")
name = name.strip()
name = name.title() #capitalize works only on the first word of the str and not on every word
print (f"Hello, {name}")
