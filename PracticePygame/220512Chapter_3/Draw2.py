import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))

pygame.display.set_caption("SONOL")

# 크기가 바뀌어도 선 유지!
x = background.get_size()[0] // 2
y = background.get_size()[1] // 2

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    background.fill((255, 255, 255))
    
    # 원
    # pygame.draw.circle(화면, 색, 중심 좌표, 반지름, 선 굵기)
    pygame.draw.circle(background, (255, 0, 0), (240, 180), 50) # 위치는 중심 기준
    
    # 사각형
    # pygame.draw.rect(화면, 색, 위치와 크기, 선 굵기)
    pygame.draw.rect(background, (0, 255, 0), (240, 180, 100, 50), 5) # 위치는 왼쪽 상단 기준
    
    # 타원
    # pygame.draw.ellipse(화면, 색, 위치와 크기, 선 굵기)
    pygame.draw.ellipse(background, (0, 0, 255), (240, 180, 100, 50)) # 위치는 외접하는 사각형이 있다고 가정한 왼쪽 상단 기준
    
    # 다각형
    # pygame.draw.polygon(화면, 색, 점들의 위치, 선 굵기)
    pygame.draw.polygon(background, (255, 255, 0), [[100, 100], [0, 200], [200, 200]]) # 점들의 좌표만 주어지면 자유롭게 그릴 수 있음
    pygame.draw.polygon(background, (255, 0, 0), ((146, 0), (292, 106), (236, 277), (56, 277), (0, 106))) # 리스트나 튜플 자유롭게 이용하기
    
    # 4등분 선 그리기
    pygame.draw.line(background, (0, 0, 0), (x, 0), (x, y * 2))
    pygame.draw.line(background, (0, 0, 0), (0, y), (x * 2, y)) 
        
    pygame.display.update() # 이거 빼먹지 마!

pygame.quit()
