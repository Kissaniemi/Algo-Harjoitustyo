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


    def test_block_vertical(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0],
                [0,0,1,0,0,0,0], 
                [0,0,1,0,0,0,0]]
  
        self.assertEqual(2, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_block_horizontal(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0], 
                [1,1,1,0,0,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_block_diagonal_right(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0],
                [0,1,0,0,0,0,0],
                [0,0,1,0,0,0,0], 
                [0,0,0,0,0,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_block_diagonal_right_2(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0],
                [2,1,0,0,0,0,0],
                [2,2,1,0,0,0,0], 
                [2,2,1,0,0,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])


    def test_block_diagonal_left(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1],
                [0,0,0,0,0,1,2],
                [0,0,0,0,1,2,2], 
                [0,0,0,0,1,2,2]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])


    def test_winning_move_vertical(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,2,0,0,0,0],
                [0,0,2,0,0,0,0], 
                [0,0,2,0,0,0,0]]
  
        self.assertEqual(2, minmax(board, 2, float("-inf"), float("inf"))[0])


    def test_winning_move_horizontal(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0], 
                [2,2,2,0,0,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_winning_move_diagonal_right(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [2,0,0,0,0,0,0],
                [0,2,0,0,0,0,0],
                [0,0,2,0,0,0,0], 
                [0,0,0,0,0,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_winning_move_diagonal_left(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2],
                [0,0,0,0,0,2,0],
                [0,0,0,0,2,0,0], 
                [0,0,0,0,0,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])
    

    def test_winning_move_before_opponent_4(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [2,0,0,0,0,0,0],
                [0,2,0,0,0,0,1],
                [0,0,2,0,0,0,1], 
                [0,0,0,0,0,0,1]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_winning_move_before_opponent_5(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1],
                [0,0,0,0,0,0,1], 
                [2,2,2,0,0,0,1]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_winning_move_before_opponent_6(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [2,0,0,0,0,0,1],
                [2,0,0,0,0,0,1], 
                [2,0,0,0,0,0,1]]
  
        self.assertEqual(0, minmax(board, 2, float("-inf"), float("inf"))[0])


    def test_block_diagonal_left_up(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1],
                [0,0,0,0,1,2,2], 
                [0,0,0,1,2,2,1]]
  
        self.assertEqual(6, minmax(board, 2, float("-inf"), float("inf"))[0])


    def test_block_situation(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,1,2,0,0],
                [2,0,1,1,2,0,0],
                [1,0,2,2,1,0,0],
                [2,1,1,1,2,2,1], 
                [2,1,2,2,1,1,2]]
  
        self.assertEqual(1, minmax(board, 2, float("-inf"), float("inf"))[0])



    def test_winning_move_before_opponent(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2],
                [1,0,0,0,0,2,0],
                [1,0,0,0,2,0,0], 
                [1,0,0,0,0,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_winning_move_before_opponent_2(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [1,0,0,0,0,0,2],
                [1,0,0,0,0,0,2], 
                [1,0,0,0,0,0,2]]
  
        self.assertEqual(6, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_winning_move_before_opponent_3(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0],
                [1,0,0,0,0,0,0], 
                [1,0,0,0,2,2,2]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])


    def test_winning_move_vs_opp_before(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,1,2,0,0,0],
                [0,0,1,2,0,0,0], 
                [0,0,1,2,0,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])

    

    def test_winning_move_vs_opp_before_2(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,1,0,2,0,0,0],
                [0,1,0,2,0,0,0], 
                [0,1,0,2,0,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])
    


    def test_winning_move_vs_opp_after(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,2,1,0,0],
                [0,0,0,2,1,0,0], 
                [0,0,0,2,1,0,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])


    def test_winning_move_vs_opp_after_2(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,2,0,1,0],
                [0,0,0,2,0,1,0], 
                [0,0,0,2,0,1,0]]
  
        self.assertEqual(3, minmax(board, 2, float("-inf"), float("inf"))[0])

    def test_winning_move_vs_opp_after_3(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,2,0,0,0,0],
                [0,0,2,0,0,0,0], 
                [0,0,2,0,1,1,1]]
  
        self.assertEqual(2, minmax(board, 2, float("-inf"), float("inf"))[0])



    def test_blocking_win(self):
        board = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0],
                [0,0,0,1,2,1,0],
                [0,0,2,2,2,1,0], 
                [0,0,1,2,2,1,0]]
        
        self.assertEqual(5, minmax(board, 2, float("-inf"), float("inf"))[0])
        

    def test_winning_move_situation(self):
        board =[[0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0],
                [0,0,0,1,2,2,0],
                [0,0,0,2,1,2,0],
                [0,0,2,1,2,1,0], 
                [0,0,1,2,1,1,2]]
  
        self.assertEqual(1, minmax(board, 2, float("-inf"), float("inf"))[0])