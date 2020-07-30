from math import sqrt


class TicTacToe(object):
    """
    Has convered wining scenerio where player1 has won with horizontal matching or vertical and also seeing if the board is filled and nobody has won then print draw
    """

    def __init__(self, ceils, players, game_over=False):
        self.ceils = ceils
        self.players = players
        self.game_over = game_over

    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    def design_board(self):
        rows = int(sqrt(self.ceils))
        colboard = []
        for row in range(rows):
            rowboard = []
            for col in range(rows):
                rowboard.append(row * rows + (col + 1))
            colboard.append(rowboard)
        return colboard

    def fill_number_in_board(self, number, value, board):
        rows = int(sqrt(self.ceils))
        div = number // rows
        mod = number % rows
        if mod == 0:
            div = div - 1
            mod = rows - mod
        if board[div][mod - 1] in ('X', 'Y'):
            print(board)
            raise Exception("Invalid Number has entered")
        board[div][mod - 1] = value
        print(board)

    def is_board_completed(self, board):
        for row in range(int(sqrt(self.ceils))):
            for col in range(int(sqrt(self.ceils))):
                if board[row][col] not in ('X', 'Y'):
                    return False
        return True

    def won(self, board):
        # horizontal check
        for row in range(int(sqrt(self.ceils))):
            if len(list(set(board[row]))) == 1:
                return True
        # vertical check
        for col in range(int(sqrt(self.ceils))):
            if len(list(set([board[row][col] for row in range(int(sqrt(self.ceils)))]))) == 1:
                return True
        # diagonal check
        # will put check here
        return False

    def start_game(self):
        # design grid of the above ceils count
        print("Displaying tic toe tac board")
        board = self.design_board()
        print(board)
        while (True):
            invalid_value = True
            while (invalid_value):
                player1_number = int(input("First player turn, please enter your number \n"))
                try:
                    self.fill_number_in_board(number=player1_number, value='X', board=board)
                    invalid_value = False
                except Exception:
                    print("Need to enter number again")
                    invalid_value = True

            if self.won(board):
                print("player1_number has won the game")
                break
            elif self.is_board_completed(board):
                print("DRAW")
                break

            # need to check player has enter valid number, this would get filled in cardboard
            invalid_value = True
            while (invalid_value):
                player2_number = int(input("Second player turn, please enter your number \n"))
                try:
                    self.fill_number_in_board(number=player2_number, value='Y', board=board)
                    invalid_value = False
                except Exception:
                    print("Need to enter number again")
                    invalid_value = True
            # need to check here we receive winning criteria or board has filled
            if self.won(board):
                print("player2_number has won the game")
                break
            elif self.is_board_completed(board):
                print("DRAW")
                break

if __name__ == '__main__':
    tct = TicTacToe(ceils=9, players=2)
    tct.start_game()
