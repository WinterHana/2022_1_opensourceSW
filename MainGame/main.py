from scripts import *
from QuizUI import *

# 1. 단순하게 퀴즈 맞추기
def Stage1(): 
    myWindow = Quiz_Window(DISPLAY, (DISPLAY_SIZE.x, DISPLAY_SIZE.y), 5, GRAMMARQUIZ_SIZE, 1, Grammar_QuizList)
    
    while True: 
    # checking for events
        for e in pygame.event.get():
            if (e.type is pygame.QUIT):
                pygame.quit()
                sys.exit()
                
        # clearing canvas
        CANVAS.fill((0, 0, 0, 0))  
        
        # drawing & updating player
        PLAYER.draw(CANVAS)
        PLAYER.update()
        
        pygame.draw.rect(CANVAS, "gray", pygame.Rect((CANVAS_SIZE.x*0//5, 0), (CANVAS_SIZE.x*2//5, CANVAS_SIZE.y//20)))
        pygame.draw.rect(
            CANVAS, "red",
            pygame.Rect((CANVAS_SIZE.x*0//5, 0),
            ((CANVAS_SIZE.x*2//5)*(PLAYER.sprite.hp/PLAYER.sprite.max_hp), CANVAS_SIZE.y//20)))
        
        # showing canvas on display
        DISPLAY.fill((135, 175, 75))
        DISPLAY.blit(pygame.transform.scale(CANVAS, tuple(DISPLAY_SIZE)), (0, 0))
        
        myWindow.makeQuizWindow()
        myWindow.QuizManager()
        if myWindow.getPlayQuiz() == False:
            del myWindow
            return
        
        if PLAYER.sprite.hp == 0:
            myWindow.gameover()
            
        # updating display
        pygame.display.flip()
        pygame.display.set_caption(f"[{DESCRIPTION}]-[FPS : {CLOCK.get_fps():.2f}]")
        CLOCK.tick(FPS)
        
def Stage2(): 
    myWindow = Quiz_Window(DISPLAY, (DISPLAY_SIZE.x, DISPLAY_SIZE.y), 10, HISTORYQUIZ_SIZE, 1.5, CommonSense_QuizList)
    
    # main loop
    while True: 
        # checking for events
        for e in pygame.event.get():
            if (e.type is pygame.QUIT):
                pygame.quit()
                sys.exit()
            
        # clearing canvas
        CANVAS.fill((0, 0, 0, 0))
            
        # drawing & updating enemies
        ENEMY.draw(CANVAS)
        ENEMY.update(PLAYER.sprite)

        # drawing & updating player
        PLAYER.draw(CANVAS)
        PLAYER.update()

        # detecting collisions
        if (PLAYER.sprite.is_attacking and int(PLAYER.sprite.anim_step) == 2):
            if (pygame.sprite.collide_mask(PLAYER.sprite, ENEMY.sprite) != None):
                ENEMY.sprite.take_damage(PLAYER.sprite.dmg)
        if (ENEMY.sprite.is_attacking and int(ENEMY.sprite.anim_step) == 3):
            if (pygame.sprite.collide_mask(PLAYER.sprite, ENEMY.sprite) != None):
                PLAYER.sprite.take_damage(ENEMY.sprite.dmg)

        # drawing health bars
        pygame.draw.rect(CANVAS, "gray", pygame.Rect((CANVAS_SIZE.x*0//5, 0), (CANVAS_SIZE.x*2//5, CANVAS_SIZE.y//20)))
        pygame.draw.rect(CANVAS, "gray", pygame.Rect((CANVAS_SIZE.x*3//5, 0), (CANVAS_SIZE.x*2//5, CANVAS_SIZE.y//20)))
        pygame.draw.rect(
            CANVAS, "red",
            pygame.Rect((CANVAS_SIZE.x*0//5, 0),
            ((CANVAS_SIZE.x*2//5)*(PLAYER.sprite.hp/PLAYER.sprite.max_hp), CANVAS_SIZE.y//20)))
        
        pygame.draw.rect(
            CANVAS, "red",
            pygame.Rect((CANVAS_SIZE.x*3//5, 0),
            ((CANVAS_SIZE.x*2//5)*(ENEMY.sprite.hp/ENEMY.sprite.max_hp), CANVAS_SIZE.y//20)))

        # showing canvas on display
        DISPLAY.fill((135, 175, 75))
        DISPLAY.blit(pygame.transform.scale(CANVAS, tuple(DISPLAY_SIZE)), (0, 0))
            
        # showing canvas
        if (DEBUG):
            pygame.draw.rect(CANVAS, "white", CANVAS.get_rect(), 1)
            DISPLAY.blit(CANVAS, (0, 0))
            
        if (ENEMY.sprite.hp <= 0):
            myWindow.makeQuizWindow()
            myWindow.QuizManager()
            if myWindow.getPlayQuiz() == False:
                del myWindow
                break
            
        if PLAYER.sprite.hp == 0:
                myWindow.gameover()   

        # updating display
        pygame.display.flip()
        pygame.display.set_caption(f"[{DESCRIPTION}]-[FPS : {CLOCK.get_fps():.2f}]")
        CLOCK.tick(FPS)
        
                       
if __name__ == "__main__":   
    Stage1()
    Stage2()
    