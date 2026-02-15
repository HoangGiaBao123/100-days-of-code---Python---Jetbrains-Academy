# Learn multiple ifs and nesting through this Python Pizza Program

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total = 0

# Check pizza size:
if size.lower() == "s":
    total += 15

    # Check pepperoni:
    if pepperoni.lower() == "y":
        total += 2
    elif pepperoni.lower() == "n":
        total += 0
    else:
        print("Something is wrong!")

# Check pizza size:
elif size.lower() == "m":
    total += 20

    # Check pepperoni:
    if pepperoni.lower() == "y":
        total += 3
    elif pepperoni.lower() == "n":
        total += 0
    else:
        print("Something is wrong!")

# Check pizza size:
elif size.lower() == 'l':
    total += 25

    # Check pepperoni:
    if pepperoni.lower() == "y":
        total += 3
    elif pepperoni.lower() == "n":
        total += 0
    else:
        print("Something is wrong!")

# Check some invalid information:
else:
    print("Something is wrong!")

# Check extra cheese:
if (size.lower() == "s" or size.lower() == "m" or size.lower() == "l") and (extra_cheese.lower() == "y"):
    total += 1
elif (size.lower() == "s" or size.lower() == "m" or size.lower() == "l") and (extra_cheese.lower() == "n"):
    total += 0
else:
    print("Something is wrong!")

# Print the final bill:
print(f'Your final bill is: ${total}')
