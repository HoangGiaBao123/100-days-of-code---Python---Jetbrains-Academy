# Learn about Python List and some important list methods
# A list can contain many items
"""---------------------------------------------------------------------------------------------------""""""---------------------------------------------------------------------------------------------------"""

games_list = ['Minecraft', 'PUBG', "Talking Tom", "Roblox"]  # This is a list
print(games_list)

"""---------------------------------------------------------------------------------------------------""""""---------------------------------------------------------------------------------------------------"""

# Find item by its index
minecraft = games_list[0]
print(minecraft)   # Output: Minecraft
# Why?
# Because Python uses zero-based indexing.
# This means we start counting from 0 instead of 1.
# So,games_list[0] gives you the first item, games_list[1] gives you the second, and so on.

"""---------------------------------------------------------------------------------------------------""""""---------------------------------------------------------------------------------------------------"""

# Adding items to the end of the list: Using append() method
games_list.append('FC26')
print(games_list)  # games_list will now become ['Minecraft', 'PUBG', "Talking Tom", "Roblox", 'FC26']

"""---------------------------------------------------------------------------------------------------""""""---------------------------------------------------------------------------------------------------"""

# Remove items: Using remove() method
games_list.remove('PUBG')
print(games_list)  # games_list will now become ['Minecraft', "Talking Tom", "Roblox", 'FC26']. No more PUBG
