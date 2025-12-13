# TSUKI

a non gui, game engine based on top of opengl for rendering and [pygame](https://www.pygame.org/news) for event and window handling.

## Features

- Entity System
- texture loader (with id)
- camera system
- entity group renderer
- Animation Manager

## Basic Example

```python
# game.py

import tsuki, pygame

tulip_img = tsuki.load_texture("tulip.png")
grass_img = tsuki.load_texture("grass.png")

frames = tsuki.load_texture_frames("slime")

# entities
player = tsuki.Entity(
    name="player",
    pos=[100,100],
    img=frames[0]
)
player_speed = 250

anim_man = tsuki.AnimationManager(player)
anim_man.add_animation("main",frames)
anim_man.load_animation("main")

test = tsuki.Entity(
    name="testbox",
    img=tulip_img
)
test.bloom = True

# grass
tsuki.Group(name="ground",y=-1)
for z in range(100):
    for x in range(100):
        grass = tsuki.Entity(f"grass{x},{z}",pos=[x*64,z*64],img=grass_img,group="ground")

def update(dt):
    tsuki.camera.follow(player)

    # movement
    keys = pygame.key.get_pressed()
    if keys[tsuki.K_d]:
        player.pos[0] += (player_speed) *dt
    elif keys[tsuki.K_a]:
        player.pos[0] += (-player_speed) *dt

    if keys[tsuki.K_w]:
        player.pos[1] += (player_speed) *dt
    elif keys[tsuki.K_s]:
        player.pos[1] += (-player_speed) *dt

    anim_man.update()

def events(event):
    pass


```

```python
# main.py
from tsuki import Tsuki

game = Tsuki()

```

then just run main.py
