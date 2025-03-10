import random
import re


class Board:
    def __init__(self,dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug = set()

    def make_new_board(self):
        #construct a board based on dim_size and num_bombs
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #Create a complete list with value None
        bombs_planted = 0
        while bombs_planted<self.num_bombs:
            loc = random.randint(0,self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                #this means we have actually planted a bomb
                continue
            board[row][col] = '*'
            bombs_planted+=1
        return board

    def assign_values_to_board(self):
        #Let's assign values to board between 0-8 where there are no bombs
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self,row,col):
        num_neighboring_bombs = 0
        for r in range(max( 0, row-1), min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1, col+1)+1):
                if r==row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs+=1 
        
        return num_neighboring_bombs

    def dig(self,row,col):
        #It returns True if successful dig, else Return False
        self.dug.add((row,col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] >0:
            return True 

        for r in range(max( 0, row-1), min(self.dim_size-1,(row+1))+1):
            for c in range(max(0,col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
        
        return True
#
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])

                else:
                    visible_board[row][col] = " "

        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
# Start the Game
def play(dim_size = 10, num_bombs = 10):
    #step1 Create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    #step2 Show the user the board and ask for user where they want to dig
    #step 3:
        #If location is a bomb, show game over
        #If location is not a bomb, then dig recursively unitl each square is at least next to a bomb
    #repeat step 2 and 3 unitl there are no more to dig
    #print Won if they didn't dig any bombs
    safe = True

    while len(board.dug) < board.dim_size **2 - num_bombs:
        print(board)
    
        user_input = re.split(',(\\s)*',input("Where would you like to dig? Input as row,col: "))
        row,col = int(user_input[0]),int(user_input[-1])
        if row<0 or row>=board.dim_size or col<0 or col>=dim_size:
            print("Invalid location. Try again.")
            continue

        safe = board.dig(row,col)
        if not safe:
            break 

    if safe:
        print("CONGRATULATIONS! YOU WON THE GAME")
    else:
        print("SORRY! Try Again :)")

        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
    
if __name__ == '__main__':
    play()
