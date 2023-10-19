class HangmanGame:
    def __init__(self):
        pass


if __name__ == "__main__":
    # While the player is okay with playing, play the game. 
    playing = True
    while playing:
        game = HangmanGame()
        game.runGame()

        validInput = False
        while not validInput:
            playagain = input("\n\n That was fun! play again? (y/n)\n")
            if playagain.lower() == "yes" or playagain.lower() == "y":
                validInput = True
            elif playagain.lower() == "no" or playagain.lower() == "n":
                validInput = True
                playing = False
                print("Thanks for playing! Hope to see you soon. ")
            else: 
                print("Please enter a valid answer.")
