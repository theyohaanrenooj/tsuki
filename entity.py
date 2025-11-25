import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from .image import load_texture

# global entities
entities = []

class Entity:
    def __init__(self,name="entity",img_path="tsuki/no.png",pos=[0,0]):
        # default values
        self.name = name
        self.img = load_texture(img_path)
        self.pos = pos

        # conditional values
        self.hidden = False
    

        entities.append(self)


def draw_entities():
    if entities:
        for entity in entities:
            if not entity.hidden:
                glBindTexture(GL_TEXTURE_2D,entity.img)

                glBegin(GL_QUADS)
                glTexCoord2f(0, 0); glVertex2f(100, 100)   # bottom-left
                glTexCoord2f(1, 0); glVertex2f(300, 100)   # bottom-right
                glTexCoord2f(1, 1); glVertex2f(300, 300)   # top-right
                glTexCoord2f(0, 1); glVertex2f(100, 300)   # top-left
                glEnd()