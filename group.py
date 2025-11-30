import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from .image import load_texture, draw_texture
from .consts import debug

groups = {}

class Group:
    def __init__(self,name="main", y=0):
        self.y = y
        self.entities = []
        self.disabled = False

        groups[name] = self

    def add_entity(self,entity):
        self.entities.append(entity)

    def draw(self,camera=None,perf=True) -> None:

        # if the group is disabled, dont have to go through the entity list, saving performance
        if not self.disabled:

            # z ordering
            self.entities.sort(key=lambda s: s.pos[1])
            self.entities.reverse()

            # camera setup for rendering
            scroll = [0,0] # defaults to no scroll isnt given, for gui and stuff
            if camera:
                scroll = camera.scroll

            # rendering group
            if self.entities:
                for entity in self.entities:
                    if not entity.hidden:
                        if camera and perf: # checking if camera is given if given then draw with performance
                            if camera.plane.colliderect(pygame.Rect(entity.pos[0],entity.pos[1],entity.width,entity.height)):

                                glEnable(GL_BLEND)
                                glBlendFunc(GL_SRC_ALPHA, GL_ONE)  # for bloom

                                # glow passes for effect
                                if entity.bloom:
                                    for i in range(1, 10 * entity.bloom_strength):
                                        scale = 1 + i * 0.125
                                        alpha = 0.25 / i  # weaker further out

                                        sw = entity.width * scale
                                        sh = entity.height * scale
                                        sx = entity.pos[0] - (sw - entity.width) / 2
                                        sz = entity.pos[1] - (sh - entity.height) / 2

                                        draw_texture(entity.img, sx, sz, sw, sh, scroll, alpha)

                                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # restore normal blending
                                draw_texture(entity.img,entity.pos[0],entity.pos[1],entity.width,entity.height,scroll,1.0)

                        else: # if camera not given , draw normal without checking for camera plane collision
                            glEnable(GL_BLEND)
                            glBlendFunc(GL_SRC_ALPHA, GL_ONE)  # for bloom

                            # glow passes for effect
                            if entity.bloom:
                                for i in range(1, 10 * entity.bloom_strength):
                                    scale = 1 + i * 0.125
                                    alpha = 0.25 / i  # weaker further out

                                    sw = entity.width * scale
                                    sh = entity.height * scale
                                    sx = entity.pos[0] - (sw - entity.width) / 2
                                    sz = entity.pos[1] - (sh - entity.height) / 2

                                    draw_texture(entity.img, sx, sz, sw, sh, scroll, alpha)

                            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # restore normal blending
                            draw_texture(entity.img,entity.pos[0],entity.pos[1],entity.width,entity.height,scroll,1.0)


# creating main group
Group(name="main")
