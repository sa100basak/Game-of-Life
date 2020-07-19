import pyglet
import time
import sys

from game_of_life import GameOfLife
from render import makeclip

#... number of pixels ...#
N = 528
#... resolution ...#
n = 132
#... number of generations ...#
n_gen = 300
#... frames per sec ...#
fps = 10.0


class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(N,N)
        self.gen = 0
        self.sim = GameOfLife(self.get_size()[0],n)
        pyglet.clock.schedule_interval(self.update,1.0/fps)

    def on_draw(self):
        self.clear()
        self.sim.cell_draw()
        pyglet.image.get_buffer_manager().get_color_buffer().save(str(self.gen) + '.png')

    def update(self,dt):
        if (self.gen < n_gen):
            self.sim.conway()
            self.gen += 1
        else:
            time.sleep(3)
            makeclip(fps,n_gen)
            sys.exit()

if __name__ == '__main__':
    blank = Window()
    pyglet.app.run()


