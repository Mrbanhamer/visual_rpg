import pygame
import asyncio
from settings.world_settings import WORLD_HEIGHT, WORLD_WIDTH, frame_width, frame_height, screen_size, screen_fill
from settings.player_settings import player_x, player_y
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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen_fill(screen)

        # Camera updates every frame
        camera_x = player_x - screen.get_width() // 2
        camera_y = player_y - screen.get_height() // 2

        # Draw large world with camera offset
        for x in range(0, WORLD_WIDTH, bg_width):
            for y in range(0, WORLD_HEIGHT, bg_height):
                screen.blit(background, (x - camera_x, y - camera_y))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player_y -= 300 * dt
            moving = True
        if keys[pygame.K_s]:
            player_y += 300 * dt
            moving = True
        if keys[pygame.K_a]:
            player_x -= 300 * dt
            moving = True
        if keys[pygame.K_d]:
            player_x += 300 * dt
            moving = True

        if moving:
            current_animation = run_animation
        else:
<<<<<<< HEAD
            asyncio.run(idle_animation(screen, stop))
=======
            current_animation = idle_animation

        current_animation.update()
        current_animation.draw(screen, (screen.get_width()//2, screen.get_height()//2))
>>>>>>> 5656f7222d2ff73727627d8a8910c8df75880d8e
            
        moving = False   

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    start_game()