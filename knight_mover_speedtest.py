from timeit import default_timer as timer
import math
import csv

start = timer()

# returns a tuple of x,y coordinates after taking a step in one
#  of four directions
def next_position(x, y, direction):
    if (direction==1): # right
        return x+1, y
    elif (direction==2): # up
        return x, y-1
    elif (direction==3): # left
        return x-1, y
    elif (direction==4): # down
        return x, y+1


# returns a list of what direction we need to go after numbering
#  each square
def make_turn_map(max_size):
    turn_list = []
    turn_number = 0
    direction = 1
    while (len(turn_list) < max_size):
        turn_number += 1
        for i in range(1, math.ceil(turn_number/2) + 1):
            turn_list.append(direction)
        direction = direction % 4 + 1
    return(turn_list[0:max_size]) # truncates the list


# makes a 2d array with a spiral-numbered board pattern
#  n should be an odd integer
def make_board(n):
    turn_map = make_turn_map(n*n)
    board = [[0]*n for i in range(n)]
    x = math.floor(n/2)
    y = math.floor(n/2)
    board[y][x] = 0
    for i in range(1, n*n):
        direction = turn_map.pop(0)
        x, y = next_position(x,y,direction)
        board[y][x] = i
    return(board)


# gets the next position of the knight
#  returns the lowest-numbered non-visited square available
def get_next_position(x, y, board, visited):
    low_value = math.inf
    low_x, low_y = (math.inf, math.inf)

    chk_x, chk_y = (x+1, y-2) # up and right
    if (board[chk_y][chk_x] < low_value and visited[chk_y][chk_x] == 0):
        low_value, low_x, low_y = (board[chk_y][chk_x], chk_x, chk_y)
    chk_x, chk_y = (x-1, y-2) # up and left
    if (board[chk_y][chk_x] < low_value and visited[chk_y][chk_x] == 0):
        low_value, low_x, low_y = (board[chk_y][chk_x], chk_x, chk_y)
    chk_x, chk_y = (x+1, y+2) # down and right
    if (board[chk_y][chk_x] < low_value and visited[chk_y][chk_x] == 0):
        low_value, low_x, low_y = (board[chk_y][chk_x], chk_x, chk_y)
    chk_x, chk_y = (x-1, y+2) # down and left
    if (board[chk_y][chk_x] < low_value and visited[chk_y][chk_x] == 0):
        low_value, low_x, low_y = (board[chk_y][chk_x], chk_x, chk_y)
    chk_x, chk_y = (x+2, y-1) # right and up
    if (board[chk_y][chk_x] < low_value and visited[chk_y][chk_x] == 0):
        low_value, low_x, low_y = (board[chk_y][chk_x], chk_x, chk_y)
    chk_x, chk_y = (x+2, y+1) # right and down
    if (board[chk_y][chk_x] < low_value and visited[chk_y][chk_x] == 0):
        low_value, low_x, low_y = (board[chk_y][chk_x], chk_x, chk_y)
    chk_x, chk_y = (x-2, y-1) # left and up
    if (board[chk_y][chk_x] < low_value and visited[chk_y][chk_x] == 0):
        low_value, low_x, low_y = (board[chk_y][chk_x], chk_x, chk_y)
    chk_x, chk_y = (x-2, y+1) # left and down
    if (board[chk_y][chk_x] < low_value and visited[chk_y][chk_x] == 0):
        low_value, low_x, low_y = (board[chk_y][chk_x], chk_x, chk_y)
    if (low_value < math.inf):
        return low_x, low_y
    else:
        return False


# initial setup
print('setting up board...')
n = 111                                 # NxN board (must be odd)
board = make_board(n)                   # numbering of board (0=center)
visited = [[0]*n for i in range(n)]     # for marking visited squares
x =  math.floor(n/2)
y =  math.floor(n/2)
visited[y][x] = 1
moves = 0
stuck = False
sequence = [0]

# main loop
while (stuck==False):
    next_pos = get_next_position(x,y,board,visited)
    if (next_pos==False):
        stuck = True
        print('got stuck!')
    else:
        moves += 1
        x, y = next_pos
        visited[y][x] = 1
        sequence.append(board[y][x])

end = timer()
print((end - start))

# save sequence to csv
print('writing sequence of moves to csv...')
with open('sequence.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(sequence)
print('done')


