import utils.utils as utils
import random

class HangmanGame:
    def __init__(self, numLetters=0):
        self.word = self.chooseWord(numLetters).upper() # The word the player is trying to guess
        self.guessedWord = ["_"] * len(self.word) # The state of the Hangman Board right now
        self.nWrongGuessesLeft = 5 # How many wrong guesses the player has left
        self.guessedLetters = [] # What letters the player has guessed so far. 

    def chooseWord(self, numLetters=0): #(numLetters = length of desired hangman word.)
        englishWords = utils.getEnglishWordList()
        # TODO if numLetters is 0, return a randomly chosen element in englishWords. 
        # TODO if numLetters is non-zero, randomly choose elements in englishWords until you pick one that is the correct length.

    def displayWord(self):
        # Print the hangman board. 
        print("\nCURRENT STATE:")
        for i in self.guessedWord:
            print(i, end= ' ')
        print("")

    def displayGuesses(self):
        # Print the guesses that the player has already made.
        if len(self.guessedLetters) == 0:
            print("You have not guessed any letters yet.", end=" ")
        else:
            print("You have guessed so far:")
            for i in self.guessedLetters:
                print(i, end=' ')
        print("")

    def validateInput(self, inp):
        # TODO: Make sure inp is a string of length 1 and is an alphabet. 
        pass # remove this line when implementing this function        
    
    def fillInWord(self, guess):
        # 'guess' is the letter the player has guessed. 
        # update the state of the board (self.guessedWord) to include this guess. 
        # TODO
        pass # remove this line when implementing this function

    def playGame(self):
        # This is the gameplay. 
        while #[TODO: This represents the game continuing. How do we know when to continue the game?]:
            self.displayWord()
            self.displayGuesses()
            # TODO: input a guess, validate it, figure out whether the guess was correct or not, 
            #        and update either the board state or the incorrect guesses remaining. 
        if #[TODO: PLAYER HAS RUN OUT OF GUESSES]:
            # TODO Print an error message for when the player has run out of guesses
        if #[TODO: PLAYER HAS GUESSED THE WHOLE WORD]:
            # TODO print some congratulations for when the player succeeds! 

if __name__ == "__main__":
    # While the player is okay with playing, play the game. 
    playing = True
    while playing:
        game = HangmanGame()
        game.playGame()

        playing = utils.playAgain()

