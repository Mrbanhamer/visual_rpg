import pygame

player_start_x = 0
player_start_y = 0
player_speed = 5

class Camera:
    def __init__(self, player):
        self.player = player
        self.offset_x = 0
        self.offset_y = 0
    
    def update(self, screen, speed=0.1):
        target_x = self.player.rect.centerx - screen.get_width() // 2
        target_y = self.player.rect.centery - screen.get_height() // 2
        self.offset_x += (target_x - self.offset_x) * speed
        self.offset_y += (target_y - self.offset_y) * speed

    def apply(self, rect):
        """Return a rect adjusted for camera offset"""
        return rect.move(-self.offset_x, -self.offset_y)

def player_controlls(moving, dt, player_y, player_x):
    keys = pygame.key.get_pressed()

    moving = False

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
    
    return moving, player_y, player_x