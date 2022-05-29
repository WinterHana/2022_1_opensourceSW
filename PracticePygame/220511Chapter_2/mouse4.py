# 마우스로 조종하기
from re import X
import pygame

pygame.init()

background = pygame.display.set_mode((480, 360)) 
pygame.display.set_caption("SONOL") 

x_pos = 0
y_pos = 0

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
        if event.type == pygame.MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()
            pygame.draw.circle(background, (255, 0, 255), (x_pos, y_pos), 10)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                background.fill((0, 0, 0))
        
    pygame.display.update()

pygame.quit