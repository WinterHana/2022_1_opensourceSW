# 마우스로 조종하기
from re import X
import pygame

pygame.init()

background = pygame.display.set_mode((480, 360)) 
pygame.display.set_caption("SONOL") 

x_pos = background.get_size()[0] // 2 #240
y_pos = background.get_size()[1] // 2 #180

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()
            
    background.fill((0, 0, 0))
    pygame.draw.circle(background, (255, 0, 255), (x_pos, y_pos), 10)     
    pygame.display.update()

pygame.quit()