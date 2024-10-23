import unittest
from minmax import minmax

class TestConnect(unittest.TestCase):
    def setUp(self):
        self.board =[[0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0]]
        
    def test_best_start_next_move(self):
        self.assertEqual(3, minmax(self.board, 2, float("-inf"), float("inf"))[0])

    def test_winning_move_block(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0],
                [0,0,1,0,0,0,0], 
                [0,0,1,0,0,0,0]]
  
        self.assertEqual(2, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_winning_move(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,2,0,0,0,0],
                [0,0,2,0,0,0,0], 
                [0,0,2,0,0,0,0]]
  
        self.assertEqual(2, minmax(board, 2, float("-inf"), float("inf"))[0])

