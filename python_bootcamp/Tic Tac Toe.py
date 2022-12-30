#!/usr/bin/env python

# Thank you for your interest in reading my code
# This is my first ever fully functional program in any language
# So it may not be the most clean & efficient code, but it works
# I'm very much still learning so my abilities & knowledge will grow in time

# You can connect with me on most popular social media platforms or by going to my website
# @KyserClark
# KyserClark.com

# function to show current game board to players
def display_board():
    game_board = f'\n\n |     |     |     |\n |  {cell_list[6]}  |  {cell_list[7]}  |  {cell_list[8]}  |\n |     |     |     |\n  _________________\n\n |     |     |     |\n |  {cell_list[3]}  |  {cell_list[4]}  |  {cell_list[5]}  |\n |     |     |     |\n  _________________\n\n |     |     |     |\n |  {cell_list[0]}  |  {cell_list[1]}  |  {cell_list[2]}  |\n |     |     |     |\n\n'
    print(game_board)

# function to start the game
def game_start():
    
    introduction = "\nWelcome to Kyser Clark's Tic Tac Toe Game!!\nPush ctrl + c to quit at anytime"
    
    print(introduction)
    
    global cell_list
    
    cell_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    global player1_letter
    global player2_letter
    
    player1_letter = 'letter not selected'
    player2_letter = 'letter not selected'
    
    while player1_letter not in ['X','O']:
        player1_letter = input("\nPlayer 1, will you be X's or O's?  ").upper()
        if player1_letter not in ['X','O']:
            print('\nInvalid input: Please select X or O: \n')
            
    if player1_letter == 'O':
        player2_letter = 'X'
    else:
        player2_letter = 'O'
    
    print(f'\nPlayer 1 is {player1_letter}\nPlayer 2 is {player2_letter}\n')
    
    
    global turn_selection
    
    turn_selection = 'Not Selected'
    
    while turn_selection not in ['1','2']:
        turn_selection = input('Who will go first? Player 1 or Player 2? ')
        if turn_selection not in ['1','2']:
            print('\nInvalid input: Please select 1 or 2: \n')
            
    print('\nThe game board cell numbers reference a standard numpad like this: ')
    # displays the reference board so players know what number equates to each cell
    print(f'\n\n |     |     |     |\n |  {7}  |  {8}  |  {9}  |\n |     |     |     |\n  _________________\n\n |     |     |     |\n |  {4}  |  {5}  |  {6}  |\n |     |     |     |\n  _________________\n\n |     |     |     |\n |  {1}  |  {2}  |  {3}  |\n |     |     |     |\n\n')
            
    if turn_selection == '1':
        player1_turn()
        
    if turn_selection == '2':
        player2_turn()
            
# function to start player 1's next turn                
def player1_turn():
    
    global cell_list
    global player1_choice
    
    player1_choice = 'Not Selected'
    
    display_board()
    
    while player1_choice not in ['1','2','3','4','5','6','7','8','9']:
        player1_choice = input(f"Player 1, which cell would you like to place an {player1_letter} on? ")
        if player1_choice not in ['1','2','3','4','5','6','7','8','9']:
            print('\nThat is not a valid choice, please select an empty cell number \n\n')
    if player1_choice in ['1','2','3','4','5','6','7','8','9']:
        player1_selection()

# function to start player 2's next turn
def player2_turn():
    
    global cell_list
    global player2_choice
    
    player2_choice = 'Not Selected'
    
    display_board()
    
    while player2_choice not in ['1','2','3','4','5','6','7','8','9']:
        player2_choice = input(f"Player 2, which cell would you like to place an {player2_letter} on? ")
        if player2_choice not in ['1','2','3','4','5','6','7','8','9']:
            print('\nThat is not a valid choice, please select an empty cell number \n\n')
    if player2_choice in ['1','2','3','4','5','6','7','8','9']:
        player2_selection()

