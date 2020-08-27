import pygame
pygame.init()

class Game:
    def __init__(self):
        self.player = Player()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

# init game screen
pygame.display.set_caption("Comet fall Game")
screen =  pygame.display.set_mode((1080, 720))

# load new game
game = Game()
# load game background image
background = pygame.image.load('assets/bg.jpg')

running = True

# boucle on game
while running:
    # apply game background
    screen.blit(background, (0,-200))

    # load game player
    screen.blit(game.player.image,game.player.rect)


    # update game screen
    pygame.display.flip()

    # if user stop the game
    for event in pygame.event.get():
        # for screen close event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closing the game...")
