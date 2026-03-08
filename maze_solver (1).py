"""
I confirm that this assignment is my own work.

Name: Yunus Emre Yesilagac
P Number: P475851

This program solves a maze using the Breadth First Search (BFS) algorithm.
The maze is read from a text file before the search starts. In the maze,
0 means the square is open and 1 means the square is a wall.

The start position is the top-left corner of the maze at (0,0). The finish
position is the bottom-right corner. The aim of the program is to find the
shortest distance from the start to the finish.

I chose BFS because it is a suitable algorithm for this type of problem.
It explores the maze level by level, so the first time the finish position
is reached, the distance found is the shortest one. This makes BFS a good
choice for an unweighted maze.

The program is divided into separate functions to make it easier to read
and understand. One function reads the maze from the file, one function
checks whether a move is safe, one function performs the BFS search, and
one function prints the result. The search checks movement in four
directions: up, down, left, and right.

If there is a path from the start to the finish, the program prints the
shortest distance. If there is no valid path, the program prints a message
to say that no path was found.
"""

# References
# https://www.geeksforgeeks.org/breadth-first-search-bfs-for-artificial-intelligence/
# https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/
# https://coderivers.org/blog/python-matrix-manipulation/

from collections import deque


# Name: read_maze
# Function description: Reads the maze data from a text file.
# Inputs: filename - the name of the text file containing the maze.
# Outputs: Returns the maze as a 2D list.
# Function process: Opens the file, reads each line, converts values to integers,
# and stores them as rows in a list.
def read_maze(filename):
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            maze.append(row)
    return maze


# Name: is_safe
# Function description: Checks if a move to a new square is valid.
# Inputs: maze, visited, row, col
# Outputs: Returns True if the move is valid, otherwise False.
# Function process: Checks boundaries, checks if the square is not a wall,
# and checks if it has not been visited before.
def is_safe(maze, visited, row, col):
    rows = len(maze)
    cols = len(maze[0])

    if row >= 0 and row < rows and col >= 0 and col < cols:
        if maze[row][col] == 0 and not visited[row][col]:
            return True

    return False


# Name: bfs
# Function description: Performs Breadth First Search on the maze.
# Inputs: maze - the 2D list representing the maze.
# Outputs: Returns the shortest distance if a path exists, otherwise -1.
# Function process: Uses a queue to explore neighbouring squares level by level
# until the finish square is reached or all possible squares are checked.
def bfs(maze):
    rows = len(maze)
    cols = len(maze[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()

    queue.append((0, 0, 0))
    visited[0][0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col, distance = queue.popleft()

        if row == rows - 1 and col == cols - 1:
            return distance

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if is_safe(maze, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, distance + 1))

    return -1


# Name: print_result
# Function description: Prints the result of the search.
# Inputs: distance - the shortest distance found by BFS.
# Outputs: Prints the result to the screen.
# Function process: Checks if a path exists and prints the correct message.
def print_result(distance):
    if distance == -1:
        print("No path found")
    else:
        print("Shortest distance:", distance)


# Main program
maze = read_maze("maze.txt")
shortest_distance = bfs(maze)
print_result(shortest_distance)
