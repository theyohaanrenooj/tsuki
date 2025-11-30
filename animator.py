class Animation:
    def __init__(self,frames,delay):
        self.frames = frames
        self.delay = delay

class AnimationManager():
    def __init__(self,entity):
        #entity being managed
        self.entity = entity

        # parameters
        self.animations = {}
        self.current_animation = None
        self.current_frame = 0
        self.delay = 0

    def add_animation(self,name,frames,delay=10):
        # adds animation to index
        self.animations[name] = Animation(frames,delay)

    def load_animation(self,name):
        # loads in animation data and changes entity info
        self.current_animation = self.animations[name]
        self.current_frame = 0
        self.delay = self.current_animation.delay

    def update(self):
        # updates each frame and sets frame to entity img
        if self.current_animation:
            if self.current_frame < len(self.current_animation.frames):
                # delay between frames
                if self.delay < self.current_animation.delay:
                    self.delay += 1
                else:
                    self.entity.img = self.current_animation.frames[self.current_frame]
                    self.current_frame += 1
                    self.delay = 0
            else:
                self.current_frame = 0
        self.entity.update_dimensions()
