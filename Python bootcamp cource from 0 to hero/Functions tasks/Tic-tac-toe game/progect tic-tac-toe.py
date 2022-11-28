# Creating the main function
def main():
    # Display a start menu with short instructions and an instanse of game field look
    dipslay_menu()
    # Choose which player game with X or O simbol
    subsequence = choose_first_player()
    # Conferm of readiness for the game
    start = ask_question('start')
    # Start the game loop
    while start:
        game_field = ['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play_game(subsequence, game_field)
        # Ask a question about continue the game
        start = ask_question('continue')
        if start:
            subsequence = choose_first_player()
    print('It was nice to play this game with you. See you later.')
    
# Creating a function which shows the start explanation of the gane in the biggining.
def dipslay_menu():
    print('This is a program to provide 2 players playing the tic-tac-toe game.\n' +
            'To make choise each of users can use the following rule:\n' +
            'Game field is lattice 3x3 cells. To make choise user should enter\n' +
            'a wished number of cell and press Enter. An instanse of such a lattice\n' +
            'givven next:')
    # Show an instance of game field with number of cells.
    show_lattice_cells()
    print('')
    print('If you are ready let\'s start the game! And may the best user win!')
    
# Creating a function which ask player of starting or continue of the game.
def ask_question(argument):
    choise = 'WRONG'
    while choise not in ['Y', 'N']:
        if argument == 'start':
            choise = input('If you are ready to start a new game enter Y to start or N to stop and press Enter: ')
        if argument == 'continue':
            choise = input('Do you want to try playing again? Enter Y or N: ')
        if choise.upper() not in ['Y', 'N']:
            print('Sorry, your choise isn\'t correct. Please make the right choise.')
            continue
        if choise.upper()=='Y':
            return True
        else:
            return False
        
# Creating a function to choose whos player will start the game       
def choose_first_player():
    print('Firstly users must choose who make a step first.')
    print('To start playing we should choose who will play by X and who O.')
    answer = 'WRONG'
    while answer not in ['X', 'O']:
        answer = input('Player 1 should enter the simbol to start playing in the game. You can choose X or O: ')
        if answer.upper() not in ['X', 'O']:
            print('You entered the wrong item. Please enter the right item X or O.')
            continue
        if answer.upper() == 'X':
            print('The player 1 game with X, the player 2 game with O.')
            return ('X', 'O')
        else:
            print('The player 1 game with O, the player 2 game with X.')
            return ('O', 'X')
        
# Creating a function to display a current game field
# To display game field in the start menu we assign a default items.
def show_lattice_cells(list=['*','1','2','3','4','5','6','7','8','9']):
    print(' '*12 + '.---.---.---.\n' +
          ' '*12 + '| '+list[7]+' | '+list[8]+' | '+list[9]+' |\n'+
          ' '*12 + '.---.---.---.\n' +
          ' '*12 + '| '+list[4]+' | '+list[5]+' | '+list[6]+' |\n'+
          ' '*12 + '.---.---.---.\n' +
          ' '*12 + '| '+list[1]+' | '+list[2]+' | '+list[3]+' |\n'+
          ' '*12 + '.---.---.---.')
    
# Creating a function which consists of making users' steps, checking victory or tie 
# and displaying the result.
def play_game(players, field):
    continue_game = True
    player1, player2 = players
    if player1 == 'X':
        steps = 1 
    else:
        steps = 2
    while continue_game:
        for i in range(steps,11):       
            if i%2==0:
                field[make_step(field)] = player2 
                show_lattice_cells(field)
                print('Player 2 made turn.')
            else:
                field[make_step(field)] = player1
                print('Player 1 made turn.')
                show_lattice_cells(field)
            steps += 1
            # Check is any of players is won
            result = check_win(field)
            if result != '':
                #Show the game field with crossed out letters
                for item in result:
                    field[int(item[0])] = '*'
                show_lattice_cells(field)
                #Show the result of the game
                if result[0][1]=='X' and player1=='X':
                    print('Congratulation! User 1 won!')
                elif result[0][1]=='X' and player1=='O':
                    print('Congratulation! User 2 won!')
                elif result[0][1]=='O' and player1=='X':
                    print('Congratulation! User 2 won!')
                else:
                    print('Congratulation! User 1 won!')
                continue_game = False
                break
            # Check is the game can be continued or players gamed tie.
            is_tie = check_tie(field)
            if is_tie:
                print('It\'s a draw!')
                continue_game = False
                break
    
    
            
# Creating a function to input the correct number of cell in game fielf from user.
# We should also check that this cell is empty.                               
def make_step(field):
    empty_check = True
    while empty_check:
        choise = 'WRONG'
        right_choise = ['1','2','3','4','5','6','7','8','9']
        while choise not in right_choise:
            choise = input('Please enter a number of cell. Enter the number from 1 to 9: ')
            if choise.isdigit()==False:
                print('You entered not a number. Please enter the right item.')
                continue 
            if choise not in right_choise:
                print('You entered the wrong number. Please try again.')
        # Checking current cell is it empty
        empty_check = check_empty(int(choise), field)
        if empty_check:
            print(f'You choose an existed item in cell {choise}. Please enter number which hasn\'t existed yet.')
            continue
        else:
            return int(choise)
        
# Creating a function to check consist of cell.          
def check_empty(number, cells):
    if cells[number]!=' ':
        return True
    else:
        return False
        
# Creating a function to check has user already won yet.
def check_win(field):
    # Set of the right combination of victory.
    set_list = [{'1X','4X','7X'}, {'2X','5X','8X'}, {'3X','6X','9X'}, {'1X','2X','3X'},
                {'4X','5X','6X'}, {'7X','8X','9X'}, {'1X','5X','9X'}, {'3X','5X','7X'},
                {'1O','4O','7O'}, {'2O','5O','8O'}, {'3O','6O','9O'}, {'1O','2O','3O'},
                {'4O','5O','6O'}, {'7O','8O','9O'}, {'1O','5O','9O'}, {'3O','5O','7O'}]
    current_field = []
    for i in range(1, len(field)):
        current_field.append(str(i)+field[i])
    for item in set_list:
        if (set.intersection(set(current_field), item))==item:
            return list(item)
    else:
        return ''

# Creating a function to check is the result of the gami os tie
def check_tie(field):
    if ' ' not in field:
        return True
    else:
        return False

# Exsecute the main function
if __name__ == '__main__':
    main()