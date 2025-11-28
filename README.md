# TSUKI

a non gui, game engine based on top of opengl for rendering and [pygame](https://www.pygame.org/news) for event and window handling.

## Features

- Entity Management
- texture loader (with id)
- camera system
- entity group renderer

## Basic Example

```python
# game.py

import tsuki, pygame


def preload():

    # load texture with id
    tsuki.load_texture("tsuki","tsuki/no.png",scale=0.1)

preload() # for loading images

# init
player = tsuki.Entity(name="player",pos=[100,100],texture_id="tsuki")

player_speed = 5

def update():
    tsuki.camera.follow(player)

    keys = pygame.key.get_pressed()
    if keys[tsuki.K_d]:
        player.pos[0] += (player_speed)
    elif keys[tsuki.K_a]:
        player.pos[0] += (-player_speed)

    if keys[tsuki.K_w]:
        player.pos[1] += (player_speed)
    elif keys[tsuki.K_s]:
        player.pos[1] += (-player_speed)

def events(event):
    pass


```

```python
# main.py
from tsuki import Tsuki

game = Tsuki()

```
