import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 100
        self.health = 100
        self.attack = 5
        self.velocity = 2
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect();
        self.rect.x = 1000
        self.rect.y = 540

    def forward(self):
        # move if not collide with the player
        if not self.game.check_collision(self, self.game.players):
            self.rect.x -= self.velocity