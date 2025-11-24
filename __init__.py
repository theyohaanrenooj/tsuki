# global imports
import pygame, sys

# local imports
from .consts import *

class Tsuki():
    def __init__(self,init,update,draw,events):

        # initialize everything
        init()

        # window init
        self.win = pygame.display.set_mode(win_size)
        pygame.display.set_caption(win_title)
        self.cl = pygame.time.Clock()

        # main loop
        while True:
            # clearing window
            self.win.fill((0,0,0))

            # events
            for event in pygame.event.get():
                # events
                events(event)

                if event.type == pygame.QUIT:
                    sys.exit()
                
                
            
            # update method
            update()
            # draw loop
            draw()

            pygame.display.update()
            self.cl.tick(frame_rate)