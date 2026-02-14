len(str(12345))
# len() doesn't work with integers, so you must convert the number to a string first

print(type("Gia Bao"))
print(type(True))
print(type(21.36))
print(type(67))

name = input("Enter your name here: ")
name_length = len(name)
print(f'Number of letter in your name: {name_length}')
