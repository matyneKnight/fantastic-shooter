import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 100
        self.health = 50
        self.attack = 5
        self.velocity = 2
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect();
        self.rect.x = 1000
        self.rect.y = 540

    def update_health_bar(self, surface):
        # define health  bar configs and draw it
        bar_color = (111, 210, 46)
        bar_background_color = (60, 63, 60)
        background_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        pygame.draw.rect(surface, bar_background_color, background_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # move if not collide with the player
        if not self.game.check_collision(self, self.game.players):
            self.rect.x -= self.velocity