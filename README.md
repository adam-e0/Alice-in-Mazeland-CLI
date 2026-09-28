# Alice-in-Mazeland-CLI

A python implementation of the Alice in Mazeland game

Example gameplay:

```python
Enter maze file path: mazes/maze-1.txt
2 rows, 3 columns
Starting position: [1, 1]
Ending position: [1, 3]

Player current position: (1, 1)
Step size: 1
⬛️⬛️🏃⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬜️✳️⬜️⬛️⬜️⏺️➡️⬛️⬜️🏁⬜️⬛️
⬛️⬜️⬇️↘️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬆️↗️⬛️⬜️⬜️⬜️⬛️↖️⬜️⬜️⬛️
⬛️⬜️🍰➡️⬛️⬅️⏺️➡️⬛️⬅️🥤⬜️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
Possible Moves: (⬇️ : X) (↘️ : C)
Enter next move: X

Player current position: (2, 1)
Step size: 1
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬜️✳️⬜️⬛️⬜️⏺️➡️⬛️⬜️🏁⬜️⬛️
⬛️⬜️⬇️↘️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️🏃⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬆️↗️⬛️⬜️⬜️⬜️⬛️↖️⬜️⬜️⬛️
⬛️⬜️🍰➡️⬛️⬅️⏺️➡️⬛️⬅️🥤⬜️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
Possible Moves: (➡️ : D) (⬆️ : W) (↗️ : E)
Enter next move: D

Player current position: (2, 3)
Step size: 2
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬜️✳️⬜️⬛️⬜️⏺️➡️⬛️⬜️🏁⬜️⬛️
⬛️⬜️⬇️↘️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️🏃⬛️⬛️
⬛️⬜️⬆️↗️⬛️⬜️⬜️⬜️⬛️↖️⬜️⬜️⬛️
⬛️⬜️🍰➡️⬛️⬅️⏺️➡️⬛️⬅️🥤⬜️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
Possible Moves: (↖️ : Q) (⬅️ : A)
Enter next move: Q

Player current position: (1, 2)
Step size: 1
⬛️⬛️⬛️⬛️⬛️⬛️🏃⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬜️✳️⬜️⬛️⬜️⏺️➡️⬛️⬜️🏁⬜️⬛️
⬛️⬜️⬇️↘️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬆️↗️⬛️⬜️⬜️⬜️⬛️↖️⬜️⬜️⬛️
⬛️⬜️🍰➡️⬛️⬅️⏺️➡️⬛️⬅️🥤⬜️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
Possible Moves: (➡️ : D)
Enter next move: D
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️🏃⬛️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬜️✳️⬜️⬛️⬜️⏺️➡️⬛️⬜️🏁⬜️⬛️
⬛️⬜️⬇️↘️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬆️↗️⬛️⬜️⬜️⬜️⬛️↖️⬜️⬜️⬛️
⬛️⬜️🍰➡️⬛️⬅️⏺️➡️⬛️⬅️🥤⬜️⬛️
⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
You Win!
Game statistics
Total moves: 4
Playthrough history:
(1, 1)
(2, 1)
(2, 3)
(1, 2)
```

# How to run the game

1. Clone the repository:

```
git clone https://github.com/adam-e0/Alice-in-Mazeland-CLI
cd Alice-in-Mazeland
```

2. Run the Python file

```
python3 game.py
```

The game will prompt you for a maze file. There are example mazes in the mazes/ folder that you can use.

```
Enter maze file path: mazes/maze-1.txt
```

# Game Rules

You are dropped onto a board with starting and ending squares. Your goal is to traverse the board to go from the starting square to the ending square. Every square has a limited set of directions you can move. Some squares may contain a cake or a drink. Landing on a square with a cake will increase your stride length by 1. Landing on a square with a drink will decrease your stride length by 1. You start on the board with a stride length of 1. If your stride length becomes 0, then the game ends. If your stide length becomes to larger than the board, the game ends. Landing on a square with no possible moves will also end the game.

# Maze format

Each line has 3 sections seperated by `::`.
The first line is the maze header which includes the rows and collumns of the maze, maze starting cell, and the maze ending cell.

```
rows columns :: startY startX :: endY endX
```

All of the next lines are the values of each cell wich includes the cell cordinates, possible moves from that cell, and the cell effect.

There are 9 possible moves for every cell and they are N, NE, E, SE, S, SW, W, NW, and X, where X means that there is no direction you can move from that cell.

There are 3 possible cell effects, N, I, and D. N stands for no effect, D (drink) stands for decrease step amount, and I (cake) stands for increase step amount.

Example Maze:

```
2 3 :: 1 1 :: 1 3
1 1 :: S SE :: N
1 2 :: E :: N
1 3 :: X :: N
2 1 :: E N NE :: I
2 2 :: E W :: N
2 3 :: NW W :: D
```
