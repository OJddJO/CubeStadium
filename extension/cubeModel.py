from PIL import Image, ImageDraw

class Cube():
    #cube 3x3x3 model
    def __init__(self):
        self.cube = [[[0 for i in range(3)] for j in range(3)] for k in range(6)]
        #white = 0, yellow = 1, red = 2, orange = 3, green = 4, blue = 5
        self.cube[0] = [[0 for i in range(3)] for j in range(3)] #white UP
        self.cube[1] = [[4 for i in range(3)] for j in range(3)] #green FRONT
        self.cube[2] = [[1 for i in range(3)] for j in range(3)] #yellow DOWN
        self.cube[3] = [[3 for i in range(3)] for j in range(3)] #orange LEFT
        self.cube[4] = [[2 for i in range(3)] for j in range(3)] #red RIGHT
        self.cube[5] = [[5 for i in range(3)] for j in range(3)] #blue BACK


    def drawCube(self, scramble):
        #draw cube pattern
        cubeImage = Image.new('RGBA', (380, 290), (50, 50, 50, 0))
        draw = ImageDraw.Draw(cubeImage, 'RGBA')
        
        #get colors from cube model
        colors = {
            0: (255, 255, 255),
            1: (255, 255, 0),
            2: (255, 0, 0),
            3: (255, 165, 0),
            4: (0, 255, 0),
            5: (0, 0, 255)
        }
        matrix = self.getMatrix(scramble)
        #draw cube pattern on image
        #draw UP face
        pos = [95, 0]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*30, pos[1]+i*30, pos[0]+(j+1)*30, pos[1]+(i+1)*30], fill=colors[matrix[0][i][j]])
        #draw FRONT face
        pos = [95, 95]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*30, pos[1]+i*30, pos[0]+(j+1)*30, pos[1]+(i+1)*30], fill=colors[matrix[1][i][j]])
        #draw DOWN face
        pos = [95, 190]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*30, pos[1]+i*30, pos[0]+(j+1)*30, pos[1]+(i+1)*30], fill=colors[matrix[2][i][j]])
        #draw LEFT face
        pos = [0, 95]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*30, pos[1]+i*30, pos[0]+(j+1)*30, pos[1]+(i+1)*30], fill=colors[matrix[3][i][j]])
        #draw RIGHT face
        pos = [190, 95]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*30, pos[1]+i*30, pos[0]+(j+1)*30, pos[1]+(i+1)*30], fill=colors[matrix[4][i][j]])
        #draw BACK face
        pos = [285, 95]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*30, pos[1]+i*30, pos[0]+(j+1)*30, pos[1]+(i+1)*30], fill=colors[matrix[5][i][j]])
        return cubeImage

    def getMatrix(self, scramble:str):
        for move in scramble.split(" "):
            if move == "U":
                self.rotateU()
            elif move == "U'":
                self.rotateUp()
            elif move == "U2":
                self.rotateU2()
            elif move == "D":
                self.rotateD()
            elif move == "D'":
                self.rotateDp()
            elif move == "D2":
                self.rotateD2()
            elif move == "F":
                self.rotateF()
            elif move == "F'":
                self.rotateFp()
            elif move == "F2":
                self.rotateF2()
            elif move == "B":
                self.rotateB()
            elif move == "B'":
                self.rotateBp()
            elif move == "B2":
                self.rotateB2()
            elif move == "L":
                self.rotateL()
            elif move == "L'":
                self.rotateLp()
            elif move == "L2":
                self.rotateL2()
            elif move == "R":
                self.rotateR()
            elif move == "R'":
                self.rotateRp()
            elif move == "R2":
                self.rotateR2()
        return self.cube
    
    #rotation functions
    #self.cube[face][row][column]
    def rotateL(self):
        for i in range(3):
            self.cube[0][i][0], self.cube[1][i][0], self.cube[2][i][0], self.cube[5][2-i][2] = self.cube[5][2-i][2], self.cube[0][i][0], self.cube[1][i][0], self.cube[2][i][0]
        #rotation of LEFT face 2 times clockwise
        for i in range(2):
            self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0], self.cube[3][1][0] = self.cube[3][1][0], self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0]

    def rotateLp(self):
        for i in range(3):
            self.cube[0][i][0], self.cube[1][i][0], self.cube[2][i][0], self.cube[5][2-i][2] = self.cube[1][i][0], self.cube[2][i][0], self.cube[5][2-i][2], self.cube[0][i][0]
        #rotation of LEFT face 2 times counter-clockwise
        for i in range(2):
            self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0], self.cube[3][1][0] = self.cube[3][0][1], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0], self.cube[3][1][0], self.cube[3][0][0]

    def rotateR(self):
        for i in range(3):
            self.cube[0][i][2], self.cube[1][i][2], self.cube[2][i][2], self.cube[5][2-i][0] = self.cube[1][i][2], self.cube[2][i][2], self.cube[5][2-i][0], self.cube[0][i][2]
        #rotation of RIGHT face 2 times clockwise
        for i in range(2):
            self.cube[4][0][0], self.cube[4][0][1], self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2], self.cube[4][2][1], self.cube[4][2][0], self.cube[4][1][0] = self.cube[4][1][0], self.cube[4][0][0], self.cube[4][0][1], self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2], self.cube[4][2][1], self.cube[4][2][0]

    def rotateRp(self):
        for i in range(3):
            self.cube[0][i][2], self.cube[1][i][2], self.cube[2][i][2], self.cube[5][2-i][0] = self.cube[5][2-i][0], self.cube[0][i][2], self.cube[1][i][2], self.cube[2][i][2]
        #rotation of RIGHT face 2 times counter-clockwise
        for i in range(2):
            self.cube[4][0][0], self.cube[4][0][1], self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2], self.cube[4][2][1], self.cube[4][2][0], self.cube[4][1][0] = self.cube[4][0][1], self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2], self.cube[4][2][1], self.cube[4][2][0], self.cube[4][1][0], self.cube[4][0][0]

    def rotateU(self):
        for i in range(3):
            self.cube[1][0][i], self.cube[3][0][i], self.cube[5][0][i], self.cube[4][0][i] = self.cube[4][0][i], self.cube[1][0][i], self.cube[3][0][i], self.cube[5][0][i]
        #rotation of UP face 2 times clockwise
        for i in range(2):
            self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2], self.cube[0][1][2], self.cube[0][2][2], self.cube[0][2][1], self.cube[0][2][0], self.cube[0][1][0] = self.cube[0][1][0], self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2], self.cube[0][1][2], self.cube[0][2][2], self.cube[0][2][1], self.cube[0][2][0]

    def rotateUp(self):
        for i in range(3):
            self.cube[1][0][i], self.cube[3][0][i], self.cube[5][0][i], self.cube[4][0][i] = self.cube[3][0][i], self.cube[5][0][i], self.cube[4][0][i], self.cube[1][0][i]
        #rotation of UP face 2 times counter-clockwise
        for i in range(2):
            self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2], self.cube[0][1][2], self.cube[0][2][2], self.cube[0][2][1], self.cube[0][2][0], self.cube[0][1][0] = self.cube[0][0][1], self.cube[0][0][2], self.cube[0][1][2], self.cube[0][2][2], self.cube[0][2][1], self.cube[0][2][0], self.cube[0][1][0], self.cube[0][0][0]

    def rotateD(self):
        for i in range(3):
            self.cube[1][2][i], self.cube[3][2][i], self.cube[5][2][i], self.cube[4][2][i] = self.cube[3][2][i], self.cube[5][2][i], self.cube[4][2][i], self.cube[1][2][i]
        #rotation of DOWN face 2 times clockwise
        for i in range(2):
            self.cube[2][0][0], self.cube[2][0][1], self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2], self.cube[2][2][1], self.cube[2][2][0], self.cube[2][1][0] = self.cube[2][1][0], self.cube[2][0][0], self.cube[2][0][1], self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2], self.cube[2][2][1], self.cube[2][2][0]

    def rotateDp(self):
        for i in range(3):
            self.cube[1][2][i], self.cube[3][2][i], self.cube[5][2][i], self.cube[4][2][i] = self.cube[4][2][i], self.cube[1][2][i], self.cube[3][2][i], self.cube[5][2][i]
        #rotation of DOWN face 2 times counter-clockwise
        for i in range(2):
            self.cube[2][0][0], self.cube[2][0][1], self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2], self.cube[2][2][1], self.cube[2][2][0], self.cube[2][1][0] = self.cube[2][0][1], self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2], self.cube[2][2][1], self.cube[2][2][0], self.cube[2][1][0], self.cube[2][0][0]

    def rotateF(self):
        for i in range(3):
            self.cube[0][2][i], self.cube[3][2-i][2], self.cube[2][0][2-i], self.cube[4][i][0] = self.cube[3][2-i][2], self.cube[2][0][2-i], self.cube[4][i][0], self.cube[0][2][i]
        #rotation of FRONT face 2 times clockwise
        for i in range(2):
            self.cube[1][0][0], self.cube[1][0][1], self.cube[1][0][2], self.cube[1][1][2], self.cube[1][2][2], self.cube[1][2][1], self.cube[1][2][0], self.cube[1][1][0] = self.cube[1][1][0], self.cube[1][0][0], self.cube[1][0][1], self.cube[1][0][2], self.cube[1][1][2], self.cube[1][2][2], self.cube[1][2][1], self.cube[1][2][0]
    
    def rotateFp(self):
        for i in range(3):
            self.cube[0][2][i], self.cube[3][2-i][2], self.cube[2][0][2-i], self.cube[4][i][0] = self.cube[4][i][0], self.cube[0][2][i], self.cube[3][2-i][2], self.cube[2][0][2-i]
        #rotation of FRONT face 2 times counter-clockwise
        for i in range(2):
            self.cube[1][0][0], self.cube[1][0][1], self.cube[1][0][2], self.cube[1][1][2], self.cube[1][2][2], self.cube[1][2][1], self.cube[1][2][0], self.cube[1][1][0] = self.cube[1][0][1], self.cube[1][0][2], self.cube[1][1][2], self.cube[1][2][2], self.cube[1][2][1], self.cube[1][2][0], self.cube[1][1][0], self.cube[1][0][0]

    def rotateB(self):
        for i in range(3):
            self.cube[0][0][i], self.cube[4][i][2], self.cube[2][2][2-i], self.cube[3][2-i][0] = self.cube[4][i][2], self.cube[2][2][2-i], self.cube[3][2-i][0], self.cube[0][0][i]
        #rotation of BACK face 2 times clockwise
        for i in range(2):
            self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0], self.cube[5][1][0] = self.cube[5][1][0], self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0]
    
    def rotateBp(self):
        for i in range(3):
            self.cube[0][0][i], self.cube[4][i][2], self.cube[2][2][2-i], self.cube[3][2-i][0] = self.cube[3][2-i][0], self.cube[0][0][i], self.cube[4][i][2], self.cube[2][2][2-i]
        #rotation of BACK face 2 times counter-clockwise
        for i in range(2):
            self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0], self.cube[5][1][0] = self.cube[5][0][1], self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0], self.cube[5][1][0], self.cube[5][0][0]

    def rotateL2(self):
        self.rotateL()
        self.rotateL()
    
    def rotateR2(self):
        self.rotateR()
        self.rotateR()
    
    def rotateU2(self):
        self.rotateU()
        self.rotateU()
    
    def rotateD2(self):
        self.rotateD()
        self.rotateD()
    
    def rotateF2(self):
        self.rotateF()
        self.rotateF()
    
    def rotateB2(self):
        self.rotateB()
        self.rotateB()
