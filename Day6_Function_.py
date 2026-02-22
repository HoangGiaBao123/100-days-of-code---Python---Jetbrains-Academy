# Function in Python
# There are 2 ways to write a function

# Method 1: Using 'return' in the function and call it by 'print()':
def greeting():
    return "Hello, my friend!"

print(greeting())   # If you write greeting(), the output wil be empty, but why?
                    # Because this function only has 'return' to return value, but you haven't print it

# Method 2: Using 'print()' in the function and call it by its name:
def bye():
    print('Goodbye, my friend!')

bye()   # If you write 'print(bye())' the output wil display 'None', but why?
        # Because this function doesn't have 'return' to return any value, so it returns 'None'
