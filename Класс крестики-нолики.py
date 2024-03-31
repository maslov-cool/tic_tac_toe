class TicTacToeBoard:
    def __init__(self):
        self.field = [['-' for _ in range(3)] for _ in range(3)]
        self.variations = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
                           [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
                           [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
        self.cnt = 0
        self.flag = False

    def new_game(self):
        self.field = [['-' for _ in range(3)] for _ in range(3)]
        self.cnt = 0
        self.flag = False

    def get_field(self):
        return self.field

    def check_field(self):
        flag_continue_game = False
        for z in self.variations:
            A = ''
            for i, j in z:
                A += self.field[i][j]
            if set(A) == {'X'}:
                return 'X'
            elif set(A) == {'0'}:
                return '0'
            elif set(A) == '-' or (len(set(A)) == 2 and '-' in set(A) and ('X' in set(A) or '0' in set(A))):
                flag_continue_game = True
        if flag_continue_game:
            return
        return 'D'

    def make_move(self, row, col):
        if self.flag:
            return 'Игра уже завершена'
        if not self.cnt:
            if self.field[row - 1][col - 1] == '-':
                self.field[row - 1][col - 1] = 'X'
                self.cnt = 1
            else:
                return f'Клетка {row}, {col} уже занята'
        else:
            if self.field[row - 1][col - 1] == '-':
                self.field[row - 1][col - 1] = '0'
                self.cnt = 0
            else:
                return f'Клетка {row}, {col} уже занята'
        s = self.check_field()
        if s == 'X':
            self.flag = True
            return 'Победил игрок X'
        elif s == '0':
            self.flag = True
            return 'Победил игрок 0'
        elif s == 'D':
            return 'Ничья'
        return 'Продолжаем играть'

