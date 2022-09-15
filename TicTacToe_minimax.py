import time 
import math 

board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' '}

player = "X"
bot = "O" 

def main(): 
    printBoard(board)
    while not isWinner(board): 
        playerMove()
        printBoard(board)
        pcMove() 
        printBoard(board)
        if isTie(): 
            break    
        


# printing board every turn 
# Makes dictionary readable 
def printBoard(board): 
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("--+---+--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--+---+--")
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("\n")

# Checks if space is free
# If space is not free then it'll ask user to input another position 
def spaceIsFree(position): 
    return board[position] == ' '                           # need return to tell us True/False boolean 
         
# inserting letter in open space 
def insertLetter(letter, position): 
    board[position] = letter                                # Syntax error earlier. I am not returning a value and equating it to letter. I am assigning. return board[pos] == letter isn't correct 

# Player move checks if spaceIsFree then insertLetter into board 
def playerMove():  
    while True: 
        try:                                                # Try/except allows us to handle input error 
            move = int(input('Where would you like to move? [1-9]: '))
            if spaceIsFree(move):                           # condition should be if int(input) is successful. If not it'll print the reason why and then reloop 
                insertLetter(player, move)
                break
            else: 
                print("Space is taken. Pick another position")
        except: 
            print('Please enter a number from [1-9]: ')
    if isWinner(board): 
        print('X has won!')
    if isTie(): 
        print('Tie game!')
    

# uses minMax function 
# computer will be minimizing as "O". X is maximizing 
def pcMove(): 
    bestScore = math.inf
    bestMove = 0 
    alpha = -math.inf 
    beta = math.inf
    start = time.time() 
    # loop through Keys in dictionary. Look for empty Value. Place letter and compute score using minimax F(x). Then remove the letter. 
    # if score is highest, replace current bestScore
    # bestMove for that score is the key, the number in the dictionary 
    # this f(x) pcMove and the loop relates the Key, value to the score and minimax function 
    for key in board.keys(): 
        if board[key] == ' ': 
            board[key] = bot 
            score = minimax(board, 0, alpha, beta, True)# depth of 0 but it'll increase as keys loop through the dictionary 
            board[key] = ' '               # place temp move, compute score of that move, and then remove it. Do this to compute scores of all possible moves 
            if score < bestScore: 
                bestScore = score 
                bestMove = key 
    end = time.time() 
    print("Evaluation time: {}s".format(round(end - start, 7)))

    insertLetter(bot, bestMove)  
    if isWinner(board): 
        print('O has won!')
    if isTie(): 
        print('Tie game!')
          
    return 
          

# minimax function utlized within pcMove()
def minimax(position, depth, alpha, beta, isMaximizing):
    # with any recrusive function, we need a basecase 
    # Tells us how each move is scored 
    # This is the base case right here. At the basecase, it gives a score of who won 
    # depth 0 means current node. (depth - 1) means we want to keep checking the next node down everyturn until we reach the basecase/the leaf node 
    if whichLetterWon(player): 
        return 1 
    elif whichLetterWon(bot): 
        return -1
    elif isTie(): 
        return 0 

    # maximizing 
    if isMaximizing: 
        bestScore = -math.inf
        for key in board.keys(): 
            if board[key] == ' ': 
                board[key] = player 
                score = minimax(board, depth - 1, alpha, beta, False) 
                board[key] = ' ' 
                if score > bestScore: 
                    bestScore = score
                alpha = max(alpha, score) 
                if beta <= alpha:
                    break            
        return bestScore             

    # minimizing
    else: 
        bestScore = math.inf 
        for key in board.keys(): 
            if board[key] == ' ': 
                board[key] = bot 
                score = minimax(board, depth - 1,alpha, beta, True) 
                board[key] = ' ' 
                if score < bestScore: 
                    bestScore = score
                beta = min(beta, score)
                if beta <= alpha: 
                    break            
        return bestScore
    
# Need whichLetterWon function for minimax to score winner. 
def whichLetterWon(mark): 
    if board[7] == board[8] == board[9] == mark: 
        return True 
    elif board[4] == board[5] == board[6] == mark: 
        return True
    elif board[1] == board[2] == board[3] == mark: 
        return True
    elif board[1] == board[4] == board[7] == mark: 
        return True
    elif board[2] == board[5] == board[8] == mark: 
        return True
    elif board[3] == board[6] == board[9] == mark: 
        return True
    elif board[1] == board[5] == board[9] == mark: 
        return True
    elif board[7] == board[5] == board[3] == mark: 
        return True
    else:                                  
        return False 

# winning condition
def isWinner(board): 
    if board[7] == board[8] == board[9] != ' ': 
        return True 
    elif board[4] == board[5] == board[6] != ' ': 
        return True
    elif board[1] == board[2] == board[3] != ' ': 
        return True
    elif board[1] == board[4] == board[7] != ' ': 
        return True
    elif board[2] == board[5] == board[8] != ' ': 
        return True
    elif board[3] == board[6] == board[9] != ' ': 
        return True
    elif board[1] == board[5] == board[9] != ' ': 
        return True
    elif board[7] == board[5] == board[3] != ' ': 
        return True
    else:                                  
        return False        

# check for tie 
def isTie(): 
    for key in board.keys():                # iterate through keys. Check if empty value at KV. If so then False (no tie). This method is better than hardcoding 
        if board[key] == ' ': 
            return False
    return True 
     



main()




# CODE IMPROVEMENTS
# Check for win and tie inside insertLetter(). It'll make the main function cleaner and it makes sense bc when we insert letter check if winner or tie. Why do it at the main function? 
# To loop through the keys/values in the dictionary just do: for keys in dictionary.keys(): or for values in dictionary.values() and look for the condition 
# added timer and moved checking conditions to function. Now main code is CLEAN and simple 




# LESSONS LEARNED
# 1. implementing alpha-beta pruning makes the program 10x+ faster 
# 2. alpha-beta are essential local max/min. Whenever we have a smaller beta than an alpha, it cuts off the tree. I do this when deciding what tree to prune. The current value at the node gets compared to the local max
# 3. if I repeat a program multiple times, I'll have to write a function for it - insertLetter, isSpaceFree, PCmove, PlayerMove, WinningCondition,