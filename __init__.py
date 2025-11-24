# global imports
import pygame, sys

# local imports
from .consts import *

class MagnumOpus():
    def __init__(self,init,update,draw,events):

        # initialize everything
        init()

        # window init
        self.win = pygame.display.set_mode(win_size)
        pygame.display.set_caption(win_title)

        while True:
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