import pygame
from parts.game import Game

pygame.init()


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
