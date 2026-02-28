import random
random_num = random.randint(0, 2)

word_list = ["aardvark", "baboon", "camel"]
random_word = word_list[random_num]

print("Can you guess the secret word? Try it!")
guess = input("Enter the word you're thinking: ").lower()

attempts_count = 0

while True:
    if guess == random_word:
        attempts_count += 1
        print("Yes! You got it!")
        print(f"It took you {attempts_count} attempt")
        break
    else:
        attempts_count += 1
        print("Uh oh, you guessed wrong!")
        guess = input("Try again: ")
