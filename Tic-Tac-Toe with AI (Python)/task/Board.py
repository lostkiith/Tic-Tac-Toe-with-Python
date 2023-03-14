import random
from User_Inputs import user_inputs


class Board:
    PLAY_X = 'X'
    PLAY_O = 'O'

    def __init__(self):
        self.game_board = []
        self.possible_moves = [[0, 0], [0, 1], [0, 2],
                               [1, 0], [1, 1], [1, 2],
                               [2, 0], [2, 1], [2, 2]]
        self.current_player = self.PLAY_X
        self.game_state = 'null'
        self.setUpBoard()

    def setUpBoard(self):
        counter = 0
        for i in range(3):
            self.game_board.append([])
            for j in range(3):
                self.game_board[i].append('_')
                counter += 1

    def printBoard(self):
        print('---------')
        for line in self.game_board:
            print('|', end='')
            print(" ", end='')
            for item in line:
                if item == '_':
                    print(" ", end='')
                    print(" ", end='')
                else:
                    print(item, end='')
                    print(" ", end='')
            print('|')

        print('---------')

    def check_for_game_condition(self):
        for i in range(2):
            # check for win in vertical
            if all(ele == self.game_board[i][0] for ele in self.game_board[i]) and self.game_board[i][0] != '_':
                self.game_state = self.game_board[i][0]
                break
            # check for win in horizontal
            if self.game_board[0][i] == self.game_board[1][i] and self.game_board[0][i] == self.game_board[2][i] and \
                    self.game_board[0][
                        i] != '_':
                self.game_state = self.game_board[0][i]
                break

        if self.game_board[0][0] == self.game_board[1][1] and self.game_board[0][0] == self.game_board[2][2] and \
                self.game_board[0][
                    0] != '_':
            self.game_state = self.game_board[0][0]

        elif self.game_board[0][2] == self.game_board[1][1] and self.game_board[0][2] == self.game_board[2][0] and \
                self.game_board[0][
                    2] != '_':
            self.game_state = self.game_board[0][2]

        elif self.game_board[0].count('_') == 0 and self.game_board[1].count('_') == 0 and self.game_board[2].count(
                '_') == 0:
            self.game_state = 'Draw'

    def _switch_player(self):
        if self.current_player == self.PLAY_X:
            self.current_player = self.PLAY_O
        else:
            self.current_player = self.PLAY_X

    def _who_has_won(self):
        if self.game_state != 'Draw':
            print(f'{self.game_state} wins')
        else:
            print(f'{self.game_state}')

    def _pos_play(self, y, x):
        self.game_board[y][x] = self.current_player
        self.possible_moves.remove([y, x])
        self._switch_player()

    def _AI_move(self, user, scores_dic=None):

        if scores_dic is None:
            scores_dic = {}

        def minimax(depth, is_minimaxing, scores, move):
            self.check_for_game_condition()
            if self.game_state != 'null':
                score = scores[self.game_state]
                self.game_state = 'null'
                return score

            if move == 'X':
                move = 'O'
            else:
                move = 'X'

            if is_minimaxing:
                best_score = -1000
                for i in range(3):
                    for j in range(3):
                        if self.game_board[i][j] == '_':
                            self.game_board[i][j] = move
                            score = minimax(depth + 1, False, scores, move)
                            self.game_board[i][j] = '_'
                            best_score = max(score, best_score)
                return best_score
            else:
                best_score = 1000
                for i in range(3):
                    for j in range(3):
                        if self.game_board[i][j] == '_':
                            self.game_board[i][j] = move
                            score = minimax(depth + 1, True, scores, move)
                            self.game_board[i][j] = '_'
                            best_score = min(score, best_score)
                return best_score

        def random_play():
            ai_play = self.possible_moves[random.randint(0, len(self.possible_moves) - 1)]
            self.game_board[ai_play[0]][ai_play[1]] = self.current_player
            self.possible_moves.remove(ai_play)
            self._switch_player()

        def medium_play():
            current = self.current_player
            # check for a wining current_player horizontal
            for i in range(2):
                if self.current_player in self.game_board[i][1] and self.current_player in self.game_board[i][2] and \
                        self.game_board[i][0] == '_':
                    print(f'found win')
                    self._pos_play(i, 0)
                    break
                if self.current_player in self.game_board[i][0] and self.current_player in self.game_board[i][2] and \
                        self.game_board[i][1] == '_':
                    print(f'found win')
                    self._pos_play(i, 1)
                    break
                if self.current_player in self.game_board[i][0] and self.current_player in self.game_board[i][1] and \
                        self.game_board[i][2] == '_':
                    print(f'found win')
                    self._pos_play(i, 2)
                    break
            # check for win block
            if self.current_player == self.PLAY_X:
                other_player = self.PLAY_O
            else:
                other_player = self.PLAY_X
            for i in range(2):
                if other_player in self.game_board[i][1] and other_player in self.game_board[i][2] and \
                        self.game_board[i][0] == '_':
                    self._pos_play(i, 0)
                    break
                if other_player in self.game_board[i][0] and other_player in self.game_board[i][2] and \
                        self.game_board[i][1] == '_':
                    self._pos_play(i, 1)
                    break
                if other_player in self.game_board[i][0] and other_player in self.game_board[i][1] and \
                        self.game_board[i][2] == '_':
                    self._pos_play(i, 2)
                    break
            # diagonal check
            if other_player == self.game_board[1][1] and other_player == self.game_board[2][2] and self.game_board[0][
                0] == '_':
                self._pos_play(0, 0)
            if other_player == self.game_board[1][1] and other_player == self.game_board[0][0] and self.game_board[2][
                2] == '_':
                self._pos_play(2, 2)
            if other_player == self.game_board[1][1] and other_player == self.game_board[2][0] and self.game_board[0][
                2] == '_':
                self._pos_play(0, 2)
            if other_player == self.game_board[1][1] and other_player == self.game_board[0][2] and self.game_board[2][
                0] == '_':
                self._pos_play(2, 0)

            if self.current_player == current:
                random_play()

        def hard_play(scores):
            best_score = -1000
            best_move = {}
            for i in range(3):
                for j in range(3):
                    if self.game_board[i][j] == '_':
                        self.game_board[i][j] = self.current_player
                        score = minimax(0, False, scores, self.current_player)
                        self.game_board[i][j] = '_'
                        if score > best_score:
                            best_score = score
                            best_move = [i, j]
            self._pos_play(best_move[0], best_move[1])

        if user == 'easy':
            print('Making move level "easy"')
            random_play()

        elif user == 'medium':
            print('Making move level "medium"')
            medium_play()

        elif user == 'hard':
            print('Making move level "hard"')
            hard_play(scores_dic)

        self.printBoard()
        self.check_for_game_condition()

    def _user_move(self):
        # check input from player
        acceptable = False
        while not acceptable:
            coordinates = input('Enter the coordinates: ')
            coordinate = coordinates.split()

            if len(coordinate) != 2 or not coordinate[0].isnumeric() or not coordinate[1].isnumeric():
                print('You should enter numbers!')
                continue

            coor1 = int(coordinate[0]) - 1
            coor2 = int(coordinate[1]) - 1

            if coor1 > 2 or coor2 > 2:
                print('Coordinates should be from 1 to 3!')
                continue

            if self.game_board[coor1][coor2] != '_':
                print('This cell is occupied! Choose another one!')
                continue
            else:
                acceptable = True
                self.game_board[coor1][coor2] = self.current_player
                self.possible_moves.remove([coor1, coor2])
                if self.current_player == self.PLAY_X:
                    self.current_player = self.PLAY_O
                else:
                    self.current_player = self.PLAY_X

            self.printBoard()
            self.check_for_game_condition()

    def play(self, user_input):

        while self.game_state == 'null':

            if user_input[1] == user_inputs.MEDIUM.value or user_input[1] == user_inputs.EASY.value \
                    or user_input[1] == user_inputs.HARD.value:
                self._AI_move(user_input[1], scores_dic={'X': 1, 'O': -1, 'Draw': 0})
                if self.game_state != 'null':
                    self._who_has_won()
                    break
                if user_input[2] == user_inputs.MEDIUM.value or user_input[2] == user_inputs.EASY.value \
                        or user_input[2] == user_inputs.HARD.value:
                    self._AI_move(user_input[2], scores_dic={'X': -1, 'O': 1, 'Draw': 0})
                    if self.game_state != 'null':
                        self._who_has_won()
                        break
                else:
                    self._user_move()
                    if self.game_state != 'null':
                        self._who_has_won()
                        break
            else:
                if user_input[1] == user_inputs.USER.value:
                    self._user_move()
                    if self.game_state != 'null':
                        self._who_has_won()
                        break
                    if user_input[2] == user_inputs.MEDIUM.value or user_input[2] == user_inputs.EASY.value \
                            or user_input[2] == user_inputs.HARD.value:
                        self._AI_move(user_input[2], scores_dic={'X': -1, 'O': 1, 'Draw': 0})
                        if self.game_state != 'null':
                            self._who_has_won()
                            break
                    else:
                        self._user_move()
                        if self.game_state != 'null':
                            self._who_has_won()
                            break
