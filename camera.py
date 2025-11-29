from .consts import win_size, debug
from .image import textures
import pygame

class Camera:
    def __init__(self) -> None:
        self.scroll = [0,0] # scroll acts like an offset
        self.smoothing = 0.2
        self.plane = pygame.Rect(0,0,win_size[0]+20,win_size[1]+20)

    def follow(self, entity) -> None:
        # target
        target_x = entity.pos[0] + textures[entity.img_id].width  / 2 - win_size[0] / 2
        target_y = entity.pos[1] + textures[entity.img_id].height / 2 - win_size[1] / 2

        # change scroll relative to target with smoothing
        self.scroll[0] += (target_x - self.scroll[0]) * self.smoothing
        self.scroll[1] += (target_y - self.scroll[1]) * self.smoothing

        # set pos of plane
        self.plane.x = target_x-10
        self.plane.y = target_y-10

    def set_pos(self,pos=(0,0)) -> None:
        target_x = pos[0] / 2 - win_size[0] / 2
        target_y = pos[1] / 2 - win_size[1] / 2

        self.scroll[0] += (target_x - self.scroll[0]) * self.smoothing
        self.scroll[1] += (target_y - self.scroll[1]) * self.smoothing
