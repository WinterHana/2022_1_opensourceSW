# 마우스로 조종하기
import pygame

pygame.init()

background = pygame.display.set_mode((480, 360)) 
pygame.display.set_caption("SONOL") 


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            pass
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print("MOUSEBUTTONDOWN")
            #print(pygame.mouse.get_pos())
            #print(event.button)
            
            if event.button == 1:
                print("왼쪽 클릭")
            elif event.button == 2:
                print("휠 클릭")
            elif event.button == 3:
                print("오른쪽 클릭")
            elif event.button == 4:
                print("휠 올리기")
            elif event.button == 5:
                print("휠 내리기")            
                
pygame.quit()
