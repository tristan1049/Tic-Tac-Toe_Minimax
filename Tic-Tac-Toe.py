import time
import sys
import os

def status(board):
    """
    board: A list of string symbol representations of a tic-tac-toe board
    
    return: 1 if X wins, -1 if O wins, 0 if draw
    """
    diag1 = board[0] + board[4] + board[8]              #Check for diagonals
    diag2 = board[2] + board[4] + board[6]
    
    if diag1 == "XXX" or diag2 == "XXX":
        return 1
    elif diag1 == "OOO" or diag2 == "OOO":
        return -1
    
    
    
    for i in range(3):                                  #Check for rows and columns
        row = ""
        col = ""
        
        for j in range(3):
            row += board[3*i + j]
            col += board[i + 3*j]
            
        if row == "XXX" or col == "XXX":
            return 1
        elif row == "OOO" or col == "OOO":
            return -1
    
    
    
    if '_' not in board:                                #Check for draw condition
        return 0
    
    
def render(board):
    """
    board: A list of string symbol representations of a tic-tac-toe board
    
    Prints out a visual representation of the tic-tac-toe board given
    """
    print()
    for i in range(3):
        print(' {} | {} | {} '.format(board[3*i], board[3*i+1], board[3*i+2]))
        
        if i != 2:
            print('-----------')
    print()
    
    
    
def minimax(board, player, enemy = 'O', player_turn = True):
    """
    board: A list of string symbol representations of a tic-tac-toe board
    player: A string representation of the player to find the best move for
    enemy: A string representation of the enemy to try and beat
    player_turn: A boolean of whether a given board is the player's turn or not
    
    return: Index of the best move for the symbol given and the value
    """
    stat = status(board)
    if stat != None:
        return None, stat
    
    value = None                                #Initialize best value and index to None
    index = None
    
    for spot in range(len(board)):              #For each spot, try to minimax
            
        if board[spot] == '_':                  #If open spot, place player or enemy symbol
            if player_turn:
                board[spot] = player
            else:
                board[spot] = enemy
                
                
                
            if player_turn:                     #If player's turn, recurse for opponent, check for max
                best_move, spot_value = minimax(board, player, enemy, False) 
                    
                if value != None:           #Check if value of spot is better than current for player
                    if spot_value > value:
                        value, index = spot_value, spot
                else:
                    value, index = spot_value, spot

            else:                               #If opponent's turn, recurse for player, check for min
                best_move, spot_value = minimax(board, player, enemy) 
                
                if value != None:           #Check if value of spot is better than current for enemy
                    if spot_value < value:
                        value, index = spot_value, spot
                else:
                    value, index = spot_value, spot
                        
                        
                        
                        
            board[spot] = '_'                   #Reset the square if changed
            
            
    return index, value                         #Return max/min value with index
        




def clear():
    """
    Clears the system properly to avoid bugs with inputs
    """
    sys.stdout.flush()
    os.system('clear')
    

def inp(s = ''):
    """
    Properly calls input function to avoid bugs
    """
    sys.stdout.flush()
    return input(s)
    
    

def player_turn(board, player):
    """
    board: A list of string symbol representations of a tic-tac-toe board
    player: Symbol representing the player
    
    Renders the tic-tac-toe board and allows for a player to choose 
    a square to play
    
    return: A modified board based on what the player chose
    """
    clear()
    render(board)                   #Render the board visually for the player to see
    
    print('Make a move!')           #Give player options for move
    print('For a row, type either Top, Middle, or Bottom')
    print('For a column, type either Left, Center, or Right')
    
    row = inp('Row: ').lower().strip()                  #Take in player's input for a move
    col = inp('Column: ').lower().strip()
    
    
    
    i, j = None, None
    
    if row == 'top':                            #Interpret player's input and convert to indexing tools
        i = 0
    elif row == 'middle':
        i = 1
    elif row == 'bottom':
        i = 2
        
    
    if col == 'left':
        j = 0
    elif col == 'center':
        j = 1
    elif col == 'right':
        j = 2

    
    if i == None or j == None:                  #If input not understood, try again
        print()
        print('Not a valid input! Try again!')
        time.sleep(2)
        
        player_turn(board, player)
        return
    
    
    index = 3*i + j                             #Index found using row and column numbers
    
    if board[index] != '_':                     #If square has a piece, try again
        print()
        print('Square already has a piece on it! Try again!')
        time.sleep(2)
        
        player_turn(board, player)
        return
    
    
    board[index] = player                       #If square is empty, place player's piece on square, render
    clear()
    render(board)
    
    stat = status(board)                        #Check if the player won on this turn
    if stat != None:
        if stat == 0:
            time.sleep(1)
            print('You drew against the computer! Try again!')
            return stat
            
        time.sleep(1)
        print('Congrats!! You beat the computer!')
        return stat
    
    
    
    
    
def computer_turn(board, piece):
    """
    board: A list of string symbol representations of a tic-tac-toe board
    piece: Symbol representing the computer's pieces
    
    renders a modified board with the computer's move given a board and
    piece to play
    """
    time.sleep(0.5)
    print("Computer is thinking!")                  #Give time for player to comprehend outputs
    time.sleep(2)
    clear()
    
    if piece == 'X':            #Use minimax to find best move for either X or O
        best_move, value = minimax(board, 'X', 'O')           
    else:
        best_move, value = minimax(board, 'X', 'O', False)   
        
        
    board[best_move] = piece                    #Modify square on board to have piece
    render(board)                               #Render the visuals for the board
    
    print('The computer made a move!!')
    
    
    stat = status(board)
    if stat != None:
        if stat == 0:
            time.sleep(1)
            print('You drew against the computer! Try again!')
            return stat
            
        time.sleep(1)
        print('The computer wins! Better luck next time!')
        return stat
    
    
    
    
def play_game(board):
    """
    board: A list of string symbol representations of a tic-tac-toe board
    
    Play a game playing the computer at tic-tac-toe
    """
    clear()
    print()
    print('Welcome to Tic-Tac-Toe! Try your best against the computer!')        #Make an intro to the game
    
    player_piece = inp("Do you want to play as X or O: ").lower().strip()       #Ask player which piece to play
    time.sleep(1)
    
    if player_piece not in  ['x', 'o']:                  #If not a valid piece, try again
        print()
        print('Not a valid piece! Try again!')
        time.sleep(1)
        play_game(board)
        return
        
    
    while True:                     #Keep playing turns until game is over
        if player_piece == 'x':                     #If player is X, they go first 
            if player_turn(board, 'X') != None:                
                return
            if computer_turn(board, 'O') != None:
                return
            
        elif player_piece == 'o':                   #If player is O, they go second
            if computer_turn(board, 'X') != None:
                return
            if player_turn(board, 'O') != None:
                return

    
    
    
if __name__ == '__main__':
    board = ['_', '_', '_', 
             '_', '_', '_', 
             '_', '_', '_']
    
    play_game(board)
