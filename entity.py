import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from .image import load_texture

# global entities
entities = []

# entity
class Entity:
    def __init__(self, name="entity", img_path="tsuki/no.png",scale=0.5,pos=None,group=entities) -> None:
        # default values
        self.name = name
        self.img, self.width, self.height = load_texture(img_path,scale=scale)
        if pos == None:
            pos = [0,0]
        self.pos = pos

        # conditional values
        self.hidden = False

        group.append(self)

# rendering group of entities
def draw_group(group=entities,camera=None) -> None:
    scroll = [0,0]
    if camera:
        scroll = camera.scroll
    if group:
        for entity in group:
            if not entity.hidden:
                glBindTexture(GL_TEXTURE_2D,entity.img)

                glBegin(GL_QUADS)
                glTexCoord2f(0, 0); glVertex2f(entity.pos[0]               -scroll[0], entity.pos[1]                -scroll[1])   # bottom-left
                glTexCoord2f(1, 0); glVertex2f(entity.pos[0] + entity.width-scroll[0], entity.pos[1]                -scroll[1])   # bottom-right
                glTexCoord2f(1, 1); glVertex2f(entity.pos[0] + entity.width-scroll[0], entity.pos[1] + entity.height-scroll[1])   # top-right
                glTexCoord2f(0, 1); glVertex2f(entity.pos[0]               -scroll[0], entity.pos[1] + entity.height-scroll[1])   # top-left
                glEnd()
