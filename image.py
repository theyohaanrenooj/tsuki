import pygame, os
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

from .consts import debug, render_scale

class Texture:
    def __init__(self,tex_id,size):
        self.data = tex_id
        self.width = size[0]
        self.height = size[1]

def load_texture(path: str, scale=1):
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

    return Texture(texture_id, (width * scale, height * scale)) # returns texture data, width and height (adjusted to scale)

    if debug:
        print(f"Texture: Loaded Successfully!")

def load_texture_frames(path:str,scale=1):
    frames = []
    if os.path.exists(path):
        imgs = os.listdir(path)
        if imgs:
            for img_name in imgs:
                frames.append(load_texture(os.path.join(path,img_name),scale=scale))

    return frames

# draw image as texture
def draw_texture(texture,x,z,w,h,scroll,alpha):
    glBindTexture(GL_TEXTURE_2D,texture.data)
    glColor4f(1, 1, 1, alpha)

    # quad vertexes
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x                  -scroll[0], z                  -scroll[1])   # bottom-left
    glTexCoord2f(1, 0); glVertex2f(x + w*render_scale -scroll[0], z                  -scroll[1])   # bottom-right
    glTexCoord2f(1, 1); glVertex2f(x + w*render_scale -scroll[0], z + h*render_scale -scroll[1])   # top-right
    glTexCoord2f(0, 1); glVertex2f(x                  -scroll[0], z + h*render_scale -scroll[1])   # top-left
    glEnd()
