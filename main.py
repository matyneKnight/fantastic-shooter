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

# loop on game (running...)
while running:
    # apply game background
    screen.blit(background, (0,-200))

    # load game player
    screen.blit(game.player.image,game.player.rect)

    # move the player (detect collision)
    if game.keys_pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.keys_pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # update game screen
    pygame.display.flip()

    # if user stop the game
    for event in pygame.event.get():
        # detect screen close event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closing the game...")

        # detect keyboard key press/release event
        elif event.type == pygame.KEYDOWN:
            game.keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.keys_pressed[event.key] = False
