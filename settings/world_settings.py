import pygame
from screeninfo import get_monitors

#decides how tall and wide the world is
WORLD_WIDTH = 4000
WORLD_HEIGHT = 3000

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
#def screen_fill():
#    screen.fill("black")