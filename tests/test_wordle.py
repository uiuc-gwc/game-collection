import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from wordle_fillable import Wordle
import utils.utils as utils

def test_wonGame():
    w = Wordle()
    w.guessedWords = ["HELLO", "ALOHA", "WORLD"]

    # The word is "HELLO"
    # The player has guessed "HELLO"
    w.word = "HELLO"
    assert w.wonGame() == True

    # The word is "GREAT"
    w.word = "GREAT"
    assert w.wonGame() == False
    

def test_getWordStringWithColor():
    w = Wordle()
    w.word = "ASDFG"
    
    # checking "SDCFG"
    correctColor = utils.colorText("S", "yellow") + \
                    utils.colorText("D", "yellow") + \
                    utils.colorText("C", "white") + \
                    utils.colorText("F", "green") + \
                    utils.colorText("G", "green")
    
    assert w.getWordStringWithColor("SDCFG") == correctColor

def test_guessValid():
    w = Wordle()
    # valid guess
    w.word = "HELLO"
    assert w.guessValid("HELLO") == True

    # guess is not 5 letters
    guess = "HELLOOO"
    assert w.guessValid(guess) == False

    # guess is not in the word list
    guess = "ASDFG"
    assert w.guessValid(guess) == False

def test_gameFinished():
    w = Wordle()

    # game has finished because the player has won
    w.word = "HELLO"
    w.guessedWords = ["HELLO"]
    w.nGuessesLeft = 5
    assert w.gameFinished() == True

    # player has "won" but they ran out of guesses
    w.nGuessesLeft = 0
    assert w.gameFinished() == True

    # no guesses left
    w.nGuessesLeft = -1
    assert w.gameFinished() == True
    
    # game has finished because the player has run out of guesses
    w.guessedWords = ["HELLO", "ALOHA", "WORLD"]
    w.word = "GREAT"
    w.nGuessesLeft = 0
    assert w.gameFinished() == True
