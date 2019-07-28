from IPython.display import clear_output
def display_board(board):
    
    print(board[7]+ '|'+board[8]+ '|'+board[9])
    print("-----")
    print(board[4]+ '|'+board[5]+ '|'+board[6])
    print("-----")
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board=[' ']*10
display_board(test_board)

def player_input():
    marker=''
    while  not(marker=='X' or marker=='O'):
        marker=input("enter your choice?: x or o:").upper()
    if(marker=='X'):
        return('X','O')
    else:
        return('O','X')
        

    #player1_marker,player2_marker=player_input()



def place_marker(board,marker,position):
    board[position]=marker

place_marker(test_board,'@',5)
display_board(test_board)

def win_check(board,mark):
    return ((board[3]==mark and board[2]==mark and board[1]==mark )or #across the line
    ( board[4]==mark and board[5]==mark and board[6]==mark) or  #across the line
    ( board[7]==mark and board[8]==mark and board[9]==mark) or #across the line
    ( board[1]==mark and board[4]==mark and board[7]==mark ) or #across the column
    ( board[3]==mark and board[6]==mark and board[9]==mark ) or #across the column
    ( board[1]==mark and board[5]==mark and board[9]==mark) or #diagonal
    ( board[3]==mark and board[5]==mark and board[7]==mark ))  #diagonal

    win_check(test_board,'X')

import random
def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'player1'
    else:
        return 'player2'
    

def space_check(board,position):
    return board[position]  ==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i): 
            return False
    return True    

def player_choice(board):
    position=0
    while  position not in [1,2,3,4,5,6,7,8,9] and not space_check(board,position):
        position=int(input("Enter your choice number:(1-9)"))
    return position
def replay():
    choice=input("YOU want to play? yes or NO:")
    return choice=='yes'

# writing the tic toc toe game 
print("Welcome to tic toc toe ")
while True:
    the_board=[' ']*10 
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+"will go first")
    play_game =input ('ready to play ? yes or not')
    if  play_game=='yes':
        game_on=True
    else:
        game_on=False
        
    while game_on :
        if turn =='player1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("player1 has won the game ")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game")
                    game_on=False
                else:
                    turn ='player2'
        else:   
            if turn =='player2':
                display_board(the_board )
                position=player_choice(the_board)
                place_marker(the_board,player2_marker,position)
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print("player2 has won the game ")
                    game_on=False
                else:
                     if full_board_check(the_board):
                        display_board(the_board)
                        print("Tie game")
                        game_on=False
                     else:
                        turn='player1'
    if not replay():
        break
    
