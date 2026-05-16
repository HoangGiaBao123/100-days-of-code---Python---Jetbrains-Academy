# Dictionaries
clubs = {
    "Lionel Messi": "Inter Miami",
    "Cristiano Ronaldo": "Al Nassr",
    "Neymar Junior": "Santos",
    "Kylian Mbappé": "Real Madrid",
    "Erling Haaland": "Man City",
    "Harry Maguire": "Man Utd",
    "Angél Di Mariá": "Rosario Central"
}

# Loop through keys and their values
for player in clubs:
    print(f'{player} - {clubs[player]}')

# Add new items to the dictionary
clubs["Gonzalo García"] = "Real Madrid"
clubs["Nico Paz"] = "Calcio Como"
