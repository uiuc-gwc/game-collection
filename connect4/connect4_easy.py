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
        # TODO: Write this function. DO THIS FIRST. 
        pass
    
    # Display the board to the console.
    # The board should be displayed with column numbers at the top.
    # Each cell should be represented by its value (either "X", "O", or ".").
    def displayBoard(self):
        # TODO: Write this function. DO THIS SECOND. 
        pass


    # Drop a piece into the specified column for the current player.
    # The piece should fall to the lowest available row in that column.
    # Return True if the piece was successfully dropped, False if the column is full.
    # If the column is full, do not change the board and return False.
    def dropPiece(self, col):
        # TODO: Write this function. DO THIS FOURTH.
        pass
    
    # Check if the game has been won. (For easy version, only check for horizontal and vertical wins)
    # Return True if a player has won, False otherwise.
    def checkWin(self):
        # TODO: check for horizontal and vertical wins ONLY. DO THIS FIFTH. 
        return False
    
    def playGame(self):
        print("Welcome to Connect 4!")
        self.displayBoard()

        while True:
            col = int(input(f"Player {self.currentPlayer}, choose a column (0-{self.ncols-1}): "))
            # TODO: Make sure the column entered by the player is a valid column. 
            # If it's not, print an error message and "continue." DO THIS THIRD. 
            
            if not self.dropPiece(col):
                print("Column is full. Try again.")
                continue
            
            self.displayBoard()
            
            if self.checkWin(): 
                print(f"Player {self.currentPlayer} wins!")
                break
            
            # Switch players
            # TODO: Switch self.currentPlayer to the other player (1 to 2 or 2 to 1) DO THIS ALSO THIRD. 



if __name__ == "__main__":
    # While the player is okay with playing, play the game. 
    playing = True
    while playing:
        game = Connect4()
        game.playGame()

        playing = utils.playAgain()