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

    # update player health bar
    game.player.update_health_bar(screen)


    # draw player bullets group on screen
    for bullet in game.player.bullets:
        bullet.move()
    game.player.bullets.draw(screen)

    # draw monster on screen
    for monster in game.monsters:
        monster.forward()
        monster.update_health_bar(screen)
    game.monsters.draw(screen)

    # move the player (with collision detection)
    if game.keys_pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.keys_pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
