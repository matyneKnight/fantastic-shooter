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
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center= self.rect.center)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # detect if bullet over the screen and destroy it
        if self.rect.x > 1080:
            self.remove()

    def remove(self):
        self.player.bullets.remove(self)
