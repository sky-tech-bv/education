import sqlite3

def main():
    choice = 0 
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    while choice != 8:
        choice = get_menu()
        execute_choice(choice, cur)
    print('Program was shouted down.')
    con.close()
    
def display_menu():
    print('              MENU')
    print('1. Display cities sorted by population, ascending order')
    print('2. Display cities sorted by population, descending order')
    print('3. Display cities sorted by name')
    print('4. Display total population of all the cities')
    print('5. Display average population of all the cities')
    print('6. Display city with the highest population')
    print('7. Display city with the lowest population')
    print('8. Exit the program')
    print('')
    
def get_menu():
    display_menu()
    choice = int(input('Insert your choice from 1 to 8 and press Enter: '))
    while choice < 1 or choice > 8:
        choice = int(input('Create the correct value! Value can be from 1 to 8.\n Commit your choice: '))
    return choice

def execute_choice(choice, cur):
    if choice == 1:
        sort_by_ascending(cur)
    elif choice == 2:
        sort_by_descending(cur)
    elif choice == 3:
        sort_by_name(cur)
    elif choice == 4:
        show_tottal_population(cur)
    elif choice == 5:
        show_average_population(cur)
    elif choice == 6:
        show_highest_population(cur)
    elif choice == 7:
        show_lowest_population(cur)
        
def display_results(values):
    print(f'{"Cities":20}{" Population"}')
    for value in values:
        print(f'{value[0]:20} {value[1]:,.0f}')
    print('')
    
def sort_by_ascending(cur):
    cur.execute('''SELECT CityName, Population
                FROM Cities
                ORDER BY Population''')
    results = cur.fetchall()
    print('Cities were sorted by population in ascending order')
    print('---------------------------------------------------')
    display_results(results)

def sort_by_descending(cur):
    cur.execute('''SELECT CityName, Population
                FROM Cities
                ORDER BY Population DESC''')
    results = cur.fetchall()
    print('Cities were sorted by population in descending order')
    print('---------------------------------------------------')
    display_results(results)

def sort_by_name(cur):
    cur.execute('''SELECT CityName, Population
                FROM Cities
                ORDER BY CityName''')
    results = cur.fetchall()
    print('''Cities were sorted by cities' names''')
    print('---------------------------------------------------')
    display_results(results)

def show_tottal_population(cur):
    cur.execute('''SELECT SUM(Population) FROM Cities''')
    results = cur.fetchone()
    print(f'\nTotal population evaluates: {results[0]:,.0f}\n')

def show_average_population(cur):
    cur.execute('''SELECT AVG(Population) FROM Cities''')
    results = cur.fetchone()
    print(f'\nAverage population evaluates: {results[0]:,.0f}\n')

def show_highest_population(cur):
    cur.execute('''SELECT MAX(Population) FROM Cities''')
    max_results = cur.fetchone()
    cur.execute('''SELECT CityName, Population
                FROM Cities
                WHERE Population == ?''', (max_results[0],))
    results = cur.fetchone()
    print(f'\nThe city with the highest population is {results[0]}.\n' +
          f'Population evaluates {results[1]:,.0f}\n')

def show_lowest_population(cur):
    cur.execute('''SELECT MIN(Population) FROM Cities''')
    min_results = cur.fetchone()
    cur.execute('''SELECT CityName, Population
                FROM Cities
                WHERE Population == ?''', (min_results[0],))
    results = cur.fetchone()
    print(f'\nThe city with the lowest population is {results[0]}.\n' +
          f'Population evaluates {results[1]:,.0f}\n')
    
if __name__ == '__main__':
    main()