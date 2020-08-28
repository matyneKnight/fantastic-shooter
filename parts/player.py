import pygame
from parts.bullet import Bullet

#define the player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = 100
        self.attack = 10
        self.bullets = pygame.sprite.Group()
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_bullet(self):
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity