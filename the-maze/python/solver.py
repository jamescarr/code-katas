def solve_maze(maze, start, end, visited=[]):
    if start == end:
        return visited

    east = [start[0],start[1]+1]
    if get_coords(maze, east[0], east[1]) == 0:
        return solve_maze(maze, east, end, visited)
    return visited


def get_coords(maze, x, y):
    if len(maze) > x and len(maze[x]) > y:
        return maze[x][y]
    return None

