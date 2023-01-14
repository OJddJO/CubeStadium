from PIL import Image, ImageDraw

class Cube():
    #cube 3x3x3 model
    def __init__(self, scramble:str):
        self.cube = [[[0 for i in range(3)] for j in range(3)] for k in range(6)]
        #white = 0, yellow = 1, red = 2, orange = 3, green = 4, blue = 5
        self.cube[0] = [[0 for i in range(3)] for j in range(3)] #white UP
        self.cube[1] = [[4 for i in range(3)] for j in range(3)] #green FRONT
        self.cube[2] = [[1 for i in range(3)] for j in range(3)] #yellow DOWN
        self.cube[3] = [[3 for i in range(3)] for j in range(3)] #orange LEFT
        self.cube[4] = [[2 for i in range(3)] for j in range(3)] #red RIGHT
        self.cube[5] = [[5 for i in range(3)] for j in range(3)] #blue BACK
        self.moves = {
            "U": self.rotateU,
            "U'": self.rotateUp,
            "D": self.rotateD,
            "D'": self.rotateDp,
            "L": self.rotateL,
            "L'": self.rotateLp,
            "R": self.rotateR,
            "R'": self.rotateRp,
            "F": self.rotateF,
            "F'": self.rotateFp,
            "B": self.rotateB,
            "B'": self.rotateBp,
            "U2": self.rotateU2,
            "D2": self.rotateD2,
            "L2": self.rotateL2,
            "R2": self.rotateR2,
            "F2": self.rotateF2,
            "B2": self.rotateB2
        }
        self.scramble = scramble
        self.matrix = self.getMatrix()


    def drawCube(self):
        #draw cube pattern
        cubeImage = Image.new('RGBA', (1200, 900), (0, 0, 0, 255))
        draw = ImageDraw.Draw(cubeImage)
        
        #get colors from cube model
        colors = {
            0: (255, 255, 255),
            1: (255, 255, 0),
            2: (255, 0, 0),
            3: (255, 165, 0),
            4: (0, 255, 0),
            5: (0, 0, 255)
        }
        #draw cube pattern on image
        #draw UP face
        pos = [300, 0]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*100, pos[1]+i*100, pos[0]+(j+1)*100, pos[1]+(i+1)*100], fill=colors[self.matrix[0][i][j]])
        #draw FRONT face
        pos = [300, 300]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*100, pos[1]+i*100, pos[0]+(j+1)*100, pos[1]+(i+1)*100], fill=colors[self.matrix[1][i][j]])
        #draw DOWN face
        pos = [300, 600]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*100, pos[1]+i*100, pos[0]+(j+1)*100, pos[1]+(i+1)*100], fill=colors[self.matrix[2][i][j]])
        #draw LEFT face
        pos = [0, 300]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*100, pos[1]+i*100, pos[0]+(j+1)*100, pos[1]+(i+1)*100], fill=colors[self.matrix[3][i][j]])
        #draw RIGHT face
        pos = [600, 300]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*100, pos[1]+i*100, pos[0]+(j+1)*100, pos[1]+(i+1)*100], fill=colors[self.matrix[4][i][j]])
        #draw BACK face
        pos = [900, 300]
        for i in range(3):
            for j in range(3):
                draw.rectangle([pos[0]+j*100, pos[1]+i*100, pos[0]+(j+1)*100, pos[1]+(i+1)*100], fill=colors[self.matrix[5][i][j]])
        return cubeImage

    def getMatrix(self):
        for move in self.scramble.split(" "):
            self.moves[move]()
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
