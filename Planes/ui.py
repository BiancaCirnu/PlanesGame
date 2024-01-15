import copy

from service import Services, TestData


def place_planes(game: Services):
    __ = 1
    for _ in game.user_board():
        print(_[0], _[1], _[2], _[3], _[4], _[5], _[6], _[7], _[8], _[9], _[10])
    print("PLACE YOUR PLANES")
    while __ < 4:
        upper_left_corner = input("Write the position of the upper-left corner of the plane on the board: ")
        plane_position = input("Write plane's position: ")
        if TestData.test_position(plane_position):
            plane_position = int(plane_position)
            if TestData.test_corner(upper_left_corner, plane_position):
                if game.add_plane(__, upper_left_corner, plane_position):
                    __ += 1
                    for _ in game.user_board():
                        print(_[0], _[1], _[2], _[3], _[4], _[5], _[6], _[7], _[8], _[9], _[10])
                else:
                    print("Plane overlaps another existing plane")


def display_board(board: list):
    new_board = copy.deepcopy(board)
    for _ in range(1, 11):
        for __ in range(1, 11):
            if isinstance(new_board[_][__], int):
                if new_board[_][__] >= 0:
                    new_board[_][__] = ' '
                elif new_board[_][__] < 0:
                    new_board[_][__] = 'X'
    for _ in new_board:
        print(f"{_[0]} | {_[1]} | {_[2]} | {_[3]} | {_[4]} | {_[5]} | {_[6]} | {_[7]} | {_[8]} | {_[9]} | {_[10]}")


def hit_opponent(game):
    try:
        target = input("Choose your target: ")
        if TestData.test_target(target):
            game.hit_computer(target)
        else:
            raise ValueError
        return game.computer_board()
    except ValueError:
        print("Input is not valid")
        hit_opponent(game)


def start():
    game = Services()
    game.generate_computer_board()
    place_planes(game)
    computer = 1
    user = 2
    while True:
        hit_opponent(game)
        print("Opponent's board:", '\n')
        display_board(game.computer_board())
        if game.verify_if_game_is_over(user):
            print("YOU WON!")
            break
        print()
        game.hit_user()
        print("Your board:", '\n')
        display_board(game.user_board())
        if game.verify_if_game_is_over(computer):
            print("YOU LOST!")
            break


if __name__ == '__main__':
    start()
