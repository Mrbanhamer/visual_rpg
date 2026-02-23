import pygame
from entities_template import Entity

class Player(Entity):
    def __init__(self, hp, speed, armor, dmg_modifier):
        super().__init__(hp, speed, armor)
        self.dmg_modifier = dmg_modifier
        self.rect = pygame.Rect(100, 100, 32, 48)
        self.moving = False

    def handle_input(self, dt):
        keys = pygame.key.get_pressed()
        self.moving = False

        if keys[pygame.K_w]:
            self.rect.y -= self.speed * dt
            self.moving = True

        if keys[pygame.K_s]:
            self.rect.y += self.speed * dt
            self.moving = True

        if keys[pygame.K_a]:
            self.rect.x -= self.speed * dt
            self.moving = True

        if keys[pygame.K_d]:
            self.rect.x += self.speed * dt
            self.moving = True

