position = [0,0]
amount = 3
direction = 'E'

def check_east(board, position, amount, direction):
    y = position[0]
    x = position[1]
    for tile in range(amount):
        x += 1
        return movement_check()
        # if board[y,x] != 'o': # extract
        #     return False

def movement_check():
    if board[x,y] != '0':
        return False
    return True

