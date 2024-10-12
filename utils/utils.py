from colorama import init as colorama_init
from colorama import Fore, Back, Style

def getEnglishWordList(length=None, common=True):
    if common:
        wordsFile = "utils/google-10000-usa-common.txt"
    else:
        wordsFile = "utils/dwyl-english-words.txt"
    with open(wordsFile) as file:
        lines = [line.strip() for line in file \
                 if (length == None or len(line.strip()) == length)]
    return lines

def colorText(text, color):
    # print in the terminal but have the text colored
    # color is a string that is one of the following:
    # "red", "green", "yellow", "blue", "magenta", "cyan", "white"
    colorama_init()
    # match the input color string to the colorama colors
    styles = {
        "red" : Fore.RED,
        "green": Fore.GREEN,
        "yellow" : Fore.YELLOW,
        "blue" : Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan" : Fore.CYAN,
        "white" : Fore.WHITE,
    }

    # actually apply the colors. 
    return f"{styles[color]}{text}{Style.RESET_ALL}"


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