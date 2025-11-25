# global imports
import pygame, sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# local imports
from .consts import *
from .entity import *

class Tsuki():
    def __init__(self,init,update,events):

        # initialize engine stuff
        pygame.init()

        # window init
        self.win = pygame.display.set_mode(win_size,pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption(win_title)
        self.cl = pygame.time.Clock()

        # image init
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND) # transparency enabled
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # local src init
        init()

        # rendering init
        
        # Setup projection (simple 2D)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, 800, 0, 600)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # main loop
        while True:
            # clearing window
            glClear(GL_COLOR_BUFFER_BIT)

            # events
            for event in pygame.event.get():
                # events
                events(event)

                if event.type == pygame.QUIT:
                    sys.exit()
            
            # update method
            update()

            # draw
            draw_entities()

            pygame.display.flip()
            self.cl.tick(frame_rate)