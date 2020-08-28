import pygame
from parts.player import Player
from parts.monster import Monster


# define the game class
class Game:
    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        self.monsters = pygame.sprite.Group()
        self.keys_pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # restart the game
        self.monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # load game player
        screen.blit(self.player.image, self.player.rect)

        # update player health bar
        self.player.update_health_bar(screen)

        # draw player bullets group on screen
        for bullet in self.player.bullets:
            bullet.move()
        self.player.bullets.draw(screen)

        # draw monster on screen
        for monster in self.monsters:
            monster.forward()
            monster.update_health_bar(screen)
        self.monsters.draw(screen)

        # move the player (with collision detection)
        if self.keys_pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.keys_pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    @staticmethod
    def check_collision(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.monsters.add(monster)
