import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from .image import load_texture, textures
from .consts import debug

# global entities
entities = []

# entity
class Entity:
    def __init__(self, name="entity", texture_id="tsuki",pos=None,group=entities) -> None:
        # default values
        self.name = name # name

        if texture_id == "tsuki": # make sure tsuki img is loaded when the first entity is created with the tsuki img
            try:
                if textures["tsuki"]:
                    pass
            except KeyError:
                load_texture("tsuki","tsuki/no.png",scale=0.5)
        self.img_id = texture_id

        if pos == None:
            pos = [0,0]
        self.pos = pos # position

        # conditional values
        self.hidden = False

        group.append(self) # adds entity to main entity group for rendering
        if debug:
            print(f"Entity: '{self.name}' loaded successfully!")

# rendering group of entities
def draw_group(group=entities,camera=None) -> None:
    scroll = [0,0] # defaults to no scroll if camera isnt given, for gui and stuff
    if camera:
        scroll = camera.scroll
    if group:
        for entity in group:
            if not entity.hidden:
                tex = textures[entity.img_id] # making reference
                glBindTexture(GL_TEXTURE_2D,tex.data)

                glBegin(GL_QUADS)
                glTexCoord2f(0, 0); glVertex2f(entity.pos[0]               -scroll[0], entity.pos[1]                -scroll[1])   # bottom-left
                glTexCoord2f(1, 0); glVertex2f(entity.pos[0]   +  tex.width-scroll[0], entity.pos[1]                -scroll[1])   # bottom-right
                glTexCoord2f(1, 1); glVertex2f(entity.pos[0]   +  tex.width-scroll[0], entity.pos[1]   +  tex.height-scroll[1])   # top-right
                glTexCoord2f(0, 1); glVertex2f(entity.pos[0]               -scroll[0], entity.pos[1]   +  tex.height-scroll[1])   # top-left
                glEnd()
