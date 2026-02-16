# Who can hang out with you today?
import random

friends = []
how_many_friends = int(input("How many do you have? "))

for friend in range(how_many_friends):
    friend = input(f"Friend {friend + 1} (Enter his/her name): ")
    friends.append(friend)

random_num = random.randint(0, len(friends))
random_friend = friends[random_num]
print(f'The friend can hang out with you is: {random_friend}')
