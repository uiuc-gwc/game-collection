def getEnglishWordList():
    with open("utils/dwyl-english-words.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines