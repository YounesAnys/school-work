#ITI1120
#Assignment Number 3
#Gorji, Mahyar
#8135109

import random

def create_board(size):
    '''int->list (of str)
       Precondition: size is even positive integer between 2 and 52    
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    random.shuffle(board)
    return board
#-----------------------------------------------------
def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')
#-----------------------------------------------------
def wait_for_player():
    '''(None)->None
    Pauses the program until the user presses enter
    '''
    try:
        input("Press enter to continue ")
    except SyntaxError:
        pass
#-----------------------------------------------------
def play_game(board):
    '''(list of str)->None'''
    count = 0
    bestpossible = len(board) // 2
   # YOUR CODE GOES HERE
   # this is the funkytown that plays the game
    while astchecker() is True:
        print_board(astlist)
        print("")
        print("Enter two distinct locations on the board that you want revealed.")
        print("i.e two integers in the range [1, ", size,"]", sep = "")
        numinput1 = int(input()) - 1
        numinput2 = int(input()) - 1
        #Checks if any of the inputs are invalid, and restarts the programs accordingly,
        #as it is fairly early in the program's execution, and a restart would not be bad practice.
        #However, note that a 'while' loop may also be used here.
        if numinput1 < 0 or numinput1 > size or numinput2 < 0 or numinput2 > size:
            print("\nSorry, one of the values you've inputted seems to be out of range.")
            print("Please try again, using values within the example given. Thank you.\n")
            play_game(board)
        iscorrect(numinput1, numinput2)
        clearscreen()
        count += 1
    print_board(astlist)
    print("\nCongratulations! You have completed the game with {} guesses. \nThat is {} more than the best possible!".format(count, count - bestpossible))
#-------------------------------------------------------
#This will check if any asterisks are remaining in astlist. Because there cannot be an odd
#amount of asterisks, this will make it so that if even 1 is detected, then there is an eligible
#pair waiting to be matched on asteriskmingle.com. Find the STAR of your life tonight!
def astchecker():
    '''(int) -> (bool)
    Checks how many asterisks are inside astlist and astchecker returns True if at least one remains
    '''
    nevergonnagiveyouup = astlist.count("*")
    if nevergonnagiveyouup > 0:
        return True
    else:
        return False
#-------------------------------------------------------
def iscorrect(ind1, ind2):
    '''(int, int) --> (str) and (str)
    if the function is used after the user gives their number inputs, this function will assign
    numinput1 and numinput2 to the indexes of astlist and varboard, and reveal them as a result.
    If the varboard indices aren't equal in string value, both are masked again with an '*'
    '''
    astlist[ind1] = varboard[ind1]
    astlist[ind2] = varboard[ind2]
    print_board(astlist)
    wait_for_player()
    #if the two varboard indices aren't equal, then astlist[ind1,ind2] reset to asterisks again.
    if varboard[ind1] != varboard[ind2]:
        astlist[ind1] = "*"
        astlist[ind2] = "*"
#-------------------------------------------------------
def clearscreen():
    '''(No input) --> (empty space)
    Function prints empty space 70 times vertically, effectively clearing the screen
    '''
    
    print("\n" * 70)
          
# MAIN 
# YOUR CODE GOES HERE TOO
# HERE YOU OBTAIN THE SIZE OF THE BOARD THE PLAYER WANTS TO PLAY WITH
#Global Stuff--------------------------------------------------------------------
size = int(input('Pick an even number between 2 and 52: '))
while size % 2 != 0 and size >= 2 and size <= 52:
    size = int(input('Pick an even number between 2 and 52: '))
varboard = create_board(size)
astlist = ['*']*size
count = 0
bestpossible = int(len(varboard)/2)
correctness = False

# this calls your play_game function that plays the game
play_game(varboard)
