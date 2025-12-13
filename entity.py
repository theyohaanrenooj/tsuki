import pygame, sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from .image import load_texture
from .consts import debug
from .group import *

# def texture


# entity
class Entity:
    def __init__(self, name="tsuki", img=None, pos=(0,0), group="main") -> None:
        # default values
        self.name = name # name

        if img:
            self.img = img
        else:
            tsuki_img = load_texture(path="tsuki/no.png", scale=0.5)
            self.img = tsuki_img

        # variables
        self.pos: list[int] = list(pos)
        self.width: int = self.img.width
        self.height: int = self.img.height

        # conditional values
        self.hidden: bool = False

        # render parameters
        self.bloom: bool = False
        self.bloom_strength: float = 5

         # adds entity to main entity group for rendering
        try:
            groups[group].add_entity(self)
        except KeyError:
            print(f"Group {group}: doesnt exist")

        # debug
        if debug:
            print(f"Entity: '{self.name}' loaded successfully!")

    def get_pos(self) -> list[int]:
        return self.pos

    def hide(self) -> None:
        self.hidden = True

    def show(self) -> None:
        self.hiddne = False

    def update_dimensions(self) -> None:
        self.width = self.img.width
        self.height = self.img.height
