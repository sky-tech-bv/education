'''
PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *
'''

def print_big(letter):
    dict={'a':'  *  \n * * \n*****\n*   *\n*   *', 
         'b':'***  \n*  * \n*****\n*   *\n*****',
         'c':' *** \n*   *\n*    \n*   *\n *** ',
         'd':'**** \n*   *\n*   *\n*   *\n**** ',
         'e':'*****\n*    \n*****\n*    \n*****'}
    print(dict[letter])

print_big('a')
print_big('b')
print_big('c')
print_big('d')
print_big('e')