from IPython.display import clear_output
import random
player1=''
player2=''
player1_marker=''
player2_marker=''
marker=''
choice=0
def take_names():
    player1=input("Enter player1's name: ")
    player2=input("Enter player2's name: ")
    return [player1,player2]
def choose_marker():
    x=random.randint(0,200)
    if x%2==0:
        player=input(f"{player1} which marker you want 'X' or 'O' ")
        while player!='X' and player!='O':
            print("Wrong marker entered. Re-enter it.")
            player=input(f"{player1} which marker you want 'X' or 'O' ")
        player1_marker=player
        if player1_marker=='X':
            player2_marker='O'
        else:
            player2_marker='X'
        return [player1_marker,player2_marker]
    else:
        player=input(f"{player2} which marker you want 'X' or 'O' ")
        while player!='X' and player!='O':
            print("Wrong marker entered. Re-enter it.")
            player=input(f"{player2} which marker you want 'X' or 'O' ")
        player2_marker=player
        if player2_marker=='X':
            player1_marker='O'
        else:
            player1_marker='X'
def display_board(board):
    clear_output()
    print("     "+"|"+"     "+"|"+"     ")
    print("  "+board[7]+"  "+"|"+"  "+board[8]+"  "+"|"+"  "+board[9]+"  ")
    print("_____"+"|"+"_____"+"|"+"_____")
    print("     "+"|"+"     "+"|"+"     ")
    print("  "+board[4]+"  "+"|"+"  "+board[5]+"  "+"|"+"  "+board[6]+"  ")
    print("_____"+"|"+"_____"+"|"+"_____")
    print("     "+"|"+"     "+"|"+"     ")
    print("  "+board[1]+"  "+"|"+"  "+board[2]+"  "+"|"+"  "+board[3]+"  ")
    print("     "+"|"+"     "+"|"+"     ")
def choose_first():
    x=random.randint(0,100)
    if x%2==0:
        return 'player1'
    else:
        return 'player2'
def space_check(board, position):
    if board[position]=='X' or board[position]=='O':
        return False
    else:
        return True
def full_board_check(board):
    count=0
    for x in range(1,10):
        if board[x]=='X' or board[x]=='O':
            count+=1
    return count==9
def player_choice(board):
    position=int(input('Enter position to place marker: '))
    if space_check(board,position):
        return position
    else:
        print('Wrong position entered Re-enter position')
        player_choice(board)
def win_check(board, mark):
    if board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark:
        return True
    elif board[7]==mark and board[8]==mark and board[9]==mark:
        return True
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    elif board[3]==mark and board[6]==mark and board[9]==mark:
        return True
    elif board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    elif board[3]==mark and board[5]==mark and board[7]==mark:
        return True
    else:
        return False
def replay():
    p=input("Want to play again?'yes' or 'no' ")
    if p=='yes':
        return True
    else:
        return False
print("....!!! Welcome To Tic Tac Toe Game !!!....")
while True:
    game_on=True
    count=0
    board=[' ']*10
    p=take_names()
    player1=p[0]
    player2=p[1]
    p=choose_marker()
    player1_marker=p[0]
    player2_marker=p[1]
    name=choose_first()
    choice=0
    while game_on:
        if count%2==0:
            if name=='player1':
                marker=player1_marker
                print(f"{player1.capitalize()}'s Turn....... ")
            else:
                marker=player2_marker
                print(f"{player2.capitalize()}'s Turn....... ")
            choice=player_choice(board)
            board[choice]=marker
            display_board(board)
            if win_check(board,marker):
                if name=='player1':
                    print(f"Congratulations {player1.capitalize()} Won.....")
                    game_on=False
                else:
                    print(f"Congratulations {player2.capitalize()} Won.....")
                    game_on=False
            if full_board_check(board):
                  if game_on==True:
                        print(" Match is draw ")
                        game_on=False
            count+=1
        else:
            if name=='player1':
                marker=player2_marker
                print(f"{player2.capitalize()}'s Turn....... ")
            else:
                marker=player1_marker
                print(f"{player1.capitalize()}'s Turn....... ")
            choice=player_choice(board)
            board[choice]=marker
            display_board(board)
            if win_check(board,marker):
                if name=='player1':
                    print(f"Congratulations {player2.capitalize()} Won.....")
                    game_on=False
                else:
                    print(f"Congratulations {player1.capitalize()} Won.....")
                    game_on=False
            if full_board_check(board):
                  if game_on==True:
                        print(" Match is draw ")
                        game_on=False
            count+=1
    if not replay():
        break      