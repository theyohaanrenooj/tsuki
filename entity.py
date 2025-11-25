import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from .image import load_texture

# global entities
entities = []

# entity
class Entity:
    def __init__(self, name="entity", img_path="tsuki/no.png",pos=[0,0],group=entities) -> None:
        # default values
        self.name = name
        self.img, self.width, self.height = load_texture(img_path)
        self.pos = pos

        # conditional values
        self.hidden = False

        group.append(self)

# rendering group of entities
def draw_group(group=entities) -> None:
    if group:
        for entity in group:
            if not entity.hidden:
                glBindTexture(GL_TEXTURE_2D,entity.img)

                glBegin(GL_QUADS)
                glTexCoord2f(0, 0); glVertex2f(entity.pos[0]               , entity.pos[1]                )   # bottom-left
                glTexCoord2f(1, 0); glVertex2f(entity.pos[0] + entity.width, entity.pos[1]                )   # bottom-right
                glTexCoord2f(1, 1); glVertex2f(entity.pos[0] + entity.width, entity.pos[1] + entity.height)   # top-right
                glTexCoord2f(0, 1); glVertex2f(entity.pos[0]               , entity.pos[1] + entity.height)   # top-left
                glEnd()