import  pygame
from parts.player import Player
from parts.monster import Monster

# define the game class
class Game:
    def __init__(self):
        self.player = Player()
        self.monsters = pygame.sprite.Group()
        self.keys_pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.monsters.add(monster)