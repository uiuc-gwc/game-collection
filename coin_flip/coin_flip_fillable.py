import random

class CoinFlip:
 
    # Returns True if the player's guess matches the coin flip result.
    # Returns False if the player's guess does not match the coin flip result.
    def wonGame(self, guess, result):
        return guess == result        

    def playGame(self):
        # Input the players guess
        guess = input("What is your guess (Heads or Tails)? ").upper()

        # TODO: Write an if statement to validate that the guess is either "Heads" or "Tails"
        if False: # Change this line of code
            print("That wasn't a valid guess! Please enter 'Heads' or 'Tails'.")
            return
       
        # Flip a coin (randomly choose Heads or Tails)
        # TODO: Use the random.choice() function to randomly select either 'HEADS' or 'TAILS' 
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
    game = CoinFlip()
    game.playGame()