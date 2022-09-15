# create dictionary 1-9. using dictionary to map X & 0. We can store the values pressing number 1-9.
# Create function print_game for a visual of the values
# Ask user for input & make X or O
# Input user input into function using dictionary K-V
# Conditions:
#   i. if any vlaue for r1, r2, r3, c1,c2,c3, or d1,d2 == same, then print winnner

# dictionary storing number and values: K-V 
table_dict = {7: " ",8: " ",9: " ",
              4: " ",5: " ",6: " ",
              1: " ",2: " ",3: " "}



def main(): 
    letter = 'X'

    for i in range(9):  
        # asking player where to move
        print("It's your turn " + letter + ',',end=' ')
        loc = int(input("Where would you like to go? ")) 

        # User cannot go in a spot that's already taken 
        while table_dict[loc] != " ": 
            print('Please choose a valid location')
            loc = int(input("Where would you like to go? "))

        table_dict[loc] = letter 
        print_game(table_dict)

        # alternate turns btwn X & O 
        if letter == 'X':
            letter = 'O' 
        else: 
            letter = 'X'

        # game winning conditions 
        # row winner condition 
        if (table_dict[7] == table_dict[8] == table_dict[9] != ' '): 
            print("Winner is: " + table_dict[7])
            break
        elif (table_dict[4] == table_dict[5] == table_dict[6] != ' '): 
            print("Winner is: " + table_dict[4])
            break       
        elif (table_dict[1] == table_dict[2] == table_dict[3] != ' '): 
            print("Winner is: " + table_dict[1]) 
            break
        # col winner condition 
        elif (table_dict[1] == table_dict[4] == table_dict[7] != ' '):                
            print("Winner is: " + table_dict[1]) 
            break
        elif (table_dict[2] == table_dict[5] == table_dict[8] != ' '):
            print("Winner is: " + table_dict[2]) 
            break
        elif (table_dict[3] == table_dict[6] == table_dict[9] != ' '):
            print("Winner is: " + table_dict[3]) 
            break
        # diagonal win condition 
        elif (table_dict[1] == table_dict[5] == table_dict[9] != ' '):
            print("Winner is: " + table_dict[1]) 
            break
        elif (table_dict[7] == table_dict[5] == table_dict[3] != ' '):
            print("Winner is: " + table_dict[7]) 
            break
        # tie when no values equal in a line 
        elif i == 8:  
            print("Tie!") 


# prints dictionary onto a board everyturn 
# value of table_dict updates every input 
# table_dict[loc] = VALUE 
def print_game(table_dict): 
    print(table_dict[7] + " | " + table_dict[8] + " | " + table_dict[9])
    print("---------")
    print(table_dict[4] + " | " + table_dict[5] + " | " + table_dict[6])
    print("---------")
    print(table_dict[1] + " | " + table_dict[2] + " | " + table_dict[3])


main() 


# don't use global variable unless needed 
# conditons are if same and not blank/ None
# Main idea is using dictionary to represent k-v. K are the numberpads and the values are 'x' & 'o'. We also use a print statement to print the board everyturn 
# steps to solving. 
# 1. create dictionary with Keys and no value: board = {7: '', 8: ''...}
# 2. ask user for value at dictionary key: board[loc] = value (x or o) 
# 3. Make sure user doesnt input key in existing spot: while board[loc]:
#   i. instead of putting while board[loc] is not empty. Simply ask if board[loc] has a value. If so, ask for another one instead of using a double negative 
# 


# I can better design this to make the main function easier to read by moving the condition to a check function 
# def checkWinner(table_dict, letter) 