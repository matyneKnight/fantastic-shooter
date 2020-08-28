import pygame
from parts.bullet import Bullet

#define the player class
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
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

    def damage(self, amount):
        if self.health - amount > 0:
            self.health -= amount
        else: self.health = 0

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def move_right(self):
        # move if player not collide with a monster
        if not self.game.check_collision(self, self.game.monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity