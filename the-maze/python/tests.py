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
        expected_solution = [
            [1,1],
            [2,1],
            [3,1],
            [4,1],
            [5,1],
            [5,2],
            [5,3],
            [6,3],
            [6,4],
            [6,5],
            [5,5],
            [5,6],
            [5,7],
            [5,8],
            [4,8],
            [3,8],
            [2,8],
            [1,8],
            [1,9]

        ]
        results = solve_maze(maze, [1,0], [1,9])

        self.assertEquals(solution, expected_solution)

