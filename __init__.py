import os

# Set the environment variable to hide the support prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# global imports
import pygame, sys
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# local imports
from .consts import *
from .image import *
from .entity import *
from .camera import *

# core component
camera = Camera()
if debug:
    print("camera loaded!")

class Tsuki():
    def __init__(self,Game):
        # pygame init
        self.pygame_init()

        # gl functions init
        self.gl_init()

        # initial init
        self.game = Game()
        if debug:
            print("initialized game!")

        # rendering init
        self.render_init()

        # main loop
        self.loop()

    def pygame_init(self):
        # initialize engine stuff
        pygame.init()

        # window init
        self.win = pygame.display.set_mode(win_size,pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption(win_title)
        self.cl = pygame.time.Clock()
        if debug:
            print("Initialized Pygame!")

    def gl_init(self):
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND) # transparency enabled
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        if debug:
            print("Initialized gl settings!")

    def render_init(self):
        # Setup projection (simple 2D)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, 800, 0, 600)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        if debug:
            print("initialized window projections!")

    def loop(self):
        while True:
            # clearing window
            glClear(GL_COLOR_BUFFER_BIT)

            # events
            for event in pygame.event.get():
                # events
                self.game.events(event)

                if event.type == pygame.QUIT:
                    sys.exit()

            # update method
            self.game.update()

            # draw
            draw_group(camera=camera)

            pygame.display.flip()
            self.cl.tick(frame_rate)
