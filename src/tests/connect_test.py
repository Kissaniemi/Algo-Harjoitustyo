import unittest
from collections import deque
from connect import check_winner, possible_columns, drop_piece, check_full, check_top, evaluate, score_position, \
    check_winner_vertical, check_winner_horizontal, check_winner_diagonal_1, check_winner_diagonal_2


class TestConnect(unittest.TestCase):
    def setUp(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]
        self.column_order = [3, 2, 4, 1, 5, 0, 6] 

    """possible_columns tests"""

    def test_possible_columns_all(self):
        board = self.board
        self.assertEqual(deque([3, 2, 4, 1, 5, 0, 6]),
                         possible_columns(board, self.column_order))

    def test_possible_columns_some(self):
        board = [[0, 0, 0, 1, 2, 0, 2],
                 [0, 0, 0, 2, 1, 0, 2],
                 [0, 0, 0, 2, 2, 0, 1],
                 [0, 0, 0, 2, 1, 1, 1],
                 [0, 0, 0, 2, 1, 2, 2],
                 [0, 0, 0, 1, 2, 2, 1]]
        self.assertEqual(deque([2, 1, 5, 0]), possible_columns(board, self.column_order))

    def test_possible_columns_none(self):
        board = [[2, 1, 1, 1, 2, 1, 2],
                 [2, 1, 2, 2, 1, 2, 2],
                 [2, 1, 1, 2, 2, 1, 1],
                 [1, 2, 2, 2, 1, 1, 1],
                 [1, 1, 1, 2, 1, 2, 2],
                 [1, 2, 2, 1, 2, 2, 1]]
        self.assertEqual(deque(), possible_columns(board, self.column_order))

    """drop_piece tests"""

    def test_drop_piece(self):
        board = self.board
        compare_board = [[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 0, 0]]
        self.assertEqual(compare_board, drop_piece(1, board, 3))

    def test_drop_piece_false(self):
        board = [[0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0]]
        self.assertEqual(False, drop_piece(1, board, 3))

    """check_full tests"""

    def test_check_full(self):
        board = [[1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0]]
        self.assertEqual(True, check_full(board))

    def test_check_full_false(self):
        board = self.board
        self.assertEqual(False, check_full(board))

    """check_top tests"""

    def test_check_top_top(self):
        board = [[0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0]]
        self.assertEqual(-6, check_top(board, 3))

    def test_check_top_bottom(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(0, check_top(board, 3))

    """check_winner tests"""

    def test_vertical_check(self):
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(False, check_winner_vertical(board,  0, -3, 1))
        board[-4][0] = 1
        self.assertEqual(True, check_winner_vertical(board,  0, -4, 1))

    def test_vertical_check_top(self):
        board = [
            [2, 0, 1, 0, 0, 0, 0],
            [2, 0, 1, 0, 2, 0, 0],
            [1, 0, 1, 0, 1, 0, 0],
            [2, 2, 1, 2, 1, 0, 0],
            [2, 2, 2, 1, 2, 1, 0],
            [2, 2, 1, 2, 1, 1, 0]]
        self.assertEqual(True, check_winner_vertical(board,  2, -6, 1))

    def test_horizontal_check_down(self):
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0]]
        self.assertEqual(True, check_winner_horizontal(board,  3, -1, 1))
        self.assertEqual(True, check_winner_horizontal(board,  2, -1, 1))
        self.assertEqual(True, check_winner_horizontal(board,  1, -1, 1))
        self.assertEqual(True, check_winner_horizontal(board,  0, -1, 1))
        board[-1][2] = 0
        self.assertEqual(False, check_winner_horizontal(board, 3, -1, 1))
        self.assertEqual(False, check_winner_horizontal(board, 1, -1, 1))
        self.assertEqual(False, check_winner_horizontal(board, 0, -1, 1))

    def test_horizontal_check_top(self):
        board = [
            [0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(True, check_winner_horizontal(board,  6, -6, 1))
        self.assertEqual(True, check_winner_horizontal(board,  5, -6, 1))
        self.assertEqual(True, check_winner_horizontal(board, 4, -6, 1))
        self.assertEqual(True, check_winner_horizontal(board, 3, -6, 1))
        board[-6][3] = 0
        board[-6][2] = 1
        self.assertEqual(False, check_winner_horizontal(board,  2, -6, 1))
        self.assertEqual(False, check_winner_horizontal(board, 1, -6, 1))
        self.assertEqual(False, check_winner_horizontal(board, 0, -6, 1))

    def test_diagonal_check_down_1(self):
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(True, check_winner_diagonal_1(board,  0, -1, 1))
        self.assertEqual(True, check_winner_diagonal_1(board,  1, -2, 1))
        self.assertEqual(True, check_winner_diagonal_1(board,  2, -3, 1))
        self.assertEqual(True, check_winner_diagonal_1(board,  3, -4, 1))
        board[-3][2] = 0
        self.assertEqual(False, check_winner_diagonal_1(board,  0, -1, 1))
        self.assertEqual(False, check_winner_diagonal_1(board,  1, -2, 1))
        self.assertEqual(False, check_winner_diagonal_1(board,  3, -4, 1))

    def test_diagonal_check_down_2(self):
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0]]
        self.assertEqual(True, check_winner_diagonal_2(board,  4, -1, 1))
        self.assertEqual(True, check_winner_diagonal_2(board,  3, -2, 1))
        self.assertEqual(True, check_winner_diagonal_2(board,  2, -3, 1))
        self.assertEqual(True, check_winner_diagonal_2(board,  1, -4, 1))
        board[-3][2] = 0
        self.assertEqual(False, check_winner_diagonal_2(board,  4, -1, 1))
        self.assertEqual(False, check_winner_diagonal_2(board,  3, -2, 1))
        self.assertEqual(False, check_winner_diagonal_2(board,  1, -4, 1))

    def test_diagonal_check_up_1(self):
        board = [[0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0],
                 [0, 0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(True, check_winner_diagonal_2(board,  6, -3, 2))
        self.assertEqual(True, check_winner_diagonal_2(board,  5, -4, 2))
        self.assertEqual(True, check_winner_diagonal_2(board,  4, -5, 2))
        self.assertEqual(True, check_winner_diagonal_2(board,  3, -6, 2))
        board[-5][4] = 0
        self.assertEqual(False, check_winner_diagonal_2(board,  6, -3, 2))
        self.assertEqual(False, check_winner_diagonal_2(board,  5, -4, 2))
        self.assertEqual(False, check_winner_diagonal_2(board,  3, -6, 2))

    def test_diagonal_check_up_2(self):
        board = [[0, 0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 0, 0, 2, 0],
                 [0, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(True, check_winner_diagonal_1(board,  3, -3, 2))
        self.assertEqual(True, check_winner_diagonal_1(board,  4, -4, 2))
        self.assertEqual(True, check_winner_diagonal_1(board,  5, -5, 2))
        self.assertEqual(True, check_winner_diagonal_1(board,  6, -6, 2))
        board[-4][4] = 0
        self.assertEqual(False, check_winner_diagonal_1(board,  3, -3, 2))
        self.assertEqual(False, check_winner_diagonal_1(board,  5, -5, 2))
        self.assertEqual(False, check_winner_diagonal_1(board,  6, -6, 2))

    def test_full_check_winner(self):
        board = [
            [2, 0, 1, 0, 0, 0, 0],
            [2, 0, 1, 0, 2, 0, 0],
            [1, 0, 1, 0, 1, 0, 0],
            [2, 2, 1, 2, 1, 0, 0],
            [2, 2, 2, 1, 2, 1, 0],
            [2, 2, 1, 2, 1, 1, 0]]
        self.assertEqual(True, check_winner(board,  2, 1))

    def test_full_check_no_winner(self):
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0]]
        self.assertEqual(False, check_winner(board, 3, 1))

    """evaluate tests"""

    def test_evaluate(self):
        section = [0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(0, evaluate(section, 2))

    def test_evaluate_gap(self):
        section1 = [2, 0, 2, 2, 0, 0, 0]
        section2 = [0, 0, 0, 2, 2, 0, 2]
        self.assertEqual(evaluate(section1, 2), evaluate(section2, 2))
