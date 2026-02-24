import pygame
from screeninfo import get_monitors

#decides how tall and wide the world is
world_width = 4000
world_height = 3000

frame_width = 68
frame_height = 130

#automatically sets the screen size to the monitors resulotion
def screen_size():
    # Get the primary monitor (first one usually)
    monitor = get_monitors()[0]  
    width, height = monitor.width, monitor.height
    
    # Initialize pygame screen with these dimensions
    screen = pygame.display.set_mode((width, height))
    return screen

#decides the color of the world outside the background
def screen_fill(screen):
    screen.fill("black")

class World:
    def __init__(self, screen, world_width, world_height, background):
        self.screen = screen
        self.world_width = world_width
        self.world_height = world_height
        self.background = background

        self.bg_width = background.get_width()
        self.bg_height = background.get_height()

    def draw_background(self, camera):
        for x in range(0, self.world_width, self.bg_width):
            for y in range(0, self.world_height, self.bg_height):
                self.screen.blit(
                    self.background,
                    (x - camera.offset_x, y - camera.offset_y)
                )

    def set_void(self, color):
        self.screen.fill(color)