
def main():
    dir = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    dipslay_menu()
    start = start_question()
    while start == True:
        subsequence = choose_first_player()
        start = play_game(subsequence, dir)
        

def dipslay_menu():
    print('This is a program to provide 2 users playing the tic-tac-toe game.\n' +
            'Firstly users must choose who make a step first.\n' +
            'To make choise each of users can use the following rule:\n' +
            'Game field is lattice 3x3 cells. To make choise user should enter\n' +
            'a wished number of cell and press Enter. An instanse of such a lattice\n' +
            'givven next:.---.---.---.\n' +
            '            | 7 | 8 | 9 |\n'+
            '            .---.---.---.\n' +
            '            | 4 | 5 | 6 |\n' +
            '            .---.---.---.\n' +
            '            | 1 | 2 | 3 |\n' +
            '            .---.---.---.\n')
    print('If you are ready let\'s start the game! And may the best user win!')
    

def start_question():
    choise = 'WRONG'
    while choise not in ['Y', 'N']:
        choise = input('If you are ready to start a new game enter Y to start or N to stop and press Enter: ')
        if choise.upper() not in ['Y', 'N']:
            print('Sorry, your choise isn\'t correct. Please make the right choise.')
            continue
        if choise.upper()=='Y':
            return True
        else:
            return False
        
def choose_first_player():
    print('To start playing we should choose who will play by X and who O.')
    answer = False
    while answer != True:
        ask = input('Enter the simbol which you want to play in the game. You can choose X or O: ')
        if ask.upper() == 'X':
            print('The player 1 game with X, the player 2 game with O.')
            answer = True
            return {0:'X', 1:'O'}
        elif ask.upper() == 'O':
            print('The player 2 game with X, the player 1 game with O.')
            answer = True
            return {1:'X', 0:'O'}
        else:
            answer = False
            
def show_lattice_cells(dir):
    print('            .---.---.---.\n' +
         f'            | {dir[7]} | {dir[8]} | {dir[9]} |\n'+
          '            .---.---.---.\n' +
         f'            | {dir[4]} | {dir[5]} | {dir[6]} |\n' +
          '            .---.---.---.\n' +
         f'            | {dir[1]} | {dir[2]} | {dir[3]} |\n' +
          '            .---.---.---.')

def play_game(players, dir):
    win = False
    if players[0]=='X':
        play = 0
        play1 = 'X'
        play2 = 'O'
    elif players[0]=='O':
        play = 1
        play2 = 'X'
        play1 = 'O'
    show_lattice_cells(dir)
    while win!=True:
        if play == 0:
            print('Player 1 make his next step.')
            step = ask_next_step()
            dir[step] = play1
            play = 1
        else:
            print('Player 2 make his next step.')
            step = ask_next_step()
            dir[step] = play2
            play = 0
        show_lattice_cells(dir)
        result = check_win(dir)
        if result =='':
            win = False
        else:
            res_list = list(result)
            if (res_list[1])[1]=='X':
                if players[0]=='X':
                    print('Congratulation! User 1 won!')
                else:
                    print('Congratulation! User 2 won!')
                win = True
            elif (res_list[1])[1]=='O':
                if players[0]=='O':
                    print('Congratulation! User 1 won!')
                else:
                    print('Congratulation! User 2 won!')
                win = True
                return False
            
                                
def ask_next_step():
    re_ask = True
    right_list = ['1','2','3','4','5','6','7','8','9']
    while re_ask==True:
        answer = input('Please enter a number of cell where you want to go. Enter the number from 1 to 9: ')
        if answer.isdigit()==True:  
            if answer not in right_list:
                print('You entered the wrong number. Please try again.')
                re_ask = True
            else:
                re_ask = False
                return int(answer)
        else:
            print('You entered not a number. Please enter the right item.')
            re_ask = True

def check_win(dir):
    set_list = [{'1X','4X','7X'}, {'2X','5X','8X'}, {'3X','6X','9X'}, {'1X','2X','3X'},
            {'4X','5X','6X'}, {'7X','8X','9X'}, {'1X','5X','9X'}, {'3X','5X','7X'},
            {'1O','4O','7O'}, {'2O','5O','8O'}, {'3O','6O','9O'}, {'1O','2O','3O'},
            {'4O','5O','6O'}, {'7O','8O','9O'}, {'1O','5O','9O'}, {'3O','5O','7O'}]
    list = []
    for key,value in dir.items():
        list.append(str(key)+value)
    set_l = set(list)
    for item in set_list:
        if (set.intersection(set_l, item))==item:
            return item
    else:
        return ''
        

if __name__ == '__main__':
    main()