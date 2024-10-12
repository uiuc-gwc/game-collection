import random
import utils.utils as utils

class TicTacToeGame:
    def __init__(self, numPlayers=2):
        self.numPlayers = numPlayers # number of players
        self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]# A blank Tic Tac Toe board

    def checkForWinner(self):
        # Check if any player has won. 
        # Return the player char if won, else return None

        # Check rows
        for i in range(0, 3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] \
                and self.board[i][0] != " ":
                return self.board[i][0]
            
        # Check columns
        for i in range(0, 3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] \
                and self.board[0][i] != " ":
                return self.board[0][i]
            
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] \
            and self.board[1][1] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] \
            and self.board[1][1] != " ":
            return self.board[0][0]
    
        return None
    
    def displayBoard(self):
        # Print the current state of the board. 
        print(f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}")
        print("---------")
        print(f"{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}")
        print("---------")
        print(f"{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")
        print()

    # Returns True if a move in position [row, col] is valid. 
    # Otherwise, returns False
    def isMoveValid(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        return self.board[row][col] == " "
    
    # Return True if there are moves possible; False if there are no possible moves left. 
    def movesPossible(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == " ":
                    return True
                
    def generateComputerMove(self):
        # randomly choose a free cell. 
        free_cells = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == " ":
                    free_cells.append([i, j])

        return random.choice(free_cells)

    def playGame(self):
        # This is the "Main Game Loop"
        currentPlayer = 1
        while self.checkForWinner() == None and self.movesPossible():
            self.displayBoard()

            # Decide to have the computer play or player #2 play. 
            if self.numPlayers == 1 and currentPlayer == 2:
                # Computer's turn
                print("Computer's move:")
                row, col = self.generateComputerMove()
            else:
                validMove = False
                while not validMove:
                    row = int(input(f"Player {currentPlayer}: Enter the row number (0-2) "))
                    col = int(input(f"Player {currentPlayer}: Enter the column number (0-2) "))
                    validMove = self.isMoveValid(row, col)
                    if not validMove:
                        print("Sorry, we cannot place a move at that cell. Please try again.")
            
            # Perform the move
            if currentPlayer == 1:
                self.board[row][col] = "X"
            else:
                self.board[row][col] = "O"

            # Switch player from player 1 to player 2
            if currentPlayer == 1:
                currentPlayer = 2
            else:
                currentPlayer = 1

        # Game over. Display the winner (or if it's a draw, display that.)

        self.displayBoard()
        winner = self.checkForWinner()
        if winner == "X":
            print("Player 1 wins!")
        elif winner == "O":
            if self.numPlayers == 1:
                print("Computer wins!")
            else:
                print("Player 2 wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    # While the player is okay with playing, play the game. 
    playing = True
    while playing:
        validNPlayers = False
        while not validNPlayers:
            nPlayers = input("How many players will be playing? (1 or 2) ")
            if nPlayers == "1" or nPlayers == "2":
                validNPlayers = True
            else:
                print("Please enter a valid number of players.")
        game = TicTacToeGame(int(nPlayers))
        game.playGame()

        playing = utils.playAgain()
