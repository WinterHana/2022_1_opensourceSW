import pygame
from QuizUI import *

pygame.init()

clock = pygame.time.Clock()

def mainmenu():   
    mainmenu = True
    
    myWindow = Quiz_Window(gameDisplay, display_width, display_height, GRAMMARQUIZ_SIZE, Grammar_QuizList)
    
    while mainmenu:
        dt = clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        gameDisplay.fill(white)
        
        myWindow.makeQuizWindow()
        myWindow.QuizManager()
        
        pygame.display.update()
        
if __name__ == "__main__":   
    mainmenu()

