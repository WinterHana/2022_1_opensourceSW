import pygame

pygame.init()

background = pygame.display.set_mode((480, 460))
pygame.display.set_caption("SONOL")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Play = False

pygame.quit()
