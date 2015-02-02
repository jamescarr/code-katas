# A-Maze Me

## The Kata
Given a maze represented by an array of arrays, write a function to find
the shortest path between two points in the maze.

## The Maze

maze =
  [  [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
     [0,  0,  1,  0,  0,  0,  0,  1,  0,  0],
     [1,  0,  1,  0,  1,  1,  0,  1,  0,  1],
     [1,  0,  0,  0,  1,  0,  0,  1,  0,  1],
     [1,  0,  1,  1,  1,  1,  1,  1,  0,  1],
     [1,  0,  0,  0,  1,  0,  0,  0,  0,  1],
     [1,  0,  1,  0,  0,  0,  1,  1,  0,  1],
     [1,  0,  1,  1,  1,  1,  1,  1,  0,  1],
     [1,  0,  0,  0,  0,  1,  0,  0,  0,  1],
     [1,  1,  1,  1,  1,  1,  1,  1,  1,  1]  ]


Where:
  0 - open
  1 - wall

Starting Point: 1,0
End Point: 1,9

## Expected Output
Disply the solved path, either by listing the coordinates of each move
or even display the solved graph itself if you're fancy!


## Tips

- [Solving mazes using Python: Simple recursivity and A* search](http://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/) - examples of how to do it using two different algorithms. 
- [Maze Solving on Rosetta Code](http://rosettacode.org/wiki/Maze_solving#Python) - honestly not a fan of this one but it's quite educational. Uses the [Dijkstra Algorithm](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to solve. 

