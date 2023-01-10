import random

moves = ("U", "U'", "U2", "D", "D'", "D2", "L", "L'", "L2", "R", "R'", "R2", "F", "F'", "F2", "B", "B'", "B2")

def getScramble(times=15):
    scramble = ""
    lastMoves = []
    while len(scramble.split(sep=" ")) <= times:
        move = random.choice(moves)
        if not move[0] in lastMoves:
            scramble += move + " "
            lastMoves[1] = lastMoves[0]
            lastMoves[0] = move[0]
    return scramble