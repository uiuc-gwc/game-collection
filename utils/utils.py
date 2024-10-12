def getEnglishWordList(length=None):
    with open("utils/dwyl-english-words.txt") as file:
        lines = [line.rstrip() for line in file \
                 if (length == None or len(line.rstrip()) == length)]
    return lines

def playAgain():
    validInput = False
    while not validInput:
        playagain = input("\n\nThat was fun! play again? (y/n)\n")
        if playagain.lower() == "yes" or playagain.lower() == "y":
            validInput = True
            return True
        elif playagain.lower() == "no" or playagain.lower() == "n":
            validInput = True
            return False
        else: 
            print("Please enter a valid answer.")