import utils.utils as utils
import random

class Wordle:
    def __init__(self):
        self.fullWordList = utils.getEnglishWordList(length=5, common=False)
        self.word = self.chooseWord().upper()
        self.nGuessesLeft = 6
        self.guessedWords = []
        
    def chooseWord(self):
        englishWords = utils.getEnglishWordList(length=5)
        index = random.randint(0, len(englishWords)-1)
        return englishWords[index]
    
    # return True if the player has won the game, 
    # False if the game isn't finished (or the player didn't win)
    def wonGame(self):
        if self.word in self.guessedWords:
            return True
        return False        
    
    # return a STRING with text properly colored. 
    def getWordStringWithColor(self, text):
        wordStr = ""
        for i in range(5):
            ch = text[i]
            if ch == self.word[i]:
                wordStr += utils.colorText(ch, "green")
            elif ch != self.word[i] and ch in self.word:
                wordStr += utils.colorText(ch, "yellow")
            else:
                wordStr += utils.colorText(ch, "white")

        return wordStr
    
    def displayBoard(self):
        for i in self.guessedWords:
            print(self.getWordStringWithColor(i))
        print()

    def playGame(self):
        # print(f"{self.word=}") # Uncomment this line to see the answer. 
        
        # Repeat until the player has finished the game.
        while self.nGuessesLeft > 0 and not self.wonGame():
            # Print the current Wordle board. 
            self.displayBoard()

            # Get a new guess from the player. 
            guess = input("What word will you guess? ").upper()

            # Check if the guess is valid.
            if len(guess) == 5 and guess.lower() in self.fullWordList:
                # Add the guess to the list of guessed words. 
                self.guessedWords.append(guess)
                # Decrement the number of guesses left.
                self.nGuessesLeft = self.nGuessesLeft - 1
            else:
                print("That wasn't a valid guess! Please enter a 5-letter word.")
            print(f"You have {self.nGuessesLeft} guesses left.")

        # The game has ended. 
        # If the player won, print a congratulations. 
        # If the player lost, print the word (and that they ran out of guesses)
        self.displayBoard()
        if self.wonGame():
            print("Congratulations! You won!")
        else:
            print(f"Sorry, you ran out of guesses! The word was {self.word}")

if __name__ == "__main__":
    # While the player is okay with playing, play the game. 
    playing = True
    while playing:
        game = Wordle()
        game.playGame()

        playing = utils.playAgain()