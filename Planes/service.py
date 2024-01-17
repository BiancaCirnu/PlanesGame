import random
from Planes.game import Game


class Services:
    def __init__(self):
        self.__game = Game()
    # computer Service

    def generate_computer_board(self):
        _ = 1
        while _ < 4:
            upper_left = random.choice("ABCDEF") + random.choice("123456")
            plane_position = random.randint(1, 4)
            if Game.add_plane(self.__game, 1, upper_left, _, plane_position):
                _ += 1

    def computer_board(self):
        return self.__game.computer_board

    def find_a_target(self):
        line = 2
        for _ in range(2, 10):
            if isinstance(self.__game.user_board[line][_], int):
                if self.__game.user_board[line][_] >= 0:
                    return str("B"+str(_))
        column = 9
        for _ in range(2, 10):
            if isinstance(self.__game.user_board[_][column], int):
                if self.__game.user_board[_][column] >= 0:
                    return chr(ord('A') + _ - 1) + str(column)
        line = 9
        for _ in [9, 8, 7, 6, 5, 4, 3, 2]:
            if isinstance(self.__game.user_board[line][_], int):
                if self.__game.user_board[line][_] >= 0:
                    return str("I"+str(_))

        column = 2
        for _ in [9, 8, 7, 6, 5, 4, 3, 2]:
            if isinstance(self.__game.user_board[_][column], int):
                if self.__game.user_board[_][column] >= 0:
                    return chr(ord('A') + _ - 1) + str(column)

        line = 4
        for _ in range(4, 8):
            if isinstance(self.__game.user_board[line][_], int):
                if self.__game.user_board[line][_] >= 0:
                    return str("D"+str(_))

        column = 7
        for _ in range(4, 8):
            if isinstance(self.__game.user_board[_][column], int):
                if self.__game.user_board[_][column] >= 0:
                    return chr(ord('A') + _ - 1) + str(column)

        line = 7
        for _ in [6, 5, 4]:
            if isinstance(self.__game.user_board[line][_], int):
                if self.__game.user_board[line][_] >= 0:
                    return str("G"+str(_))

        column = 4
        for _ in [6, 5]:
            if isinstance(self.__game.user_board[_][column], int):
                if self.__game.user_board[_][column] >= 0:
                    return chr(ord('A') + _ - 1) + str(column)

        for _ in range(1, 11):
            for __ in range(1, 11):
                if isinstance(self.__game.user_board[_][__], int):
                    if self.__game.user_board[_][__] > 0:
                        if self.verify_if_neighbors_are_part_of_a_plane(_, __):
                            return chr(ord('A') + _ - 1) + str(__)

    def verify_if_neighbors_are_part_of_a_plane(self, row, column):
        board = self.__game.user_board
        if row > 1:
            if isinstance(board[row-1][column], int):
                if board[row-1][column] < 0:
                    return True
        if column > 1:
            if isinstance(board[row][column - 1], int):
                if board[row][column - 1] < 0:
                    return True
        if row < 10:
            if isinstance(board[row + 1][column], int):
                if board[row + 1][column] < 0:
                    return True
        if column < 10:
            if isinstance(board[row][column + 1], int):
                if board[row][column + 1] < 0:
                    return True
        return False

    def hit_user(self):
        target = self.find_a_target()
        self.__game.hit_board(1, target)

    # user Service
    def add_plane(self, plane_number, upper_left_corner, plane_position):
        if not Game.add_plane(self.__game, 2, upper_left_corner, plane_number, plane_position):
            return False
        return True

    def user_board(self):
        return self.__game.user_board

    def hit_computer(self, target):
        self.__game.hit_board(2, target)

    def verify_if_game_is_over(self, player):
        computer = 1
        user = 2
        if player == computer:
            for _ in range(1, 11):
                for __ in range(1, 11):
                    if isinstance(self.__game.user_board[_][__], int):
                        if self.__game.user_board[_][__] > 0:
                            return False
        elif player == user:
            for _ in range(1, 11):
                for __ in range(1, 11):
                    if isinstance(self.__game.computer_board[_][__], int):
                        if self.__game.computer_board[_][__] > 0:
                            return False
        return True
    # other services


class TestData:
    @staticmethod
    def test_target(target):
        if len(target) == 2:
            if target[0] not in "ABCDEFGHIJ" or target[1] not in "123456789":
                return False
            return True
        elif len(target) == 3:
            if target[0] not in "ABCDEFGHIJ" or not target[1] == '1' or not target[2] == '0':
                return False
            return True
        else:
            return False

    @staticmethod
    def test_corner(upper_left_corner, plane_position):
        try:
            if not len(upper_left_corner) == 2:
                raise ValueError("Corner has to be represented by a letter followed by a digit")
            else:
                if plane_position in [1, 3]:
                    if not upper_left_corner[0] in "ABCDEFG" or not upper_left_corner[1] in "123456":
                        raise ValueError("Plane has to fit in the board")
                elif plane_position in [2, 4]:
                    if not upper_left_corner[0] in "ABCDEF" or not upper_left_corner[1] in "1234567":
                        raise ValueError("Plane has to fit in the board")
        except ValueError:
            return False
        return True

    @staticmethod
    def test_position(plane_position):
        try:
            plane_position = int(plane_position)
        except ValueError:
            print("The position of the plane has to be a number in the interval [1,4]")
            return False
        if plane_position not in [1, 2, 3, 4]:
            print("The position of the plane has to be a number in the interval [1,4]")
            return False
        return True
