# write your code here
from Board import Board
from User_Inputs import user_inputs

user_input = 'start easy easy'
user_input = user_input.split()

while user_input[0] is not user_inputs.EXIT.value:

    user_input = input('Input command:')
    user_input = user_input.split()

    if user_input[0] == user_inputs.EXIT.value:
        break

    if len(user_input) != 3:
        print('Bad parameters!')
        continue
    else:
        gameBoard = Board()
        gameBoard.printBoard()
        gameBoard.play(user_input)
