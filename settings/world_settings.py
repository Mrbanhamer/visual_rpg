import pygame

#decides how tall and wide the world is
WORLD_WIDTH = 4000
WORLD_HEIGHT = 3000

frame_width = 68
frame_height = 130

#decides the resolution of the game
screen = pygame.display.set_mode((1920, 1080))

#decides the color of the world outside the background
def screen_fill():
    screen.fill("black")