
def main():
     
    dipslay_menu()
    

def dipslay_menu():
    print('This is a program to provide 2 users playing the tic-tac-toe game.\n' +
          'Firstly users must choose who make a step first.\n' +
          'To make choise each of users can use the following rule:\n' +
          'Game field is lattice 3x3 cells. To make choise user should enter\n' +
          'a wished number of cell and press Enter. An instanse of such a lattice\n' +
          'givven next:| 7 | 8 | 9 |\n'+
          '             --- --- ---\n' +
          '            | 4 | 5 | 6 |\n' +
          '             --- --- ---\n' +
          '            | 1 | 2 | 3 |')
    print('If you are ready let\'s start the game! And may the best user win!')
    

def start_question():
    pass



if __name__ == '__main__':
    main()