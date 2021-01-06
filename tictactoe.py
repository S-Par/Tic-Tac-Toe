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


def introduction():
    print("""Welcome to
    88888888888 8888888 .d8888b.       88888888888     d8888  .d8888b.       88888888888 .d88888b.  8888888888 
        888       888  d88P  Y88b          888        d88888 d88P  Y88b          888    d88P" "Y88b 888        
        888       888  888    888          888       d88P888 888    888          888    888     888 888        
        888       888  888                 888      d88P 888 888                 888    888     888 8888888    
        888       888  888                 888     d88P  888 888                 888    888     888 888        
        888       888  888    888 888888   888    d88P   888 888    888 888888   888    888     888 888        
        888       888  Y88b  d88P          888   d8888888888 Y88b  d88P          888    Y88b. .d88P 888        
        888     8888888 "Y8888P"           888  d88P     888  "Y8888P"           888     "Y88888P"  8888888888
    """)
    print("-" * 80)
    print("Here are a few instructions to get you started:")
    print("A board looks like this:")
    test_board = Board()
    test_board.print_board()
    print("You will be prompted to enter coordinates.")
    print("Enter a row and column number (between 1 and 3) to place your move on the board.")
    print("Enjoy playing Tic-Tac-Toe with your friends!")
    print("-" * 80, end="\n\n\n")

def main():
    introduction()
    board = Board()
    board.print_board()

    # Until the board is not solved, keep asking for moves and print board:
    while not board.check_completion():
        board.user_move()
        board.print_board()
        # Check if someone won:
        if board.check_3_x():
            print('X wins')
            break
        elif board.check_3_o():
            print('O wins')
            break
    else:
        print('Draw')


if __name__ == '__main__':
    main()

