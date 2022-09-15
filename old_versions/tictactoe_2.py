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
        
        isWinner(table_dict, i)

        


# prints dictionary onto a board everyturn 
# value of table_dict updates every input 
# table_dict[loc] = VALUE 
def print_game(table_dict): 
    print(table_dict[7] + " | " + table_dict[8] + " | " + table_dict[9])
    print("---------")
    print(table_dict[4] + " | " + table_dict[5] + " | " + table_dict[6])
    print("---------")
    print(table_dict[1] + " | " + table_dict[2] + " | " + table_dict[3])

def isWinner(table_dict, i): 
    if (table_dict[7] == table_dict[8] == table_dict[9] != ' '): 
        print("Winner is: " + table_dict[7])
        
    elif (table_dict[4] == table_dict[5] == table_dict[6] != ' '): 
        print("Winner is: " + table_dict[4])
        
    elif (table_dict[1] == table_dict[2] == table_dict[3] != ' '): 
        print("Winner is: " + table_dict[1]) 
        
        # col winner condition 
    elif (table_dict[1] == table_dict[4] == table_dict[7] != ' '):                
        print("Winner is: " + table_dict[1]) 
        
    elif (table_dict[2] == table_dict[5] == table_dict[8] != ' '):
        print("Winner is: " + table_dict[2]) 
        
    elif (table_dict[3] == table_dict[6] == table_dict[9] != ' '):
        print("Winner is: " + table_dict[3]) 
        
        # diagonal win condition 
    elif (table_dict[1] == table_dict[5] == table_dict[9] != ' '):
        print("Winner is: " + table_dict[1]) 
        
    elif (table_dict[7] == table_dict[5] == table_dict[3] != ' '):
        print("Winner is: " + table_dict[7]) 
        
    # tie when no values equal in a line 
    elif i == 8: 
        print("Tie!") 


main() 


# similar to version1. Moved long conditional statement to a seperate function for readability 
# code breaks when using test case where number is outside of 1-9. Use a Try & except condition 
# Try & accept helps handle errors so program doesn't crash 
# the idea is creating a simple, efficient, robust program that solves the problem 