

tictactoe = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def main():
    '''here it all depends in the mod 2: if it is 0 result, 
    it's the x's turn. If it is a 1 result it's o's turn'''
    value = 0
    a_winner = False    
    while value != 9:
        module = value % 2
        a_winner = winner(tictactoe)
        if a_winner == True:
            break
        printing_tic_tac()   #printing the table to see the marks in the tic tac toe
        if module == 0:
            user_turn = int(input("X's turn. Enter a number(1-9): "))
            print()

        elif module == 1:
            user_turn = int(input("O's turn. Enter a number(1-9): "))
            print()

        append_simbol(user_turn, module)   
        
        value += 1
        

    printing_tic_tac()
    if a_winner == True:   
        print("We have a winner!! Good Game y'all")
    else:
        print("Nice! Equal power!")
    
def printing_tic_tac():
    ''''''
    for i in range(1, 9+1):   #This loop is for the printing of the table and jumping to another column
            print(tictactoe[i], end=" ")  #iterating through each item of the list 

            for j in range(0, 9+1):  #this loop is for the number of items it has to count in order to jump to the other row.
                # The thing here is that the "j" is to iterate in the number of rows: every time it multiplies a multiple of the square root of the number of places it'l jump to the other.   
                if i == (3 * j):
                    print()

def append_simbol(user_turn, module):
    ''''''
    if (user_turn in tictactoe) and user_turn != 0 and module == 0:
        tictactoe[user_turn] = "\033[2;32;40mx\033[0;37;40m"
    
    elif (user_turn in tictactoe) and user_turn != 0 and module == 1:
        tictactoe[user_turn] = "\033[1;35;40mo\033[0;37;40m"
    
    else:
        print("Sorry... but the program will run again")
                
        
        

def winner(table_list):
    """This is the functio where I iterate through 
    the table to search for the results of the tic_tac_toe"""
    if  table_list[1] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[2] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[3] == "\033[2;32;40mx\033[0;37;40m" or \
        \
        table_list[4] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[5] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[6] == "\033[2;32;40mx\033[0;37;40m" or \
        \
        table_list[7] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[8] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[9] == "\033[2;32;40mx\033[0;37;40m" or \
        \
        table_list[1] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[4] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[7] == "\033[2;32;40mx\033[0;37;40m" or \
        \
        table_list[2] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[5] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[8] == "\033[2;32;40mx\033[0;37;40m" or \
        \
        table_list[3] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[6] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[9] == "\033[2;32;40mx\033[0;37;40m" or \
        \
        table_list[1] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[5] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[9] == "\033[2;32;40mx\033[0;37;40m" or \
        \
        table_list[3] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[5] == "\033[2;32;40mx\033[0;37;40m" and \
        table_list[7] == "\033[2;32;40mx\033[0;37;40m":
        return True 

    elif  table_list[1] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[2] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[3] == "\033[1;35;40mo\033[0;37;40m" or \
        \
        table_list[4] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[5] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[6] == "\033[1;35;40mo\033[0;37;40m" or \
        \
        table_list[7] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[8] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[9] == "\033[1;35;40mo\033[0;37;40m" or \
        \
        table_list[1] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[4] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[7] == "\033[1;35;40mo\033[0;37;40m" or \
        \
        table_list[2] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[5] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[8] == "\033[1;35;40mo\033[0;37;40m" or \
        \
        table_list[3] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[6] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[9] == "\033[1;35;40mo\033[0;37;40m" or \
        \
        table_list[1] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[5] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[9] == "\033[1;35;40mo\033[0;37;40m" or \
        \
        table_list[3] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[5] == "\033[1;35;40mo\033[0;37;40m" and \
        table_list[7] == "\033[1;35;40mo\033[0;37;40m":
        return True 

    else:
        return False



# user_list_x = []
# user_x = int(input("Type the number: "))
# user_list_x.append(user_x)



# user_list_o = []
# user_o = int(input("Type the number: "))
# user_list_o.append(user_o)

main()