# funtion to check for win conditions after player 1's turn. If win conditons are not met, begin player 2's turn
def player1_win_conditions():
    
    player1_condition = 'Not Met'
    
    if cell_list[0:3] == [f'{player1_letter}', f'{player1_letter}', f'{player1_letter}']:
        player1_condition = 'Met'
    
    elif cell_list[3:6] == [f'{player1_letter}', f'{player1_letter}', f'{player1_letter}']:
        player1_condition = 'Met'
        
    elif cell_list[6:10] == [f'{player1_letter}', f'{player1_letter}', f'{player1_letter}']:
        player1_condition = 'Met' 
        
    elif cell_list[0:8:3] == [f'{player1_letter}', f'{player1_letter}', f'{player1_letter}']:
        player1_condition = 'Met' 
        
    elif cell_list[1:9:3] == [f'{player1_letter}', f'{player1_letter}', f'{player1_letter}']:
        player1_condition = 'Met'
        
    elif cell_list[2:10:3] == [f'{player1_letter}', f'{player1_letter}', f'{player1_letter}']:
        player1_condition = 'Met'
        
    elif cell_list[0:10:4] == [f'{player1_letter}', f'{player1_letter}', f'{player1_letter}']:
        player1_condition = 'Met' 
        
    elif cell_list[2:8:2] == [f'{player1_letter}', f'{player1_letter}', f'{player1_letter}']:
        player1_condition = 'Met'
        
    elif ' ' in cell_list:
        player2_turn()
    
    else: 
        print("\n\nIT'S A CATS GAME. Meow!!! ")
        play_again()
    
    if player1_condition == 'Met':
        display_board()
        print(f'\n\n{player1_letter*3}  PLAYER 1 WINS!!!  {player1_letter*3}')
        play_again()
        
# funtion to check for win conditions after player 2's turn. If win conditons are not met, begin player 1's turn        
def player2_win_conditions():
    
    player2_condition = 'Not Met'
    
    if cell_list[0:3] == [f'{player2_letter}', f'{player2_letter}', f'{player2_letter}']:
        player2_condition = 'Met'
    
    elif cell_list[3:6] == [f'{player2_letter}', f'{player2_letter}', f'{player2_letter}']:
        player2_condition = 'Met'
        
    elif cell_list[6:10] == [f'{player2_letter}', f'{player2_letter}', f'{player2_letter}']:
        player2_condition = 'Met' 
        
    elif cell_list[0:8:3] == [f'{player2_letter}', f'{player2_letter}', f'{player2_letter}']:
        player2_condition = 'Met' 
        
    elif cell_list[1:9:3] == [f'{player2_letter}', f'{player2_letter}', f'{player2_letter}']:
        player2_condition = 'Met'
        
    elif cell_list[2:10:3] == [f'{player2_letter}', f'{player2_letter}', f'{player2_letter}']:
        player2_condition = 'Met'
        
    elif cell_list[0:10:4] == [f'{player2_letter}', f'{player2_letter}', f'{player2_letter}']:
        player2_condition = 'Met' 
        
    elif cell_list[2:8:2] == [f'{player2_letter}', f'{player2_letter}', f'{player2_letter}']:
        player2_condition = 'Met'
        
    elif ' ' in cell_list:
        player1_turn()
    
    else: 
        print("\n\nIT'S A CATS GAME. Meow!!! ")
        play_again()
    
    if player2_condition == 'Met':
        display_board()
        print(f'\n\n{player2_letter*3}  PLAYER 2 WINS!!!  {player2_letter*3}')
        play_again()

# function to ask players if they want to play again after win conditons are met 
def play_again():
    
    play_again_selection = 'Not Selceted'
    
    while play_again_selection not in ['y','n']:
        play_again_selection = input('\n\nWould you like to play again? y or n: ').lower()
        if play_again_selection not in ['y', 'n']:
            print('\n\nInvalid Input, please select y or n\n\n')
            
    if play_again_selection == 'y':
        game_start()
        
    else:
        print('\n\nThank you for playing! :) ')
        quit()

