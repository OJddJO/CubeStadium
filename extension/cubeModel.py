class Cube():
    #cube 3x3x3 model
    def __init__(self, scramble):
        self.cube = [[[0 for i in range(3)] for j in range(3)] for k in range(6)]
        #white = 0, yellow = 1, red = 2, orange = 3, green = 4, blue = 5
        self.cube[0] = [[0 for i in range(3)] for j in range(3)] #white UP
        self.cube[1] = [[4 for i in range(3)] for j in range(3)] #green FRONT
        self.cube[2] = [[1 for i in range(3)] for j in range(3)] #yellow DOWN
        self.cube[3] = [[3 for i in range(3)] for j in range(3)] #orange LEFT
        self.cube[3] = [[1,2,3],[4,5,6],[7,8,9]]
        self.cube[4] = [[2 for i in range(3)] for j in range(3)] #red RIGHT
        self.cube[5] = [[5 for i in range(3)] for j in range(3)] #blue BACK
        self.scramble = scramble
    
    #self.cube[face][row][column]
    def rotateL(self):
        for i in range(3):
            self.cube[0][i][0], self.cube[1][i][0], self.cube[2][i][0], self.cube[5][i][2] = self.cube[5][i][2], self.cube[0][i][0], self.cube[1][i][0], self.cube[2][i][0]
        #rotation of LEFT face 3 times clockwise
        for i in range(2):
            self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0], self.cube[3][1][0] = self.cube[3][1][0], self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0]

    def rotateLp(self):
        for i in range(3):
            self.cube[0][i][0], self.cube[1][i][0], self.cube[2][i][0], self.cube[5][i][2] = self.cube[1][i][0], self.cube[2][i][0], self.cube[5][i][2], self.cube[0][i][0]
        #rotation of LEFT face 3 times counter-clockwise
        for i in range(2):
            self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0], self.cube[3][1][0] = self.cube[3][0][1], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0], self.cube[3][1][0], self.cube[3][0][0]

    def rotateR(self):
        pass

    def rotateU(self):
        pass

    def rotateD(self):
        pass

    def rotateF(self):
        pass

    def rotateB(self):
        pass

cube = Cube("R U R' U'")
print(cube.cube)
cube.rotateL()
print(cube.cube)