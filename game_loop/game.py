import pygame
from settings.world_settings import WORLD_HEIGHT, WORLD_WIDTH, frame_width, frame_height, screen_size
from settings.player_settings import player_x, player_y
from rendering.render import player_idle, player_move, background_brick, load_player_sprites

def start_game():
    global player_x, player_y, frame_height, frame_width
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # Initialize your screen ONCE
    screen = screen_size()  
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    player_sprite = load_player_sprites()
    background = background_brick()
    stop = player_idle()

    bg_width = background.get_width()
    bg_height = background.get_height()

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

        # Draw large world with camera offset
        for x in range(0, WORLD_WIDTH, bg_width):
            for y in range(0, WORLD_HEIGHT, bg_height):
                screen.blit(background, (x - camera_x, y - camera_y))

        # Draw player in center of screen
        screen.blit(stop, (screen.get_width()//2, screen.get_height()//2))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    start_game()