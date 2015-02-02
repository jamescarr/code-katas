from unittest import TestCase
from solver import solve_maze

maze = [  [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
          [0,  0,  1,  0,  0,  0,  0,  1,  0,  0],
          [1,  0,  1,  0,  1,  1,  0,  1,  0,  1],
          [1,  0,  0,  0,  1,  0,  0,  1,  0,  1],
          [1,  0,  1,  1,  1,  1,  1,  1,  0,  1],
          [1,  0,  0,  0,  1,  0,  0,  0,  0,  1],
          [1,  0,  1,  0,  0,  0,  1,  1,  0,  1],
          [1,  0,  1,  1,  1,  1,  1,  1,  0,  1],
          [1,  0,  0,  0,  0,  1,  0,  0,  0,  1],
          [1,  1,  1,  1,  1,  1,  1,  1,  1,  1]  ]

class MazeSolverTest(TestCase):
    def test_solve_maze(self):
        solve_maze()

