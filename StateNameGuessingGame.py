states={'alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming'}
statescopy = states.copy()
correctAnswers = set()
points = 0

print("State guessing game \nName as many states as you can!")
gameActive = True
while gameActive:
    userInput = input("Quit (q) / Word (enter state): ")
    if userInput.lower() in statescopy:
        statescopy.remove(userInput.lower())
        print(f"Correct! {userInput} is a state")
        correctAnswers.add(userInput.lower())
        points += 1
    elif userInput.lower() == "q":
        gameActive = False
    else:
        if userInput.lower() in correctAnswers:
            print("You have named that state already!")
        else:
            print("Incorrect Answer!")
            points -= 1

print(f"Congratulations, you got {points} points!")
