import random

moves = ("U", "U'", "U2", "D", "D'", "D2", "L", "L'", "L2", "R", "R'", "R2", "F", "F'", "F2", "B", "B'", "B2")

def getScramble(times=15):
    scramble = ""
    lastMove = ""
    for i in range(times):
        move = random.choice(moves)
        if move != lastMove:
            scramble += move + " "
            lastMove = move
        else:
            i -= 1
    return scramble