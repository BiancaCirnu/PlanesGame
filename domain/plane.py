class Plane:
    def __init__(self, plane_number):
        self.__plane_id = plane_number
        self.__position = 1
        self._plane = [[0, 0, self.__plane_id, 0, 0], [self.__plane_id, self.__plane_id, self.__plane_id, self.__plane_id, self.__plane_id], [0, 0, self.__plane_id, 0, 0], [0, self.__plane_id, self.__plane_id, self.__plane_id, 0]]

    def __eq__(self, other):
        return self.__plane_id == other.__plane_id

    def rotate_plane(self):
        if self.__position == 1:
            self._plane = [[0, 0, self.__plane_id, 0, 0], [self.__plane_id, self.__plane_id, self.__plane_id, self.__plane_id, self.__plane_id], [0, 0, self.__plane_id, 0, 0], [0, self.__plane_id, self.__plane_id, self.__plane_id, 0]]
        elif self.__position == 2:
            self._plane = [[0, 0, self.__plane_id, 0], [self.__plane_id, 0, self.__plane_id, 0], [self.__plane_id, self.__plane_id, self.__plane_id, self.__plane_id], [self.__plane_id, 0, self.__plane_id, 0], [0, 0, self.__plane_id, 0]]
        elif self.__position == 3:
            self._plane = [[0, self.__plane_id, self.__plane_id, self.__plane_id, 0], [0, 0, self.__plane_id, 0, 0], [self.__plane_id, self.__plane_id, self.__plane_id, self.__plane_id, self.__plane_id], [0, 0, self.__plane_id, 0, 0]]
        elif self.__position == 4:
            self._plane = [[0, self.__plane_id, 0, 0], [0, self.__plane_id, 0, self.__plane_id], [self.__plane_id, self.__plane_id, self.__plane_id, self.__plane_id], [0, self.__plane_id, 0, self.__plane_id], [0, self.__plane_id, 0, 0]]

    @property
    def position(self):
        return self.__position

    @property
    def get_plane(self):
        return self._plane

    @position.setter
    def position(self, new_position):
        self.__position = new_position


    def get_cockpit_coordinates(self):
        if self.__position == 1:
            return 0, 2
        elif self.__position == 2:
            return 2, 3
        elif self.__position == 3:
            return 3, 2
        elif self.__position == 4:
            return 2, 0

    def rotate_right(self):
        self.__position += 1
        if not self.__position == 4:
            self.__position = self.__position % 4
        self.rotate_plane()

    def rotate_left(self):
        self.__position -= 1
        if self.__position == 0:
            self.__position = 4
        self.rotate_plane()
