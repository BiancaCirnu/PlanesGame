import copy
from domain.plane import Plane


class Board:
    def __init__(self):
        empty_row = ['A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        empty_board = [[' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        for _ in range(0, 10):
            empty_row[0] = chr(ord('A') + _)
            empty_board.append(copy.deepcopy(empty_row))
        self.__game = empty_board

    @property
    def board(self):
        return self.__game

    def get_board(self):
        return self.__game

    def add_plane(self, upper_right_corner, new_plane, plane_position):
        new_plane = Plane(new_plane)
        new_plane.position = plane_position
        new_plane.rotate_plane()
        if upper_right_corner[0] < 'A' or upper_right_corner[1] < '1':
            raise ValueError("Plane has to be on the board")
        elif new_plane.position in [1, 3]:
            if upper_right_corner[0] > "G" or upper_right_corner[1] > '6':
                raise ValueError("Plane has to fit in the board")
        elif new_plane.position in [2, 4]:
            if upper_right_corner[0] > "F" or upper_right_corner[1] > '7':
                raise ValueError("Plane has to fit in the board")
        if Board.verify_if_plane_doesnt_overlap_another_plane(self, upper_right_corner, new_plane):
            Board.add_plane_to_board(self, upper_right_corner, new_plane)
            return True
        return False

    def add_plane_to_board(self, upper_right_corner, new_plane: Plane):
        upper_right_corner = [int(ord(upper_right_corner[0]) - ord('A')) + 1, int(upper_right_corner[1])]
        if new_plane.position in [1, 3]:
            for _ in range(0, 4):
                for __ in range(0, 5):
                    if new_plane.get_plane[_][__]:
                        self.__game[upper_right_corner[0] + _][upper_right_corner[1] + __] = new_plane.get_plane[_][__]
        elif new_plane.position in [2, 4]:
            for _ in range(0, 5):
                for __ in range(0, 4):
                    if new_plane.get_plane[_][__]:
                        self.__game[upper_right_corner[0] + _][upper_right_corner[1] + __] = new_plane.get_plane[_][__]

    def verify_if_plane_doesnt_overlap_another_plane(self, upper_right_corner: str, new_plane: Plane):
        upper_right_corner = [int(ord(upper_right_corner[0]) - ord('A'))+1, int(upper_right_corner[1])]
        try:
            if new_plane.position in [1, 3]:
                for _ in range(0, 4):
                    for __ in range(0, 5):
                        if self.__game[upper_right_corner[0]+_][upper_right_corner[1]+__] and new_plane.get_plane[_][__]:
                            if not self.__game[upper_right_corner[0]+_][upper_right_corner[1]+__] == new_plane.get_plane[_][__]:
                                raise ValueError("Plane overlaps another plane")
            elif new_plane.position in [2, 4]:
                for _ in range(0, 5):
                    for __ in range(0, 4):
                        if self.__game[upper_right_corner[0] + _][upper_right_corner[1] + __] and new_plane.get_plane[_][__]:
                            if not self.__game[upper_right_corner[0] + _][upper_right_corner[1] + __] == new_plane.get_plane[_][__]:
                                raise ValueError("Plane overlaps another plane")
        except ValueError:
            return False
        return True

    def hit_board(self, target: str):
        """
        - if the target belongs to one of the planes, the number in the array will be replaced with the opposite of the planes index.
        - otherwise, the number will be replaced with 'X'
        :return:
        """
        if len(target) == 2:
            target = [ord(target[0])-ord('A')+1, int(target[1])]
        elif len(target) == 3:
            target = [int(ord(target[0]) - ord('A')) + 1, int(target[1])*10+int(target[2])]
        if 0 < target[0] < 11 and 0 < target[1] < 11:
            if isinstance(self.__game[target[0]][target[1]], int):
                if self.__game[target[0]][target[1]] > 0:
                    self.__game[target[0]][target[1]] = -self.__game[target[0]][target[1]]
                    if self.plane_is_destroyed(self.__game[target[0]][target[1]]):
                        for _ in self.__game:
                            for __ in _:
                                if __ == self.__game[target[0]][target[1]]:
                                    __ = 'X'
                elif self.__game[target[0]][target[1]] == 0:
                    self.__game[target[0]][target[1]] = '#'
            else:
                raise ValueError("Target was already shot")


    def plane_is_destroyed(self, plane_hit):
        for _ in self.__game:
            for __ in _:
                if __ == -plane_hit:
                    return False
        return True

