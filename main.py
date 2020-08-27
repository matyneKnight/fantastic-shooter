import pygame
pygame.init()

# init game screen
pygame.display.set_caption("Comet fall Game")
pygame.display.set_mode((1080, 720))

running = True

# boucle on game
while running:
    # if user stop the game
    for event in pygame.event.get():
        # for screen close event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closing the game...")
