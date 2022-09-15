import random 

# board with blank spaces from 0-9 
board = [' ' for x in range(10)]

def main(): 
    print('Welcome to Tic Tac Toe!')
    printBoard(board) 

    while not isBoardFull(board):
        # Check if O won 
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)  
        else: 
            print("O has won")
            break 
        
        # check if X won 
        if not isWinner(board, 'X'): 
            move = computerMove()
            # if computer cannot move then it'll return 0
            if move == 0: 
                print('Tie game')
            else: 
                insertLetter('O', move) 
                print('Computer placed "O" in position ', move)    
                printBoard(board) 
        else: 
            print("X has won")
            break 

    # check for Tie 
    if isBoardFull(board): 
        print('Tie!')



# puts letter in board position 
def insertLetter(letter, pos): 
    board[pos] = letter 

# True/false if space is free at the position 
def spaceIsFree(pos): 
    return board[pos] == ' '

# prints board 
def printBoard(board): 
    print('  |   |')
    print(' ' + board[7] + '|' + board[8] + '  | ' + board[9])
    print('  |   |')
    print('----------')
    print('  |   |')
    print(' ' + board[4] + '|' + board[5] + '  | ' + board[6])
    print('  |   |')
    print('----------')
    print(' ' + board[1] + '|' + board[2] + '  | ' + board[3])
    print('  |   |')
    print('  |   |')

# condition for winning 
def isWinner(board, letter): 
    return (board[1] == board[2] == board[3] == letter) or (board[4] == board[5] == board[6] == letter) or (board[7] == board[8] == board[9] == letter) or (board[1] == board[4] == board[7] == letter) or (board[2] == board[5] == board[8] == letter) or (board[3] == board[6] == board[9] == letter) or (board[1] == board[5] == board[9] == letter) or (board[3] == board[5] == board[7] == letter)

# checks if board is full 
# check if more than 1 blank space 
def isBoardFull(board): 
    return not board.count(' ') > 1
    #     return False
    # else: 
    #     return True 

def playerMove():
    run = True
    while run: 
        move = input("Please select position to place [X] (1-9)")
        # Try except to ask for int, without crashing program
        try: 
            move = int(move) 
            # move int must be from 1-9 and the space must be free 
            # creating small functions like spaceIsFree and insertLetter makes it easier to understand & reuse
            # spaceIsFree checks if True. No need to ask if false bc automatically checks for true 
            if move > 0 and move < 10 and spaceIsFree(move): 
                run = False 
                insertLetter('X', move) 
            else: 
                print('Please enter a number from (1-9) and pick a free space')
        except: 
            print('Please type a number!')

def computerMove(): 
    # first check if computer can win 
    # If comp cannot win, is there a move PC can do to stop player from winning? 
    # pick a corner to move 
    # if all corners are taken, then move in center 
    # if center is taken, then move to edge 

    # loop giving index, value [1, ' '; 2, X ; 3, O, etc]
    # creates list of all possible position 
    posMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0 

    # create copy of board and analyze PC moves
    # check if PC can win [O]
    # If PC cannot win, it looks to block [X] 
    for let in ['O', 'X']: 
        for i in posMoves:
            boardCopy = board[:]            # important that we do not assign boardCopy with Board. We want to copy the values 
            boardCopy[i] = let 
            if isWinner(boardCopy,let):     # Check if winning move on copied board 
                move = i 
                return move 

    # check corner 
    # random move to any corner, so it's not always 1,3,7,9 
    openCorner = [] 
    for i in posMoves:  # 1, 3, 7, 9 
        if i in [1, 3, 7, 9]:               # this is correct because we are checking i in []. We are checking the value, not the index 
            openCorner.append(i)            
    if len(openCorner) > 0:                 # must check if openCorner > 0 because if no list, program will crash 
        move = random.choice(openCorner) 
        return move         

    # check center 
    if 5 in posMoves: 
        move = 5 
        return move 

    # move to edge: 
    openEdge = [] 
    for i in posMoves:  # 1, 3, 7, 9 
        if i in [2, 4, 6, 8]:               # ???? idk if this is correct. it means appending the index not value 
            openCorner.append(i)            # should it be append(posMoves(i))? 
    if len(openCorner) > 0:                 # must check if openCorner > 0 because if no list, program will crash 
        move = random.choice(openEdge) 
        return move

    return move                             # move = 0 if nothing applies         
    

main() 

# STEPS 
# 1. Main function() 
#     i. check if game is won > isWinner 
#     ii. PC makes move
#     iii. Player checks if won > isWinner 
#     IV. check for tie 

# 2. side functions: 
#     i. isWinner() 
#     ii. playerMove()
#     iii. computerMove() 
#     IV. printBoard() 
#     V. insertLetter()   # insert letter to board 
#     VI. isBoardFree()   # check for Tie. If no possible move then tie
#     VII. isSpaceFree()  # function used within playerMove(). Not necessary but it helps simplify problem. computerMove() checks this using another method. 



# LESSONS LEARNED 
# Learned to make a tictactoe game using simple step of AI 
# learned to break down the problem into simpler functions 
# learned to leverage the power of side functions -- isWinner, playerMove, computerMove, insertLetter,
# the power of boolean return value in a function is so useful 