import pygame
import sys

pygame.init()

# 1. 배경 설정
Stage1_bg = pygame.image.load("QuestUI/image/stage1.png")
Stage2_bg = pygame.image.load("QuestUI/image/stage2.png")
size_Stage1_width = Stage1_bg.get_size()[0]
size_Stage1_height = Stage1_bg.get_size()[1]

display_height = size_Stage1_height # 세로 길이
display_width = size_Stage1_width # 가로 길이

gameDisplay= pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Stage")

def quitgame():
    pygame.quit()
    sys.exit()
    
def main_screen():
    pass

def Stage1():
    play = True

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                
            if event.type == pygame.MOUSEBUTTONDOWN:  
                print(pygame.mouse.get_pos())
                Stage2()
            
        pygame.display.update()
            
        gameDisplay.blit(Stage1_bg, (0, 0))
        
def Stage2():
    play = True
 
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                
        pygame.display.update()
            
        gameDisplay.blit(Stage2_bg, (0, 0))    
        
Stage1()


