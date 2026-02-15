print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 100 and height <= 190:
    print("You can play rollercoaster!")
elif height < 100 or height > 190:
  print("You can NOT play rollercoaster!")
else:
    print("Something is wrong!")
