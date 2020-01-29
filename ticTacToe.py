'''
board
display board
play game
handle turn
check win
  check row
  check column
  check diagonal
check tie
flip player

'''

#game board
board = ['-','-','-','-','-','-','-','-','-',]

#if game is still going
game_still_going = True

#who is the winner? or if tied?
winner = None

#player's turn
current_player = 'X'

#to keep count
count = 0

def set_symbol():
    symbol = input("enter symbol of player 1..(X\O)")
    if symbol=="X" or symbol == "O":
        global current_player
        current_player = symbol
        
    else:
        print("You did not choose from the choice, now play with default settings.")
        

        
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8])

def handle_turn(player):
    position = input("choose the position from 1-9 ")
    position = int(position)-1
    if position>9:
        print("you made a wrong choice")
    else:
        if board[position]=="-":
           global count
           count += 1
           board[position] = player
           display_board()
        else:
             print("position is already acquired!!! ")

def flip_players():
    global current_player
    if current_player=='X':
           current_player = "O"
    elif current_player=='O':
           current_player = "X"
    
def checkRows():
    if board[0]==board[1]==board[2]==current_player or board[3]==board[4]==board[5]==current_player or board[6]==board[7]==board[8]==current_player:
        return True
    else:
        return False

def checkColumns():
    if board[0]==board[3]==board[6]==current_player or board[1]==board[4]==board[7]==current_player or board[2]==board[5]==board[8]==current_player:
        return True
    else:
        return False

def checkDiagonals():
    if board[0]==board[4]==board[8]==current_player or board[2]==board[4]==board[6]==current_player:
        return True
    else:
        return False

def check_if_win():
    winR = checkRows()
    winC = checkColumns()
    winD = checkDiagonals()
    if winC or winR or winD:
        print("game end--------------------------------------------------------")
        global game_still_going
        game_still_going = False
        global winner
        winner = current_player
    

def check_if_tie():
    if count >=9:
        global game_still_going
        game_still_going = False
        

def check_if_game_over():
    check_if_win()
    check_if_tie()

def play_game():
    display_board() #displays the board

    
    while game_still_going:
          handle_turn(current_player)
          check_if_game_over()
          if game_still_going:
              flip_players()
          
          
    if winner=='X' or winner=='O':
        print('WINNER IS '+winner)
    else:
        print("TIE")

          
set_symbol()
play_game()
    

