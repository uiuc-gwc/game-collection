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
        # Make sure inp is a string of length 1 and is an alphabet. 
        return len(inp) == 1 and inp.isalpha()
    
    def fillInWord(self, guess):
        # 'guess' is the letter the player has guessed. 
        # update the state of the board (self.guessedWord) to include this guess. 
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.guessedWord[i] = guess

    def playGame(self):
        # This is the gameplay. 
        while "_" in self.guessedWord and self.nWrongGuessesLeft > 0:
            self.displayWord()
            self.displayGuesses()
            inp = input("What letter will you guess? ").upper()
            if self.validateInput(inp):
                if inp in self.guessedLetters:
                    print("You have already guessed this letter!")
                else:
                    self.guessedLetters.append(inp)
                    if inp in self.word:
                        self.fillInWord(inp)
                    else:
                        print("Sorry, {} is not in this word!".format(inp))
                        self.nWrongGuessesLeft -= 1
                        print("You have {} wrong guesses left.".format(self.nWrongGuessesLeft))
            else:
                print("Sorry, that was not a valid input! ")
        if self.nWrongGuessesLeft == 0:
            print("Sorry! You have run out of guesses. The word was:")
            print(self.word)
        if "_" not in self.guessedWord:
            self.displayWord()
            print("Congratulations! You guessed the word! ")

if __name__ == "__main__":
    # While the player is okay with playing, play the game. 
    playing = True
    while playing:
        game = HangmanGame()
        game.playGame()

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
