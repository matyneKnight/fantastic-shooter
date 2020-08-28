import pygame
import math
from parts.game import Game

pygame.init()


# init game screen
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# load new game
game = Game()
# load game background, starting banner, play button images
background = pygame.image.load('assets/bg.jpg')

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

running = True

# loop on game (running...)
while running:
    # apply game background
    screen.blit(background, (0, -200))

    # playing status
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # update game screen
        pygame.display.flip()

        # Detect all events when game run
        for event in pygame.event.get():
            # detect screen close event
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Closing the game...")

            # detect keyboard key press/release event
            elif event.type == pygame.KEYDOWN:
                game.keys_pressed[event.key] = True

                # detect shoot key press (space)
                if event.key == pygame.K_SPACE:
                    game.player.launch_bullet()

            elif event.type == pygame.KEYUP:
                game.keys_pressed[event.key] = False
