# Tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip = 1 + tip / 100

each_person_bill = (bill / people) * tip

print(f'Each person should pay ${each_person_bill:.2f}')
