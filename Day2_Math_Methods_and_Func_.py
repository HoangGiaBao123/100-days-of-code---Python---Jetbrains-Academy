import math   # This library will provide you some math methods

# Flooring a Number
a = 3.738492
floor_num1 = math.floor(a)    # This is the floor() method -> a = 3
floor_num2 = int(a)           # Int() can also floor a decimal number -> a = 3

# Rounding a Number
b = 66.8284978
round_num = round(b)          # This is the round() function -> b = 67
print(round(3.14159999, 2))   # This is also the round() func with 2 decimal places -> 3.14159999 = 3.14

# f-Strings
print(f'{b} with round() function = {round(b)}')
print(f"{a} with floor() method = {math.floor(a)}")
# f-Strings can work with both "" and ''
