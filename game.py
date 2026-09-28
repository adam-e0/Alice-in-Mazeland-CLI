def printBoard(b, w, h, s, e, p):
    # Prints out the current game state with emojis

    # Each line of the output is stored as a string in an array
    output = []
    for y in range(h):
        # If the player is on the same y level as the current
        # black bar being made then add the player emoji
        # above the cell they are on
        if p[0] - 1 == y:
            output.append(
                ("⬛️" * (((p[1] - 1) * 4) + 2))
                + "🏃"
                + ("⬛️" * (((width - p[1] + 1) * 4) - 2))
                + "\n⬛️"
            )
        else:
            # Make black bar
            output.append(("⬛️" * ((width * 4) + 1)) + "\n⬛️")
        output.append("⬛️")
        output.append("⬛️")
        for x in range(w):
            # Dictionary for turning directions into emojis
            dirs = {
                "N": "⬆️ ",
                "NE": "↗️ ",
                "E": "➡️ ",
                "SE": "↘️ ",
                "S": "⬇️ ",
                "SW": "↙️ ",
                "W": "⬅️ ",
                "NW": "↖️ ",
                "X": "",
            }
            # Adds the directions if they exist on a square
            # and a blank emoji otherwise
            dirsList = list(dirs.keys())
            for d in b[f"{y + 1} {x + 1}"]["dir"]:
                dirsList.remove(d)
            for d in dirsList:
                dirs[d] = "⬜️"
            # Add the center cell based on the current cell effect
            states = {"N": "⏺️ ", "I": "🍰", "D": "🥤"}
            center = states[b[f"{y + 1} {x + 1}"]["state"]]
            # Custom centers for starting and ending cells
            if y + 1 == s[0] and x + 1 == s[1]:
                center = "✳️ "
            if y + 1 == e[0] and x + 1 == e[1]:
                center = "🏁"
            # Add the vertical black border between cells
            top = dirs["NW"] + dirs["N"] + dirs["NE"] + "⬛️"
            mid = dirs["W"] + center + dirs["E"] + "⬛️"
            bot = dirs["SW"] + dirs["S"] + dirs["SE"] + "⬛️"
            # Add cell to output
            output[y * 3] += top
            output[y * 3 + 1] += mid
            output[y * 3 + 2] += bot
    # Print out final result
    print("\n".join(output))
    print("⬛️" * ((width * 4) + 1))


def validMove(pos, dir, step, w, h):
    # Outputs true if direction from a cell brings you to a valid cell
    # based on stride length
    newPos = [pos[0] + (dir[0] * step), pos[1] + (dir[1] * step)]
    # Checks if new position is out of bounds
    if newPos[0] < 0 or newPos[0] > h:
        return False
    if newPos[1] < 0 or newPos[1] > w:
        return False
    return True


# Get maze file and read it
maze = open(input("Enter maze file path: "), "r", encoding="utf-8").read().split("\n")
# First line of file is the maze header
header = maze.pop(0).split(" :: ")
# Height and width of the game board
height = int(header[0].split(" ")[0])
width = int(header[0].split(" ")[1])
# The cordinates of the starting and ending squares
start = [int(header[1].split(" ")[0]), int(header[1].split(" ")[1])]
end = [int(header[2].split(" ")[0]), int(header[2].split(" ")[1])]

print(f"{height} rows, {width} columns")
print(f"Starting position: {start}")
print(f"Ending position: {end}")

# Creates keys for all of the cells
board = {}
for y in range(1, height + 1):
    for x in range(1, width + 1):
        board[f"{y} {x}"] = {"dir": [], "state": ""}
# Enters the values for all of the cells
for i in range(width * height):
    line = maze[i].split(" :: ")
    board[line[0]]["dir"] = line[1].split(" ")
    board[line[0]]["state"] = line[2]
    # Starting square must have no effect
    if line[0] == f"{start[0]} {start[1]}":
        board[line[0]]["state"] = "N"
    # Ending Square must have no effect and no directions
    if line[0] == f"{end[0]} {end[1]}":
        board[line[0]]["dir"] = "X"
        board[line[0]]["state"] = "N"

# Player starts on the starting square
playerPos = [start[0], start[1]]
# Player starts at a stride length of 1
steps = 1
# Maximum stride length
maxSteps = max(width, height) - 1
# Dictionary for displaying directions as keypresses
moves = {
    "N": "(⬆️ : W) ",
    "NE": "(↗️ : E) ",
    "E": "(➡️ : D) ",
    "SE": "(↘️ : C) ",
    "S": "(⬇️ : X) ",
    "SW": "(↙️ : Z) ",
    "W": "(⬅️ : A) ",
    "NW": "(↖️ : Q) ",
}
# Dictionary for converting keypresses to directions
moveToDir = {
    "W": "N",
    "E": "NE",
    "D": "E",
    "C": "SE",
    "X": "S",
    "Z": "SW",
    "A": "W",
    "Q": "NW",
}
# Dictionary to convert direction to vector
dirDict = {
    "N": [-1, 0],
    "NE": [-1, 1],
    "E": [0, 1],
    "SE": [1, 1],
    "S": [1, 0],
    "SW": [1, -1],
    "W": [0, -1],
    "NW": [-1, -1],
}

# Array for storing the steps a player took
cellHistory = []
# Loop goes until player reaches end cell or break statement is reached
while playerPos != end:
    # Add current cell to cell history
    cellHistory.append(playerPos)
    currentCell = board[f"{playerPos[0]} {playerPos[1]}"]
    print()
    print(f"Player current position: ({playerPos[0]}, {playerPos[1]})")
    print(f"Step size: {steps}")
    # Prints the emoji board
    printBoard(board, width, height, start, end, playerPos)
    # If current cell effect is I (cake) increase the stride length by 1
    # If current cell effect is D (drink) decrease the stride length by 1
    if currentCell["state"] == "I":
        steps += 1
    elif currentCell["state"] == "D":
        steps -= 1
    # If player lands on square with no directions
    # or has a stride length of 0
    # or has a stride length of more than the maximum
    # then the game ends because there is no where the player can go
    if "X" in currentCell["dir"] or steps == 0 or steps > maxSteps:
        print("You cannot move anymore!\nGame Over")
        break
    # Checks all moves of the players cell to see which ones are valid
    # and prints the valid moves to the console and waits for player input
    allMoves = ""
    possibleMoves = []
    for d in currentCell["dir"]:
        # validMove() returns true if a move is valid
        if validMove(playerPos, dirDict[d], steps, width, height):
            allMoves += moves[d]
            possibleMoves.append(moves[d][6])
    # If there are no valid moves left then the game ends
    if len(possibleMoves) == 0:
        print("You cannot move anymore!\nGame Over")
        break
    move = input("Possible Moves: " + allMoves + "\nEnter next move: ").upper()
    # Checks if player inputs a valid move
    if move not in possibleMoves:
        print("Not a valid move!\nTry again")
    else:
        # Sets player to new cell based on direction chosen and stride length
        # Loop restarts at new player location
        newDir = moveToDir[move]
        playerPos = [
            playerPos[0] + (dirDict[newDir][0] * steps),
            playerPos[1] + (dirDict[newDir][1] * steps),
        ]
# If the player reaches the end square after the loop is over
# then the game statistics will be printed
if playerPos == end:
    printBoard(board, width, height, start, end, playerPos)
    print("You Win!\nGame statistics")
    print(f"Total moves: {len(cellHistory)}")
    print("Playthrough history:")
    for c in cellHistory:
        print(f"({c[0]}, {c[1]})")
