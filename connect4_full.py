import utils.utils as utils

class Connect4:
    def __init__(self):
        self.nrows = 6
        self.ncols = 7
        self.board = self.createBoard()
        self.currentPlayer = 1
    
    # Create a self.nrows x self.ncols board with all cells initialized to "."
    # "." indicates an empty cell.
    def createBoard(self):
        return [["." for _ in range(self.ncols)] for _ in range(self.nrows)]
    
    # Display the board to the console.
    # The board should be displayed with column numbers at the top.
    # Each cell should be represented by its value (either "X", "O", or ".").
    def displayBoard(self):
        # Display the board to the console. 
        print(" ".join(str(x) for x in range(self.ncols)))  # Column numbers
        for row in self.board:
            print(" ".join(row))
        print()


    # Drop a piece into the specified column for the current player.
    # The piece should fall to the lowest available row in that column.
    # Return True if the piece was successfully dropped, False if the column is full.
    # If the column is full, do not change the board and return False.
    def dropPiece(self, col):
        for i in range(self.nrows-1, -1, -1):
            if self.board[i][col] == ".":
                self.board[i][col] = "X" if self.currentPlayer == 1 else "O"
                return True
        return False
    
    # Check if the game has been won. 
    def checkWin(self):
        # Check horizontal wins
        for row in range(self.nrows):
            for col in range(self.ncols-4):
                if self.board[row][col] != "." and \
                self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3]:
                    return True

        # Check vertical wins
        for col in range(self.ncols):
            for row in range(self.nrows-4):
                if self.board[row][col] != "." and \
                self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col]:
                    return True

        # Check diagonal wins (bottom-left to top-right)
        for row in range(3, self.nrows):
            for col in range(self.ncols-4):
                if self.board[row][col] != "." and \
                self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3]:
                    return True
                
        # Check diagonal wins (top-left to bottom-right)
        for row in range(0, 3):
            for col in range(self.ncols-4):
                if self.board[row][col] != "." and \
                self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3]:
                    return True
                

        return False
    
    def playGame(self):
        print("Welcome to Connect 4!")
        self.displayBoard()

        while True:
            col = int(input(f"Player {self.currentPlayer}, choose a column (0-{self.ncols-1}): "))
            if col < 0 or col >= self.ncols:
                print("Invalid column. Try again.")
                continue
            
            if not self.dropPiece(col):
                print("Column is full. Try again.")
                continue
            
            self.displayBoard()
            
            if self.checkWin(): 
                print(f"Player {self.currentPlayer} wins!")
                break
            
            # Switch players
            self.currentPlayer = 2 if self.currentPlayer == 1 else 1



if __name__ == "__main__":
    # While the player is okay with playing, play the game. 
    playing = True
    while playing:
        game = Connect4()
        game.playGame()

        playing = utils.playAgain()