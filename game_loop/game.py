import pygame
import asyncio
from entities.player import Player
from settings.world_settings import WORLD_HEIGHT, WORLD_WIDTH, frame_width, frame_height, screen_size, screen_fill
from settings.player_settings import player_x, player_y, player_controlls, Camera
from rendering.render import player_idle, player_move, get_brick_sprite, get_player_sprite, Animation

def start_game():
    global player_x, player_y, frame_height, frame_width
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # Initialize your screen ONCE
    screen = screen_size()  

    background = get_brick_sprite()

    bg_width = background.get_width()
    bg_height = background.get_height()

    sprite_sheet = get_player_sprite()

    idle_frame = player_idle(sprite_sheet)
    run_frames = player_move(sprite_sheet)

    idle_animation = Animation([idle_frame], 0)  # speed 0 since 1 frame
    run_animation = Animation(run_frames, 0.2)

    moving = False

    player = Player(5, 5, 5, 5)

    camera = Camera(player)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen_fill(screen)

        # Camera updates every frame
        camera.update(screen)

        # Draw large world with camera offset
        for x in range(0, WORLD_WIDTH, bg_width):
            for y in range(0, WORLD_HEIGHT, bg_height):
                screen.blit(background, (x - camera_x, y - camera_y))

        player.handle_input(dt)

        if moving == True:
            current_animation = run_animation
        else:
            current_animation = idle_animation

        current_animation.update()
        current_animation.draw(screen, (screen.get_width()//2, screen.get_height()//2))
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    start_game()