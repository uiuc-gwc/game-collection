import random

class RockPaperScissors:
 
    # Returns True if the player's guess is "better" than the computer's guess.
    # Returns False if the computer's guess is "better" than the player's guess.
    def wonGame(self, guess, result):
        # TODO: Write an if statement to determine if the player won the game
        pass # delete this line of code one completed. 

    def playGame(self):
        # Input the players guess
        guess = input("Rock, paper, or scissors?").upper()

        # TODO: Write an if statement to validate that the guess is either "Heads" or "Tails"
        if False: # Change this line of code
            print("That wasn't a valid guess! Please enter 'Rock', 'Paper', or 'Scissors'.")
            return
       
        # Have the computer choose one of the options
        # TODO: Use the random.choice() function to 
        # randomly select one of ROCK, PAPER, or SCISSORS
        # and assign the result to the 'result' variable.
        result = ""

         # Check if the guess was correct
        if self.wonGame(guess, result): 
            # TODO: Print a congratulations message if the player won
            print("")
        else:
            # TODO: Print a message telling the player they lost and the result
            print("")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.playGame()