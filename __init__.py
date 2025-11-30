import os

# Set the environment variable to hide the support prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# global imports
import pygame, sys, importlib

import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# local imports
from .consts import *
from .image import *
from .entity import *
from .camera import *
from .group import *
from .animator import *

# core component
# initialize engine stuff
pygame.init()
camera = Camera()
if debug:
    print("camera loaded!")

class Tsuki():
    def __init__(self):
        # pygame init
        self.pygame_init()

        # gl functions init
        self.gl_init()

        # initial init
        self.game = importlib.import_module("game")
        self.update_func = getattr(self.game, "update", None)
        self.events_func = getattr(self.game, "events", None)
        if debug:
            print("initialized game!")

        # rendering init
        self.render_init()

        # main loop
        self.loop()

    def pygame_init(self):

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
        gluOrtho2D(0, win_size[0], 0, win_size[1])

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        if debug:
            print("initialized window projections!")

    def loop(self):
        while True:
            # delta time
            dt = self.cl.tick(frame_rate) / 1000

            # clearing window
            glClear(GL_COLOR_BUFFER_BIT)

            # events
            for event in pygame.event.get():
                # events
                if self.events_func:
                    self.events_func(event)

                if event.type == pygame.QUIT:
                    sys.exit()

            # update method
            if self.update_func:
                self.update_func(dt)

            # draw groups
            sorted_groups = sorted(groups.items(), key=lambda item: item[1].y)
            for name,group in sorted_groups:
                group.draw(camera=camera)

            pygame.display.flip()
