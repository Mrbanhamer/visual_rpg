import pygame
from settings.world_settings import frame_height, frame_width

def player_render():
    player_sprite = pygame.image.load(
        '../Tech Dungeon Roguelite - Asset Pack (DEMO)/Players/No Outlines/players blue x3.png'
    ).convert_alpha()
    return player_sprite

def player_idle():
    player_sprite = player_render
    idle_frame = player_sprite.subsurface((0, 0, frame_width, frame_height))
    return idle_frame

def player_move():
    running_frames = []
    player_sprite = player_render
    for x in range(4):
        frame = player_sprite.subsurface((x * frame_width, 0, frame_width, frame_height))
        running_frames.append(frame)
    return running_frames

def background():
    background = pygame.image.load(
        '../128x128/brick/brick_20-128x128.png'
    ).convert()
    return background
