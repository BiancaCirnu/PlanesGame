import unittest

from service import Services

from Planes.game import Game


class MyTestCase(unittest.TestCase):
    def test_add_planes(self):
        game = Game()
        game.add_plane(1, 'A1', 1, 1)
        with self.assertRaises(ValueError):
            game.add_plane(1, 'A0', 1, 4)
            game.add_plane(1, 'AA', 2, 2)
            game.add_plane(1, 'K1', 3, 3)
            game.add_plane(1, 'A1', 4, 1)
            game.add_plane(1, 'A2', 5, 1)

    def test_hit_board(self):
        game = Game()
        game.add_plane(1, 'A1', 1, 4)
        game.add_plane(1, 'A7', 2, 2)
        game.add_plane(1, 'E3', 3, 3)

        game.add_plane(2, 'A1', 1, 4)
        game.add_plane(2, 'A7', 2, 2)
        game.add_plane(2, 'E3', 3, 3)

        self.assertIsNone(game.hit_board(1, 'A1'))
        with self.assertRaises(ValueError):
            game.hit_board(1, 'A1')

    def test_win_game(self):
        game = Game()
        game.add_plane(1, 'A1', 1, 4)
        game.add_plane(1, 'A7', 2, 2)
        game.add_plane(1, 'E3', 3, 3)

        game.add_plane(2, 'A1', 1, 4)
        game.add_plane(2, 'A7', 2, 2)
        game.add_plane(2, 'E3', 3, 3)

        game.hit_board(1, 'C1')
        game.hit_board(1, 'A2')
        game.hit_board(1, 'B2')
        game.hit_board(1, 'C2')
        game.hit_board(1, 'D2')
        game.hit_board(1, 'E2')
        game.hit_board(1, 'C3')
        game.hit_board(1, 'B4')
        game.hit_board(1, 'C4')
        game.hit_board(1, 'D4')
        game.hit_board(1, 'E4')
        game.hit_board(1, 'E5')
        game.hit_board(1, 'E6')
        game.hit_board(1, 'F5')
        game.hit_board(1, 'G3')
        game.hit_board(1, 'G4')
        game.hit_board(1, 'G5')
        game.hit_board(1, 'G6')
        game.hit_board(1, 'G7')
        game.hit_board(1, 'H4')
        game.hit_board(1, 'C7')
        game.hit_board(1, 'D7')
        game.hit_board(1, 'E7')
        game.hit_board(1, 'D8')
        game.hit_board(1, 'B9')
        game.hit_board(1, 'C9')
        game.hit_board(1, 'D9')
        game.hit_board(1, 'E9')
        game.hit_board(1, 'F9')

        self.service = Services()
        self.assertTrue(self.service.verify_if_game_is_over(1))
        game.hit_board(1, 'D10')

        self.assertTrue(self.service.verify_if_game_is_over(1))

if __name__ == '__main__':
    unittest.main()
