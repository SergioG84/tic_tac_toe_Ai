# create a board and fill it with blank spaces
board = [' ' for x in range(10)]

# insert the letter at position
def insertLetter(letter, pos):
    board[pos] = letter

# make sure the space on the board is free
def isSpaceFree(pos):
    if board[pos] == ' ':
        return True
    else:
        return False

# print the board
def printBoard(board):
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

# position number for each location
def printPositionBoard():
    print('Enter number where to place \'X\'')
    print('1' + ' | ' + '2' + ' | ' + '3')
    print('-----------')
    print('4' + ' | ' + '5' + ' | ' + '6')
    print('-----------')
    print('7' + ' | ' + '8' + ' | ' + '9')
    print('-----------------------------------------------')

# place X where player specifies
def playerMove():
    run = True
    while run:
        print('-----------------------------------------------')
        move = input("Enter a number between 1 and 9 for X position: ")
        try:
            move = int(move)
            if move > 0 or move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Space is full, try again')
            else:
                print('Enter a number between 1 and 9')
        except:
            print('Type a number, for example, 4')


def comMove():
    # create a list of possible moves for the com to input
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' 'and x != 0]
    move = 0

    # check for move to win or block player winning move
    for lett in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = lett
            if winner(boardCopy, lett):
                move = i
                return move

    # check for open corners
    corners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            corners.append(i)

    # if a corner is open, move to a random one 
    if len(corners) > 0:
        move = pickRandom(corners)
        return move

    # check for center
    # center is equal to 5 on the board
    if 5 in possibleMoves:
        move = 5
        return move

    # check for edges
    edges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edges.append(i)
    if len(edges) > 0:
        move = pickRandom(edges)
        return move

    return move


def pickRandom(list):
    import random
    length = len(list)
    randomNumber = random.randrange(0, length)
    return list[randomNumber]


# make sure the board is not full
def boardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


# check to see if com or player won
# winner() will return True if either com or player one
def winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
        (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
        (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
        (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
        (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
        (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
        (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
        (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def main():
    printPositionBoard()
    print('Start the game!')
    printBoard(board)
    # main game loop
    while not (boardFull(board)):
        # check if com won
        if not winner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print('O\'s won!')
            break
        # check if player won
        if not winner(board, 'X'):
            move = comMove()
            if move == 0:
                break
            else:
                insertLetter('O', move)
                print('Computer put an \'O\' in position ' + str(move) + ':')
                printBoard(board)
        else:
            print('X\'s won!')
            break

    if boardFull(board):
        print('It\'s a tie!')

main()

while True:
    userInput = input('Would you like to play again? Y or N: ')
    if userInput == 'y' or userInput == 'Y':
        board = [' ' for x in range(10)]
        main()
    else:
        print('Thanks for playing!')
        break
