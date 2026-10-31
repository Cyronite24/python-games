# The game is simple; try your luck in "Luckiest Gambler".
# It's a 50/50 chance the number is either 1 or 2.
# Hard mode is now a 33/33/33.33 chance the number is 1, 2, or 3.
# Run the software with "python3 luckiestGambler.py".

import sys
import time

gameState = 0
possibleNumbers = [1, 2, 3]

while gameState == 0:
    print("Welcome to Luckiest Gambler!\nTry your luck by guessing numbers without failing!\nThere is no endpoint, just try getting the highest score.\n")

    start_game = input("Would you like to start? [Y/n]\n> ").strip().lower()

    if start_game == 'n'.strip().lower():
        print("Exiting Python Software...")
        time.sleep(2)
        sys.exit(0)
    elif start_game == 'Y':
        print("The game has started!")
        gameState = 1
    else:
        print("this is a placeholder you dingleberries.")

while gameState == 1:
    difficulty = input("\nChoose your difficulty (Normal, Hard)")

    if difficulty == "Normal".strip().lower():
        print("NORMAL difficulty has been selected by PLAYER.")
