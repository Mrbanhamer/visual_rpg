import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0

player_sprite = pygame.image.load(
    'Tech Dungeon Roguelite - Asset Pack (DEMO)/Players/No Outlines/players blue x3.png'
).convert_alpha()

background = pygame.image.load(
    '128x128/brick/brick_20-128x128.png'
).convert()

player_x = 1000
player_y = 800

bg_width = background.get_width()
bg_height = background.get_height()

WORLD_WIDTH = 4000
WORLD_HEIGHT = 3000

frame_width = 68
frame_height = 130

idle_frame = player_sprite.subsurface((0, 0, frame_width, frame_height))
running_frames = []
for i in range(4):
    frame = player_sprite.subsurface((i * frame_width, 0, frame_width, frame_height))
    running_frames.append(frame)
h = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_y -= 300 * dt
    if keys[pygame.K_s]:
        player_y += 300 * dt
    if keys[pygame.K_a]:
        player_x -= 300 * dt
    if keys[pygame.K_d]:
        player_x += 300 * dt

    # Camera updates every frame
    camera_x = player_x - screen.get_width() // 2
    camera_y = player_y - screen.get_height() // 2

    screen.fill("black")

    # Draw large world with camera offset
    for x in range(0, WORLD_WIDTH, bg_width):
        for y in range(0, WORLD_HEIGHT, bg_height):
            screen.blit(background, (x - camera_x, y - camera_y))

    # Draw player in center of screen
    screen.blit(running_frames[h], (screen.get_width()//2, screen.get_height()//2))
    if h == 3:
        h = 0
    h =+ 1



    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
