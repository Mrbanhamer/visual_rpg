import pygame
from entities.player import Player
from settings.world_settings import (
    world_height, world_width, screen_size, screen_fill, World
)
from settings.player_settings import player_start_x, player_start_y, Camera
from rendering.render import player_idle, player_move, get_brick_sprite, get_player_sprite, Animation


def start_game():
    pygame.init()
    clock = pygame.time.Clock()
    running = True

    # Initialize your screen ONCE
    screen = screen_size()  

    # Load assets
    background = get_brick_sprite()
    sprite_sheet = get_player_sprite()

    idle_frame = player_idle(sprite_sheet)
    run_frames = player_move(sprite_sheet)

    idle_animation = Animation([idle_frame], 0)        # idle: single frame
    run_animation = Animation(run_frames, 0.2)         # running: multiple frames

    # Create player once
    player = Player(5, 300, 5, 5)
    player.rect.x = player_start_x
    player.rect.y = player_start_y

    # Camera tracks player
    camera = Camera(player)

    # World instance
    world = World(screen, world_width, world_height, background)

    while running:
        dt = clock.tick(60) / 1000  # Delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen_fill(screen)

        # Update camera first
        camera.update(screen)

<<<<<<< HEAD
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
=======
        # Draw world
        world.draw_background(camera)
>>>>>>> player_settings

        # Move player and determine animation
        player.move(dt)
        current_animation = run_animation if player.moving else idle_animation
        current_animation.update()
<<<<<<< HEAD
        current_animation.draw(screen, (screen.get_width()//2, screen.get_height()//2))
>>>>>>> 5656f7222d2ff73727627d8a8910c8df75880d8e
            
        moving = False   
=======
>>>>>>> player_settings

        # Draw player at camera-adjusted position
        draw_pos = camera.apply(player.rect)
        current_animation.draw(screen, (draw_pos.x, draw_pos.y))

        # Flip display
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    start_game()