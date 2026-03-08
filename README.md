# Maze Solver using BFS

**Name:** Yunus Emre Yesilagac  
**P Number:** P475851  
**Module:** Artificial Intelligence (IY496)

## Project Description

This project is a Python program that solves a maze using the Breadth First Search (BFS) algorithm.

The program reads the maze from a text file and finds the shortest distance from the start position to the finish position. The start position is the top-left corner of the maze `(0,0)` and the finish position is the bottom-right corner.

## Maze Representation

The maze is stored in a file called `maze.txt`.

- `0` = free path
- `1` = wall

The program reads the maze file and stores it as a 2D list.

## Algorithm Used

This project uses **Breadth First Search (BFS)**.

BFS is a good choice for this task because it explores the maze level by level. This means the first time the finish square is reached, the program has found the shortest path.

The algorithm checks movement in four directions:

- Up
- Down
- Left
- Right

A queue is used to store the next positions to explore.

## Program Functions

### `read_maze()`
Reads the maze from the text file.

### `is_safe()`
Checks if moving to a new square is valid.

### `bfs()`
Performs Breadth First Search and finds the shortest distance.

### `print_result()`
Prints the result to the screen.

## Project Structure

```text
AI-Maze-Solver
├── maze_solver.py
├── maze.txt
└── README.md
```

## How to Run

Run the following command in the terminal:

```bash
python maze_solver.py
```

Example output:

```text
Shortest distance: 14
```

## References

- GeeksforGeeks, Breadth First Search (BFS) for Artificial Intelligence
- GeeksforGeeks, Shortest Path in a Binary Maze
- CodeRivers, Python Matrix Manipulation

## Author

**Yunus Emre Yesilagac**  
**P Number:** P475851
