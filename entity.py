import pygame, sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from .image import load_texture, textures
from .consts import debug
from .group import *

# entity
class Entity:
    def __init__(self, name="entity", texture_id="tsuki",pos=None,group="main") -> None:
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

        # render parameters
        self.bloom = False
        self.bloom_strength = 5

         # adds entity to main entity group for rendering
        try:
            groups[group].add_entity(self)
        except KeyError:
            print(f"Group {group}: doesnt exist")

        # debug
        if debug:
            print(f"Entity: '{self.name}' loaded successfully!")
