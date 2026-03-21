# Functions with Inputs
# Ex1:
def greeting(name):
    print(f'Hi, {name}!')

greeting("Messi")

# Ex2:
def add(num1, num2):
    result = num1 + num2
    return f'{num1} + {num2} = {result}'

expression = add(2.1, 6.7)
print(expression)

# Ex3:
def multiplication_table(number):
    for num in range(1, 11):
        print(f'{number} * {num} = {number * num}')

multiplication_table(5)
