def input_validation():
    print('Enter the coordinates: ', end="")
    try:
        x, y = input().split()
        x = int(x)
        y = int(y)
    except:
        print('You should enter numbers!')
        x, y = input_validation()
    while (x < 1 or x > 3) or (y < 1 or y > 3):
        print('Coordinates should be from 1 to 3!')
        x, y = input_validation()
    return x, y


class Board:
    def __init__(self):
        self.matrix = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.next_move = 'X'

    def print_board(self):
        print('-' * 9)
        for row in self.matrix:
            print('| ', end="")
            for ch in row:
                print(ch, end=" ")
            print('|')
        print('-' * 9)

    def user_move(self):
        print(self.next_move, "to play")
        x, y = input_validation()
        # x corresponds to the row and y to the column
        # However the map values are 1-indexed
        # while the board is 0-indexed
        while self.matrix[x - 1][y - 1] != ' ':
            print('This cell is occupied! Choose another one!')
            x, y = input_validation()
        self.matrix[x - 1][y - 1] = self.next_move

        # Change next_move to the opposite move:
        self.next_move = 'X' if self.next_move == 'O' else 'O'

    def check_completion(self):
        for row in self.matrix:
            if ' ' in row:
                return False
        return True

    def check_3_x(self):
        # Check for 3 Xs diagonally
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == 'X' or \
                self.matrix[2][0] == self.matrix[1][1] == self.matrix[0][2] == 'X':
            return True

        for i in range(3):
            # Check for 3 Xs in a row
            if 'O' not in self.matrix[i] and ' ' not in self.matrix[i]:
                return True
            # Check for 3 Xs in a column
            if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == 'X':
                return True
        return False

    def check_3_o(self):
        # Check for 3 Os diagonally
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == 'O' or \
                self.matrix[2][0] == self.matrix[1][1] == self.matrix[0][2] == 'O':
            return True

        for i in range(3):
            # Check for O Xs in a row
            if 'X' not in self.matrix[i] and ' ' not in self.matrix[i]:
                return True
            # Check for 3 Os in a column
            if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == 'O':
                return True
        return False
