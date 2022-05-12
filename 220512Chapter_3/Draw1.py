import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))

pygame.display.set_caption("왜 안돼?")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    background.fill((255, 255, 255))
    
    # # 선
    # # pygame.draw.line(화면, 색, 시작 위치, 끝 위치, 선 굵기)
    # pygame.draw.line(background, (0, 0, 0), (240, 0), (240, 360))
    # pygame.draw.line(background, (0, 0, 0), (0, 180), (480, 180))
    # pygame.draw.line(background, (0, 0, 0), (0, 0), (480, 360), 5)
    # pygame.draw.line(background, (0, 0, 0), (0, 360), (480, 0), 5)
    
    for i in range(0 , 480, 30):
        pygame.draw.line(background, (0, 0, 0), (i, 0), (i, 360))
    for i in range(0 , 360, 30):
        pygame.draw.line(background, (0, 0, 0), (0, i), (480, i))    
        
    pygame.display.update() # 이거 빼먹지 마!

pygame.quit()
