from .consts import win_size, debug
import pygame

class Camera:
    def __init__(self) -> None:
        self.scroll = [0,0] # scroll acts like an offset
        self.smoothing = 0.2
        self.plane = pygame.Rect(0,0,win_size[0]+100,win_size[1]+100)

    def follow(self, entity) -> None:
        # target
        target_x = entity.pos[0] + entity.width  / 2 - win_size[0] / 2
        target_y = entity.pos[1] + entity.height / 2 - win_size[1] / 2

        # change scroll relative to target with smoothing
        self.scroll[0] += (target_x - self.scroll[0]) * self.smoothing
        self.scroll[1] += (target_y - self.scroll[1]) * self.smoothing

        # set pos of plane
        self.plane.x = target_x-50
        self.plane.y = target_y-50

    def set_pos(self,pos=(0,0)) -> None:
        target_x = pos[0] / 2 - win_size[0] / 2
        target_y = pos[1] / 2 - win_size[1] / 2

        self.scroll[0] += (target_x - self.scroll[0]) * self.smoothing
        self.scroll[1] += (target_y - self.scroll[1]) * self.smoothing
