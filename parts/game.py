import  pygame
from parts.player import Player
from parts.monster import Monster

# define the game class
class Game:
    def __init__(self):
        self.player = Player(self)
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        self.monsters = pygame.sprite.Group()
        self.keys_pressed = {}
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.monsters.add(monster)