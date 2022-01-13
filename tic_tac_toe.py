# hello people!!! Here is gonna be my code to play with the 
# user a little bit when he has no one to play with...
import math

winner_x_dictionary = {
    "w_1" : [1, 2, 3],
    "w_2" : [4, 5, 6],
    "w_3" : [7, 8, 9],
    "w_4" : [1, 5, 9],
    "w_5" : [1, 4, 7],
    "w_6" : [2, 5, 8],
    "w_7" : [3, 6, 9],
    "w_8" : [3, 5, 7]
}
winner_o_dictionary = {
    "w_1" : [1, 2, 3],
    "w_2" : [4, 5, 6],
    "w_3" : [7, 8, 9],
    "w_4" : [1, 5, 9],
    "w_5" : [1, 4, 7],
    "w_6" : [2, 5, 8],
    "w_7" : [3, 6, 9],
    "w_8" : [3, 5, 7]
}

tic_tac = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  #list for the tic_tac_toe numbers where I can append the x's and the o's

def main():
    """here is going to be the main code """
    table()
    # rows_and_col = int(input("How many columns and how many row you want?\
    # \n(The number of columns you enter will be the same as the rows) --> "))
    x_tics = 0
    o_tics = 0
    win = False
    while win != True:


        user_type_x = int(input("x's turn to choose a square(1-9): "))
        x_tics = x_list(user_type_x) #this is a list with the movements of the "x" gamer
        table_list = loop_table(user_type_x, game_status=win)
        win = winner(tic_tac)

        user_type_o = int(input("o's turn to choose a square(1-9): "))
        o_tics = o_list(user_type_o) #this is a list with the movements of the "x" gamer
        table_list = loop_table(user_type_o, game_status=win)
        win = winner(tic_tac)

        # user_type_o = int(input("o's turn to choose a square(1-9): ")) #this is a list with the movements of the "o" gamer
        # o_tics = o_list(user_type_o)
        # loop_table(user_type_o)
    print("Good game! We have a winner!!")

def winner(table_list):
    """This is the functio where I iterate through 
    the table to search for the results of the tic_tac_toe"""
    if  table_list[1] == "x" and \
        table_list[2] == "x" and \
        table_list[3] == "x" or \
        \
        table_list[4] == "x" and \
        table_list[5] == "x" and \
        table_list[6] == "x" or \
        \
        table_list[7] == "x" and \
        table_list[8] == "x" and \
        table_list[9] == "x" or \
        \
        table_list[1] == "x" and \
        table_list[4] == "x" and \
        table_list[7] == "x" or \
        \
        table_list[2] == "x" and \
        table_list[5] == "x" and \
        table_list[8] == "x" or \
        \
        table_list[3] == "x" and \
        table_list[6] == "x" and \
        table_list[9] == "x" or \
        \
        table_list[1] == "x" and \
        table_list[5] == "x" and \
        table_list[9] == "x" or \
        \
        table_list[3] == "x" and \
        table_list[5] == "x" and \
        table_list[7] == "x":
        return True 

    elif  table_list[1] == "o" and \
        table_list[2] == "o" and \
        table_list[3] == "o" or \
        \
        table_list[4] == "o" and \
        table_list[5] == "o" and \
        table_list[6] == "o" or \
        \
        table_list[7] == "o" and \
        table_list[8] == "o" and \
        table_list[9] == "o" or \
        \
        table_list[1] == "o" and \
        table_list[4] == "o" and \
        table_list[7] == "o" or \
        \
        table_list[2] == "o" and \
        table_list[5] == "o" and \
        table_list[8] == "o" or \
        \
        table_list[3] == "o" and \
        table_list[6] == "o" and \
        table_list[9] == "o" or \
        \
        table_list[1] == "o" and \
        table_list[5] == "o" and \
        table_list[9] == "o" or \
        \
        table_list[3] == "o" and \
        table_list[5] == "o" and \
        table_list[7] == "o":
        return True 

    else:
        return False
        

def x_list(x_input):
    ''''''
    user_x = []
    user_x.append(x_input)
    return user_x

def o_list(o_input):
    user_o = []
    user_o.append(o_input)
    ''''''
    return user_o

def table():
    ''''''
    print("\
    \n1 | 2 | 3\
    \n- + - + -\
    \n4 | 5 | 6\
    \n- + - + -\
    \n7 | 8 | 9\
    \n") 

def loop_table(user_turn, game_status=False, col_and_rows=3):
    ''' 
    ''' 
    num = col_and_rows**2  #the total amount of numbers in the tic_tac_toe
    # if anything happens, I'll use conditionals for the rows and stuff
    # for number in range(1, num+1):  
    #     tic_tac.append(number)  #appending the total numbers in a list
    

    '''this function is to intersperse between the x's and the o's'''
    numbers_square = tic_tac
    module = 0    #This is where the numbers start to count between 0 and 1. 
    while (module != 9) and game_status == False:
        if user_turn in tic_tac and (module % 2) == 0:  # if the the number is in the lisst and the module is 0...
            tic_tac[user_turn] = "x"   # → the number that the user typed is gona have the x simbol
            tic_tac.append(user_turn)   # and append it to the list of TIC_TAC_TOE
            module += 1    # adding the one every time it completes the round
            if game_status == True: # breaking the loop if there is a winner 
                break

        elif user_turn in tic_tac and (module % 2) == 1:    # if the the number is in the lisst and the module is 1...
            tic_tac[user_turn] = "o"  # → the number that the user typed is gona have the o simbol
            tic_tac.append(user_turn)   # and append it to the list of TIC_TAC_TOE
            module += 1  # adding the one every time it completes the round
            if game_status == True:   # breaking the loop if there is a winner 
                break
        # print(number, end=" ")   #
    
    '''
    if user_simbol in tic_tac:
        tic_tac[user_simbol] = "x"
        tic_tac.append(user_simbol)
    

        # print(number, end=" ")   #
    '''
    print()

    # print(tic_tac)
    print("down here printing the list items:")
    for i in range(1, num+1):   #This loop is for the printing of the table and jumping to another column
        print(tic_tac[i], end=" ")  #iterating through each item of the list 

        for j in range(0, num+1):  #this loop is for the number of items it has to count in order to jump to the other row.
            # The thing here is that the "j" is to iterate in the number of rows: every time it multiplies a multiple of the square root of the number of places it'l jump to the other.   
            if i == (col_and_rows * j):
                print()
    
        
    
    

    def amount_of_simbols():
        '''this is going to be if the user types a different number of columns and rows'''
        

    



main()

