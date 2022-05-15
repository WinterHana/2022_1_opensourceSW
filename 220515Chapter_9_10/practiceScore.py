import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

# 1. 폰트, 글자의 크기 지정
font_test = pygame.font.SysFont(None, 30)
Point = 10

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    # 2. 내용 적기 여기서는 문자열만 가능하기 때문에, str로 형변환을 해야 함
    text = font_test.render(str(Point), True, (0, 0, 0))
    background.fill((255, 255, 255))
    
    # 3. text의 위치 지정하기
    background.blit(text, (100, 100))
    
    pygame.display.update()


pygame.quit()