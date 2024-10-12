import utils.utils as utils
import random

class HangmanGame:
    def __init__(self, numLetters=0):
        self.word = self.chooseWord(numLetters).upper() # The word the player is trying to guess
        self.guessedWord = ["_"] * len(self.word) # The state of the Hangman Board right now
        self.nWrongGuessesLeft = 5 # How many wrong guesses the player has left
        self.guessedLetters = [] # What letters the player has guessed so far. 

    def chooseWord(self, numLetters=0):
        englishWords = utils.getEnglishWordList()
        # Keep fishing for words until we find one of the correct length
        wordFound = False
        while not wordFound:
            index = random.randint(0, len(englishWords)-1)
            word = englishWords[index]
            if numLetters == 0 or len(word) == numLetters:
                wordFound = True
        return word

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
            guess = input("What letter will you guess? ").upper()
            if self.validateInput(guess):
                if #TODO: Check if the player has already guessed the letter:
                    # TODO: Print some error message when the player has already guessed the letter!
                else:
                    self.guessedLetters.append(guess)
                    #[TODO: What to do when the player makes a valid guess?]
            else:
                print("Sorry, that was not a valid input! ")
        if #[TODO: PLAYER HAS RUN OUT OF GUESSES]:
            # Print an error message for when the player has run out of guesses
        if #[TODO: PLAYER HAS GUESSED THE WHOLE WORD]:
            # print some congratulations for when the player succeeds! 

if __name__ == "__main__":
    # While the player is okay with playing, play the game. 
    playing = True
    while playing:
        game = HangmanGame()
        game.playGame()

        playing = utils.playAgain()
