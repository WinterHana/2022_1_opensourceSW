from scripts import *
from QuizUI import *

myWindow = Quiz_Window(CANVAS, 1500, 600, GRAMMARQUIZ_SIZE, Grammar_QuizList)

# main loop
while True:
    
    # checking for events
    for e in pygame.event.get():
        if (e.type is pygame.QUIT):
            pygame.quit()
            sys.exit()
    
    # clearing canvas
    CANVAS.fill((35, 35, 35))
    
    myWindow.makeQuizWindow()
    myWindow.QuizManager()
    
    # drawing environments
    # LEVEL.draw(CANVAS) 

    # drawing & updating enemies
    # ENEMIES.draw(CANVAS)
    # ENEMIES.update()

    # drawing & updating player
    PLAYER.draw(CANVAS)
    PLAYER.update()

    # showing canvas on display
    DISPLAY.blit(pygame.transform.scale(CANVAS, tuple(DISPLAY_SIZE)), (0, 0))
    # showing canvas
    if (DEBUG):
        pygame.draw.rect(CANVAS, "white", CANVAS.get_rect(), 1)
        DISPLAY.blit(CANVAS, (0, 0))

    # updating display
    pygame.display.flip()
    pygame.display.set_caption(f"[Sejong Uni. Open Source Project]-[FPS : {CLOCK.get_fps():.2f}]")
    CLOCK.tick(FPS)
