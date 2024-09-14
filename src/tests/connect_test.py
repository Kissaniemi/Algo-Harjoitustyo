import unittest
from connect import check_winner

class TestConnect(unittest.TestCase):
    def setUp(self):
        pass

    def test_horizonal_check(self):
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [1,1,1,0,0,0,0]]
        self.assertEqual(False, check_winner(board, -1, 0, 1))
        board[-1][4] = 1
        self.assertEqual(False, check_winner(board, -1, 0, 1))
        board[-1][3] = 1
        self.assertEqual(True, check_winner(board, -1, 3, 1))
        self.assertEqual(True, check_winner(board, -1, 2, 1))
        self.assertEqual(True, check_winner(board, -1, 1, 1))
        self.assertEqual(True, check_winner(board, -1, 0, 1))

    def test_vertical_check(self):
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0], 
            [1,0,0,0,0,0,0]]
        self.assertEqual(False, check_winner(board, -3, 0, 1))
        board[-4][0] = 1
        self.assertEqual(True, check_winner(board, -4, 0, 1))

    def test_diagonal_right_check(self):
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,1,0,0,0,0,0], 
            [1,0,0,0,0,0,0]]
        self.assertEqual(False, check_winner(board, -1, 0, 1))
        board[-5][4] = 1
        self.assertEqual(False, check_winner(board, -1, 0, 1))
        board[-4][3] = 1
        self.assertEqual(True, check_winner(board, -1, 0, 1))
        board[-3][2] = 0
        self.assertEqual(False, check_winner(board, -1, 0, 1))

    def test_diagonal__left_check(self):
        board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,0,1,0,0,0], 
            [0,0,0,0,1,0,0]]
        self.assertEqual(False, check_winner(board, -1, 4, 1))
        board[-5][0] = 1
        self.assertEqual(False, check_winner(board, -1, 4, 1))
        board[-4][1] = 1
        self.assertEqual(True, check_winner(board, -1, 4, 1))
        board[-3][2] = 0
        self.assertEqual(False, check_winner(board, -1, 4, 1))





    

    





