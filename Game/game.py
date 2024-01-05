from domain.board import Board


class Game:
    def __init__(self):
        self.__user_board = Board()
        self.__computer_board = Board()

    @property
    def user_board(self):
        return self.__user_board.get_board()

    @property
    def computer_board(self):
        return self.__computer_board.get_board()

    def hit_board(self, player, target: str):
        computer = 1
        user = 2
        if player == user:
            self.__computer_board.hit_board(target)
        elif player == computer:
            self.__user_board.hit_board(target)

    def add_plane(self, player, upper_left_corner, plane_number, plane_position):
        computer = 1
        user = 2
        if player == computer:
            if self.__computer_board.add_plane(upper_left_corner, plane_number, plane_position):
                return True
        elif player == user:
            if self.__user_board.add_plane(upper_left_corner, plane_number, plane_position):
                return True
        return False

