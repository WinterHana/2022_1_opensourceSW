# 스테이지가 바뀌는지 확인
import pygame
import sys
from QuizUI import *

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


hp = 0

def quitgame():
    pygame.quit()
    sys.exit()
    
def main_screen():
    pass

def Stage1():
    global hp
    play = True
    myWindow = Quiz_Window(gameDisplay, display_width, display_height, GRAMMARQUIZ_SIZE, Grammar_QuizList)

    while play:
        gameDisplay.blit(Stage1_bg, (0, 0))
        if hp == 0:
            # 퀴즈 창 실행
            myWindow.makeQuizWindow()
            myWindow.QuizManager()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:   
                # 오른쪽 키 누르면 퀴즈창 사라짐
                if event.key == pygame.K_RIGHT:
                    del myWindow
                    hp = hp + 1
                    
                # 스페이즈바 누르면 다음 스테이지로
                if event.key == pygame.K_SPACE:
                    Stage2()
                
        pygame.display.update()
            
        
        
def Stage2():
    play = True

    while play:
        gameDisplay.blit(Stage2_bg, (0, 0))  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                
        pygame.display.update()
            
          
        
Stage1()


