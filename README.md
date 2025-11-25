# TSUKI

a non gui, game engine based on top of opengl for rendering and [pygame](https://www.pygame.org/news) for event and window handling.

## Features

- Entity Management
- texture loader (with id)
- camera system
- entity group renderer

## Basic Example

```python
import tsuki, pygame

class Game:
    def __init__(self):
        self.preload() # for loading images

        self.player = tsuki.Entity(name="player",texture_id="test")
        self.test = tsuki.Entity(name="testbox",texture_id="test")

        self.player_speed = 4

    def preload(self):
        tsuki.load_texture("test","Untitled.png") # load a texture with id test

    def update(self):
        tsuki.camera.follow(self.player)

        keys = pygame.key.get_pressed()
        if keys[tsuki.K_d]:
            self.player.pos[0] += self.player_speed
        elif keys[tsuki.K_a]:
            self.player.pos[0] -= self.player_speed

        if keys[tsuki.K_w]:
            self.player.pos[1] += self.player_speed
        elif keys[tsuki.K_s]:
            self.player.pos[1] -= self.player_speed

    def events(self, event):
        pass

```
