import numpy as np 
import pyglet

class GameOfLife:

    def __init__(self,pixel,resolution):
        self.pixel = pixel
        self.resolution = resolution
        self.side = int(pixel/resolution)
        
        #... Initialize ...#
        self.cell_state = np.genfromtxt('ini_config.csv',delimiter = ',')


    def conway(self):
        '''
        @ Prof. John Conway (1937-2020), Princeton University, USA @

        '''
        new = np.zeros((self.resolution,self.resolution)) 
        for i in range(self.resolution):
            for j in range(self.resolution):
                move = self.mic(i,j)

                #..................... Moore Neighbourhood .....................#
                front = self.cell_state[i][move[0]]
                back = self.cell_state[i][move[1]]
                up = self.cell_state[move[2]][j]
                down = self.cell_state[move[3]][j]
                front_up = self.cell_state[move[2]][move[0]]
                front_down = self.cell_state[move[3]][move[0]]
                back_up = self.cell_state[move[2]][move[1]]
                back_down = self.cell_state[move[3]][move[1]]
                #...............................................................#
                
                count = sum([front,back,up,down,front_up,front_down,back_up,back_down])
                if (self.cell_state[i][j] == 1) and ( (count == 2) or (count == 3) ):
                    new[i][j] = 1
                elif (self.cell_state[i][j] == 0) and (count == 3):
                    new[i][j] = 1

        self.cell_state = new


    def mic(self,row,col):
        '''
        Minimum Image Convention (MIC) : periodic boundary conditions in (x,y)
        
        '''
        if (col == 0):
            front = col + 1
            back = self.resolution - 1
        elif (col == self.resolution - 1):
            front = 0
            back = col - 1
        else:
            front = col + 1
            back = col - 1

        if (row == 0):
            up = self.resolution - 1
            down = row + 1
        elif (row == self.resolution - 1):
            up = row - 1
            down = 0
        else:
            up = row - 1
            down = row + 1

        return np.array([front,back,up,down]).astype('int32')


    def cell_draw(self):
        ''' 
        (x1,y2)_______(x2,y2)
              |       |
              | (i,j) |
              |_______|
        (x1,y1)       (x2,y1)
            
        '''
        for i in range(self.resolution):
            for j in range(self.resolution):
                if (self.cell_state[i][j] == 1):
                    x_1 = j*self.side
                    x_2 = x_1 + self.side
                    y_1 = self.pixel - (i + 1)*self.side
                    y_2 = y_1 + self.side

                    #... tuple ...#
                    coord = (x_1,y_1,x_2,y_1,x_1,y_2,x_2,y_2)
                    pyglet.graphics.draw_indexed(4,pyglet.gl.GL_TRIANGLES,[0,1,2,1,2,3],('v2i',coord))





        