# function that cycles through all possible options for player 2's cell choice from player2_turn. If choice is valid, check for win conditions. If choice is not valid, restart player 2's turn
def player2_selection():
    
    global player2_choice
    
    if player2_choice == "1":

        if cell_list[0] == ' ':

            cell_list[0] = player2_letter
            player2_choice = 'Score'

            
    elif player2_choice == "2":

        if cell_list[1] == ' ':

            cell_list[1] = player2_letter
            player2_choice = 'Score'

        
    elif player2_choice == "3":

        if cell_list[2] == ' ':

            cell_list[2] = player2_letter
            player2_choice = 'Score'

       
    elif player2_choice == "4":

        if cell_list[3] == ' ':

            cell_list[3] = player2_letter
            player2_choice = 'Score'

                      
    elif player2_choice == "5":

        if cell_list[4] == ' ':

            cell_list[4] = player2_letter
            player2_choice = 'Score'

            
    elif player2_choice == "6":

        if cell_list[5] == ' ':

            cell_list[5] = player2_letter
            player2_choice = 'Score'

                
    elif player2_choice == "7":

        if cell_list[6] == ' ':

            cell_list[6] = player2_letter
            player2_choice = 'Score'


    elif player2_choice == "8":

        if cell_list[7] == ' ':

            cell_list[7] = player2_letter
            player2_choice = 'Score'
            
                
    elif player2_choice == "9":

        if cell_list[8] == ' ':

            cell_list[8] = player2_letter
            player2_choice = 'Score'
            
    
    if player2_choice == 'Score':
        player2_win_conditions()
        
    elif player2_choice not in ['1','2','3','4','5','6','7','8','9']:
        print('\n\nPlease select a valid cell 1-9: \n')
        player2_turn()
        
    elif player2_choice != 'Score':
        print('\n\nThat Cell is taken, please choose an empty cell: \n')
        player2_turn()

# function that cycles through all possible options for player 1's cell choice from player1_turn. If choice is valid, check for win conditions. If choice is not valid, restart player 1's turn
def player1_selection():
    
    global player1_choice
    
    if player1_choice == "1":

        if cell_list[0] == ' ':

            cell_list[0] = player1_letter
            player1_choice = 'Score'

            
    elif player1_choice == "2":

        if cell_list[1] == ' ':

            cell_list[1] = player1_letter
            player1_choice = 'Score'

        
    elif player1_choice == "3":

        if cell_list[2] == ' ':

            cell_list[2] = player1_letter
            player1_choice = 'Score'

       
    elif player1_choice == "4":

        if cell_list[3] == ' ':

            cell_list[3] = player1_letter
            player1_choice = 'Score'

                      
    elif player1_choice == "5":

        if cell_list[4] == ' ':

            cell_list[4] = player1_letter
            player1_choice = 'Score'

            
    elif player1_choice == "6":

        if cell_list[5] == ' ':

            cell_list[5] = player1_letter
            player1_choice = 'Score'

                
    elif player1_choice == "7":

        if cell_list[6] == ' ':

            cell_list[6] = player1_letter
            player1_choice = 'Score'


    elif player1_choice == "8":

        if cell_list[7] == ' ':

            cell_list[7] = player1_letter
            player1_choice = 'Score'
            
                
    elif player1_choice == "9":

        if cell_list[8] == ' ':

            cell_list[8] = player1_letter
            player1_choice = 'Score'
            
    
    if player1_choice == 'Score':
        player1_win_conditions()
        
    elif player1_choice not in ['1','2','3','4','5','6','7','8','9']:
        print('\n\nPlease select a valid cell 1-9: \n')
        player1_turn()
        
    elif player1_choice != 'Score':
        print('\n\nThat Cell is taken, please choose an empty cell: \n')
        player1_turn()

# runs the game_start function that begins the game
game_start()
