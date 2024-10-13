import utils.utils as utils
import random

class Wordle:
    def __init__(self):
        self.fullWordList = utils.getEnglishWordList(length=5, common=False) # The list of all english words.
        self.word = self.chooseWord().upper() # choose a word to be "THE" wordle word. 
        self.nGuessesLeft = 6 # number of guesses left in the wordle game.
        self.guessedWords = [] # The list of words that have been guessed. 
        
    def chooseWord(self):
        englishWords = utils.getEnglishWordList(length=5)
        index = random.randint(0, len(englishWords)-1)
        return englishWords[index]
    
    # return True if the player has guessed the word correctly,
    # False if the game isn't finished (or the player didn't win)
    # Do not worry about number of guesses 
    # Just figure out if the player has guessed the word correctly 
    def wonGame(self):
        # TODO Implement this function.
        pass          
    
    # return a STRING with text properly colored. 
    # text is a 5-letter word. 
    # We want to color the text as follows:
    # 1. If the letter is in the correct position, color it green.
    # 2. If the letter is in the word but not in the correct position, color it yellow.
    # 3. If the letter is not in the word, color it white.
    # Use utils.colorText to color the text.
    # Example: To color a letter 'a' green, use utils.colorText('a', 'green')
    def getWordStringWithColor(self, text):
        # TODO: implement this function
        pass # remove this line after finishing the above TODO
    
    # Display the Wordle board. All the words that have been guessed so far.
    def displayBoard(self):
        # Iterate through the guessed words and print them with the correct colors.
        # Hint: Use the getWordStringWithColor function to get the correctly colored string.
        # TODO: Implement this function.        
        pass # remove this line after finishing the above TODO

    # return True if the Wordle game has finished, False otherwise. 
    # Make sure to consider the number of guesses. 
    def gameFinished(self):
        # TODO: Implement this function.
        pass # remove this line after finishing the above TODO
    
    # return True if the player's guess (guess variable) is valid
    # return False if the player's guess is invalid. 
    def guessValid(self, guess):
        # TODO: Implement this function.
        pass # remove this line after finishing the above TODO

    def playGame(self):
        # print(f"{self.word=}") # Uncomment this line to see the answer. 

        # Repeat until the player has finished the game.
        while not self.gameFinished():
            # Print the current Wordle board. 
            self.displayBoard()

            # Get a new guess from the player. 
            guess = input("What word will you guess? ").upper()

            # Check if the guess is valid.
            if self.guessValid(guess):
                # Add the guess to the list of guessed words. 
                # Decrement the number of guesses left.
                # TODO Implement this. 
                pass # remove this line after finishing the above TODO
            else:
                print("That wasn't a valid guess! Please enter a 5-letter word.")
            # TODO: print the number of guesses left. 

        # The game has ended. 
        # If the player won, print a congratulations. 
        # If the player lost, print the word (and that they ran out of guesses)
        self.displayBoard()
        # TODO: Print congratulations if the player won, the word if the player lost. 

if __name__ == "__main__":
    # While the player is okay with playing, play the game. 
    playing = True
    while playing:
        game = Wordle()
        game.playGame()

        playing = utils.playAgain()