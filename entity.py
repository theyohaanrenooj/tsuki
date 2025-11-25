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
        self.width = textures[texture_id].width
        self.height = textures[texture_id].height

        # conditional values
        self.hidden = False
        self.bloom = False

        group.append(self) # adds entity to main entity group for rendering
        if debug:
            print(f"Entity: '{self.name}' loaded successfully!")

def draw_texture(tex_data,x,y,w,h,scroll,alpha):
    glBindTexture(GL_TEXTURE_2D,tex_data)
    glColor4f(1, 1, 1, alpha)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x     -scroll[0], y    -scroll[1])   # bottom-left
    glTexCoord2f(1, 0); glVertex2f(x + w -scroll[0], y    -scroll[1])   # bottom-right
    glTexCoord2f(1, 1); glVertex2f(x + w -scroll[0], y + h-scroll[1])   # top-right
    glTexCoord2f(0, 1); glVertex2f(x     -scroll[0], y + h-scroll[1])   # top-left
    glEnd()

def draw_group(group=entities,camera=None,z_order=True) -> None:
    # z ordering
    if z_order:
        group.sort(key=lambda s: s.pos[1])
        group.reverse()

    scroll = [0,0] # defaults to no scroll isnt given, for gui and stuff
    if camera:
        scroll = camera.scroll
    if group:
        for entity in group:
            if not entity.hidden:
                tex = textures[entity.img_id]
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE)  # for bloom

                # glow passes
                if entity.bloom:
                    for i in range(1, 6):
                        scale = 1 + i * 0.25
                        alpha = 0.25 / i  # weaker further out

                        sw = entity.width * scale
                        sh = entity.height * scale
                        sx = entity.pos[0] - (sw - entity.width) / 2
                        sy = entity.pos[1] - (sh - entity.height) / 2

                        draw_texture(tex.data, sx, sy, sw, sh, scroll, alpha)

                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # restore normal blending
                draw_texture(tex.data,entity.pos[0],entity.pos[1],entity.width,entity.height,scroll,1.0)
