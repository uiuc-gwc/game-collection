import pytest
from wordle_fillable import Wordle

def test_wonGame():
    w = Wordle()
    w.guessedWords = ["HELLO", "ALOHA", "WORLD"]

    # The word is "HELLO"
    # The player has guessed "HELLO"
    w.word = "HELLO"
    assert w.wonGame() == True
    
