import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 95

    def move(self):
        self.rect.x += self.velocity
        # detect if bullet over the screen and destroy it
        if self.rect.x > 1080:
            self.remove()

    def remove(self):
        self.player.bullets.remove(self)
