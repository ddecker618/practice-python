import random
import re

# lets create a board object to represent the minesweeper game
# this is so that we can just say 'create a new board object', or
# 'dig here', or 'render this game for this object'
class Board:
    def __init__(self, dim_size, num_bombs):
        #let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function!
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set() # if we dig at 0,0, then self.dug = {(0,0)}

        def make_new_board(self):
            # construct a new board based on the dim size and num num_bombs
            # we should construct the list of lists here (or whatevere representation you prefer,
            # but since we have a 2-d board, list of lists is most natural)

            # generate a make_new_board
            board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
            # this creates an array like this:
            # [[None, None, ..., None],
            #  [None, None, ..., None],
            #  [...                  ],
            #  [None, None, ..., None]]
            # we can see how this represents a board!

            # plant the num_bombs
            bombs_planted = 0
            while bombs_planted < self.num_bombs:
                loc = random.randint(0, self.dim_size**2 - 1) # return a random integer N such that a <= N <= b
                row = loc // self.dim_size
                col = loc % self.dim_size

                if board[row][col] == '*':
                    # this means we've actually already planted a bomb there so keep going
                    continue

                board[row][col] = '*' # plant the bomb
                bombs_planted += 1

            return board

    def assign_values_to_board(self)
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. we can precompute these and it'll save us some
        # effort checking what's around the board later on
        for r in range (self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is a bomb, we don't want to calculate anythiong
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs_planted
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure not to go out of bounds!

        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) + 1):
            for c in range(max(0, col-1), min(self.dim_size-1, col-1) +1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location!
        # return true if successful dig, false if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors!

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) + 1):
            for c in range(max(0, col-1), min(self.dim_size-1, col-1) +1):
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r, c)
        # if our initial dig didn't hit a bomb, we shouldn't hit a bomb here
                return True


    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ''
        # put this together in a string

# play the game
def play (dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if the location is a bomb show a game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is
    #          at least next to a bombs
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> Victory!
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # 0,0 or 0, 0 or 0,   0
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col:")) # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_sizeor col < 0 or col >= dim_size
            print('Invalid location. Try again.')
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            #dug a bomb
            break # (game over you dead)

    # 2 ways to end loop, let's check
    if safe:
        print('Live to see another day')
    else:
        print('Hope you had life insurance')
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': # good practice
    play()
