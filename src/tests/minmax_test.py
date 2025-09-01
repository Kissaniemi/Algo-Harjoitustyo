import unittest
from minmax import iterative_deepening
from connect import check_winner


class TestConnect(unittest.TestCase):
    def setUp(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

    def test_best_start_next_move(self):
        self.assertEqual(
            3, iterative_deepening(self.board, 2, None, -1000000, 1000000, 1)[0])

    def test_block_vertical(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0]]

        self.assertEqual(2, iterative_deepening(
            board, 2, 0, -1000000, 1000000, 4)[0])

    def test_block_horizontal(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0, 0]]

        self.assertEqual(3, iterative_deepening(
            board, 2, 2, -1000000, 1000000, 4)[0])

    def test_block_diagonal_right(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0],
                 [2, 1, 0, 0, 0, 0, 0],
                 [2, 2, 1, 0, 0, 0, 0],
                 [2, 2, 1, 0, 0, 0, 0]]

        self.assertEqual(3, iterative_deepening(
            board, 2, 2, -1000000, 1000000, 10)[0])

    def test_block_diagonal_left(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 1, 2],
                 [0, 0, 0, 0, 1, 2, 2],
                 [0, 0, 0, 0, 1, 2, 2]]

        self.assertEqual(3, iterative_deepening(
            board, 2, 4, -1000000, 1000000, 10)[0])

    def test_winning_move_vertical(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0]]

        self.assertEqual(2, iterative_deepening(
            board, 2, 3, -1000000, 1000000, 4)[0])

    def test_winning_move_horizontal(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [2, 2, 2, 0, 0, 0, 0]]

        self.assertEqual(3, iterative_deepening(
            board, 2, 6, -1000000, 1000000, 4)[0])

    def test_winning_move_diagonal_right(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(3, iterative_deepening(
            board, 2, 6, -1000000, 1000000, 4)[0])

    def test_winning_move_diagonal_left(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 0, 0, 2, 0],
                 [0, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(3, iterative_deepening(
            board, 2, 0, -1000000, 1000000, 4)[0])

    def test_winning_move_before_opponent(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 2],
                 [1, 0, 0, 0, 0, 0, 2],
                 [1, 0, 0, 0, 0, 0, 2]]

        self.assertEqual(6, iterative_deepening(
            board, 2, 0, -1000000, 1000000, 7)[0])

    def test_winning_move_before_opponent_2(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0, 1],
                 [2, 0, 0, 0, 0, 0, 1],
                 [2, 0, 0, 0, 0, 0, 1]]

        self.assertEqual(0, iterative_deepening(
            board, 2, 6, -1000000, 1000000, 7)[0])

    def test_board_full(self):
        board = [[1, 1, 2, 2, 1, 1, 1],
                 [1, 2, 1, 1, 2, 1, 2],
                 [2, 2, 1, 2, 2, 1, 1],
                 [1, 2, 2, 2, 1, 2, 2],
                 [2, 1, 1, 1, 2, 2, 1],
                 [2, 1, 2, 2, 1, 1, 2]]
        self.assertEqual(0, iterative_deepening(
            board, 2, 5, -1000000, 1000000, 41)[1])

    def test_blocking_win_situation(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 2, 1, 0],
                 [0, 0, 2, 2, 2, 1, 0],
                 [0, 0, 1, 2, 2, 1, 0]]

        self.assertEqual(5, iterative_deepening(
            board, 2, 5, -1000000, 1000000, 13)[0])

    def test_block_situation(self):  
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0],
                 [2, 0, 1, 1, 2, 0, 0],
                 [1, 0, 2, 2, 1, 0, 0],
                 [2, 1, 1, 1, 2, 2, 1],
                 [2, 1, 2, 2, 1, 1, 2]]

        self.assertEqual(1, iterative_deepening(
            board, 2, 1, -1000000, 1000000, 25)[0])

    def test_winning_move_situation(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 2, 2, 0],
                 [0, 0, 0, 2, 1, 2, 0],
                 [0, 0, 2, 1, 2, 1, 0],
                 [0, 0, 1, 2, 1, 1, 2]]

        self.assertEqual(1, iterative_deepening(
            board, 2, 2, -1000000, 1000000, 17)[0])

    def test_winning_move_situation_2(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 2, 2, 0],
                 [0, 0, 0, 2, 1, 2, 0],
                 [0, 0, 2, 1, 2, 1, 1],
                 [0, 0, 1, 2, 1, 1, 2]]

        self.assertEqual(1, iterative_deepening(
            board, 2, 6, -1000000, 1000000, 18)[0])

    def test_definitive_loss_in_5_moves(self):
        board = [[0, 0, 1, 1, 2, 0, 0],
                 [0, 0, 2, 2, 1, 0, 0],
                 [1, 0, 1, 2, 2, 0, 0],
                 [2, 0, 2, 2, 1, 0, 0],
                 [1, 0, 1, 1, 2, 2, 0],
                 [1, 0, 1, 2, 1, 2, 0]]

        self.assertNotEqual(
            5, iterative_deepening(board, 2, 0, -1000000, 1000000, 25)[0])
        move, value = iterative_deepening(
            board, 2, 0, -1000000, 1000000, 20)
        self.assertEqual(-9990 , value)

    def test_block_win_situation(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 2, 0, 0],
                 [0, 2, 1, 2, 1, 0, 0],
                 [0, 1, 2, 1, 2, 1, 0],
                 [0, 1, 1, 2, 1, 2, 0]]
        self.assertEqual(2, iterative_deepening(
            board, 2, 2, -1000000, 1000000, 17)[0])

    def test_block_win_situation_2(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0],
                 [0, 2, 1, 2, 1, 0, 0],
                 [0, 1, 2, 1, 2, 1, 0],
                 [0, 1, 1, 2, 1, 2, 0]]
        self.assertEqual(2, iterative_deepening(
            board, 2, 2, -1000000, 1000000, 16)[0])
        
    def test_win_ignored_in_two_moves(self):
        board =[[0, 0, 1, 2, 0, 0, 0],
                [0, 0, 2, 2, 2, 0, 0],
                [0, 0, 2, 2, 1, 0, 0],
                [0, 1, 2, 1, 1, 0, 0],
                [1, 1, 1, 2, 2, 1, 0],
                [2, 2, 1, 2, 1, 1, 0]]
        
        move, value = iterative_deepening(
            board, 2, 1, -1000000, 1000000, 10)
        board[2][move] = 2
        self.assertEqual(1, move)
        self.assertEqual(9998, value)

        board[3][0] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 1, -1000000, 1000000, 10)
        board[2][move] = 2
        self.assertEqual(1, move)
        self.assertEqual(10000, value)
    

    """Tests for multiple turns"""

    def test_win_in_4_moves(self):  # needs to reach depth 7
        board = [[0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 2, 2, 0, 0, 0],
                 [0, 0, 2, 2, 1, 0, 0],
                 [0, 1, 2, 1, 1, 0, 0],
                 [1, 1, 1, 2, 2, 0, 0],
                 [2, 2, 1, 2, 1, 0, 0]]


        move, value = iterative_deepening(
            board, 2, 0, -1000000, 1000000, 20)
        board[1][move] = 2
        self.assertEqual(4, move)
        self.assertEqual(9994 ,value)

        board[5][5] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 5, -1000000, 1000000, 18)
        board[0][move] = 2
        self.assertEqual(3, move)
        self.assertEqual(9996 ,value)

        board[3][0] = 1 # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 0, -1000000, 1000000, 16)
        board[2][move] = 2
        self.assertEqual(1, move)
        self.assertEqual(9998 ,value)

        board[2][0] = 1 # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 0, -1000000, 1000000, 14)
        board[1][move] = 2
        self.assertEqual(1, move)
        self.assertEqual(10000 ,value)

        self.assertEqual(True, check_winner(board,  0, 2))

    def test_win_in_5_moves(self):  # needs to reach depth 9
        board = [[0, 0, 1, 2, 0, 0, 0],
                 [0, 2, 1, 2, 2, 0, 0],
                 [0, 2, 1, 2, 1, 0, 0],
                 [0, 1, 2, 1, 1, 0, 0],
                 [0, 1, 2, 1, 2, 1, 0],
                 [0, 1, 2, 2, 1, 2, 0]]
        
        move, value = iterative_deepening(
            board, 2, 2, -1000000, 1000000, 25)
        board[3][move] = 2
        self.assertEqual(5, move)
        self.assertEqual(9990 ,value)

        board[2][5] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 5, -1000000, 1000000, 23)
        board[1][move] = 2
        self.assertEqual(5, move)
        self.assertEqual(9992 ,value)


        board[0][5] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 5, -1000000, 1000000, 21)
        board[5][move] = 2
        self.assertEqual(6, move)
        self.assertEqual(9994,value)


        board[4][6] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 6, -1000000, 1000000, 19)
        board[3][move] = 2
        self.assertEqual(6, move)
        self.assertEqual(9998 ,value)


        board[2][6] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 6, -1000000, 1000000, 17)
        board[1][move] = 2
        self.assertEqual(6, move)
        self.assertEqual(10000 ,value)

        self.assertEqual(True, check_winner(board, 5, 2))

    def test_another_win_in_5_moves(self):  # needs to reach depth 9
        board = [[0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 2, 2, 0, 0, 0],
                 [0, 1, 1, 1, 2, 0, 0],
                 [0, 1, 2, 2, 1, 1, 0]]
        
        move, value = iterative_deepening(
            board, 2, 1, -1000000, 1000000, 15)
        board[2][move] = 2
        self.assertEqual(2, move)
        self.assertEqual(9992 ,value)
        
        board[3][1] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 1, -1000000, 1000000, 17)
        board[2][move] = 2
        self.assertEqual(1, move)
        self.assertEqual(9994 ,value)

        board[1][1] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 1, -1000000, 1000000, 17)
        board[1][move] = 2
        self.assertEqual(2, move)
        self.assertEqual(9996 ,value)

        board[0][2] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 2, -1000000, 1000000, 17)
        board[3][move] = 2
        self.assertEqual(4, move)
        self.assertEqual(9998 ,value)

        board[0][1] = 1  # Opponents (players) move

        move, value = iterative_deepening(
            board, 2, 2, -1000000, 1000000, 17)
        board[2][move] = 2
        print(board[2])
        self.assertEqual(4, move)
        self.assertEqual(10000,value)

        self.assertEqual(True, check_winner(board, 5, 2))

    def test_loss_in_3_moves(self):
        board = [[0, 1, 0, 2, 2, 1, 1],
                 [0, 2, 0, 2, 1, 2, 2],
                 [0, 1, 0, 2, 2, 1, 1],
                 [0, 2, 0, 1, 2, 2, 2],
                 [1, 1, 1, 2, 1, 1, 1],
                 [2, 1, 2, 2, 1, 1, 2]]
        
        move, value = iterative_deepening(
            board, 2, 1, -1000000, 1000000, 10)
        board[4][move] = 2
        self.assertEqual(0, move)
        self.assertEqual(-9994, value)
