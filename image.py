import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

from .consts import debug

class Texture:
    def __init__(self,tex_id,size):
        self.data = tex_id
        self.width = size[0]
        self.height = size[1]

# dict containing all textures loaded
textures: dict[str,Texture] = {}

def load_texture(id:str, path: str, scale=1):
    img = pygame.image.load(path).convert_alpha()
    img_data = pygame.image.tostring(img, "RGBA", True)
    width, height = img.get_size()

    # generating texture id for opengl
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # upload texture to gpu
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    # texture settings
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    textures[id] = Texture(texture_id, (width * scale, height * scale)) # returns texture data, width and height (adjusted to scale)

    if debug:
        print(f"Texture: '{id}' Loaded Successfully!")

# draw image as texture
def draw_texture(tex_data,x,z,w,h,scroll,alpha):
    glBindTexture(GL_TEXTURE_2D,tex_data)
    glColor4f(1, 1, 1, alpha)

    # quad vertexes
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x     -scroll[0], z    -scroll[1])   # bottom-left
    glTexCoord2f(1, 0); glVertex2f(x + w -scroll[0], z    -scroll[1])   # bottom-right
    glTexCoord2f(1, 1); glVertex2f(x + w -scroll[0], z + h-scroll[1])   # top-right
    glTexCoord2f(0, 1); glVertex2f(x     -scroll[0], z + h-scroll[1])   # top-left
    glEnd()
