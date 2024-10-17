import unittest
from collections import deque
from connect import check_winner, possible_columns, preferred_order, drop_piece, check_full, check_top

class TestConnect(unittest.TestCase):
    def setUp(self):
        self.board =[[0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0]]

    def test_horizonal_check(self):
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [1,1,1,0,0,0,0]]
        self.assertEqual(False, check_winner(board, 0, 1))
        board[-1][4] = 1
        self.assertEqual(False, check_winner(board,  0, 1))
        board[-1][3] = 1
        self.assertEqual(True, check_winner(board,  3, 1))
        self.assertEqual(True, check_winner(board,  2, 1))
        self.assertEqual(True, check_winner(board,  1, 1))
        self.assertEqual(True, check_winner(board,  0, 1))

    def test_vertical_check(self):
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0], 
            [1,0,0,0,0,0,0]]
        self.assertEqual(False, check_winner(board,  0, 1))
        board[-4][0] = 1
        self.assertEqual(True, check_winner(board,  0, 1))

    def test_vertical_check_top(self):
        board = [
            [2, 0, 1, 0, 0, 0, 0],
            [2, 0, 1, 0, 2, 0, 0],
            [1, 0, 1, 0, 1, 0, 0],
            [2, 2, 1, 2, 1, 0, 0],
            [2, 2, 2, 1, 2, 1, 0],
            [2, 2, 1, 2, 1, 1, 0]]
        self.assertEqual(True, check_winner(board,  2, 1))

    def test_diagonal_right_check(self):
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,1,0,0,0,0,0], 
            [1,0,0,0,0,0,0]]
        self.assertEqual(False, check_winner(board,  0, 1))
        board[-5][4] = 1
        self.assertEqual(False, check_winner(board,  0, 1))
        board[-4][3] = 1
        self.assertEqual(True, check_winner(board,  0, 1))
        board[-3][2] = 0
        self.assertEqual(False, check_winner(board,  0, 1))

    def test_diagonal__left_check(self):
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,0,1,0,0,0], 
            [0,0,0,0,1,0,0]]
        self.assertEqual(False, check_winner(board,  4, 1))
        board[-5][0] = 1
        self.assertEqual(False, check_winner(board,  4, 1))
        board[-4][1] = 1
        self.assertEqual(True, check_winner(board,  4, 1))
        board[-3][2] = 0
        self.assertEqual(False, check_winner(board,  4, 1))

    
    def test_possible_columns(self):
        board = self.board
        self.assertEqual(deque([0,1,2,3,4,5,6]), possible_columns(1, board))

    def test_preferred_order(self):
        columns = deque([0,1,2,3,4,5,6])
        self.assertEqual(deque([3,2,4,1,5,0,6]), preferred_order(columns))

    def test_drop_piece(self):
        board = self.board
        compare_board = [[0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0], 
                        [0,0,0,1,0,0,0]]
        self.assertEqual(compare_board, drop_piece(1, board, 3))

    def test_drop_piece_false(self):
        board = [[0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0], 
                [0,0,0,1,0,0,0]]
        self.assertEqual(False, drop_piece(1, board, 3))

    def test_check_full(self):
        board = [[1,1,1,1,1,1,1],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0], 
                [0,0,0,1,0,0,0]]
        self.assertEqual(True, check_full(board))


    def test_check_full_false(self):
        board = self.board
        self.assertEqual(False, check_full(board))

    def test_check_top(self):
        board = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0], 
                [0,0,0,1,0,0,0]]
        self.assertEqual(-4, check_top(board,3))

    def test_check_top_top(self):
        board = [[0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0], 
                [0,0,0,1,0,0,0]]
        self.assertEqual(-6, check_top(board,3))

    def test_check_top_bottom(self):
        board = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0]]
        self.assertEqual(0, check_top(board,3))
