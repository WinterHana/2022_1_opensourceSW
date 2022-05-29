# 전체 주석 : CTRL + /
import pygame

pygame.init()

background = pygame.display.set_mode((480, 360)) # 창의 크기
pygame.display.set_caption("SONOL") # 창의 제목

# 좌표는 좌측 상단 끝이 (0, 0)이다.
#    오른쪽    으로 이동해서 측정
#아래


x_pos = background.get_size()[0] // 2 # 240
y_pos = background.get_size()[1] // 2 # 180


# print(background.get_size()) # 사이즈의 크기가 튜플의 형태로 주어진다.

# 게임의 창을 계속 유지시킨다.
play = True
while play:
    for event in pygame.event.get():
        # print(event.type) # 이벤트 코드 출력 : 아스키코드로 출력
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                y_pos = y_pos - 10
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                y_pos = y_pos + 10
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                x_pos = x_pos + 10
            elif event.key == pygame.K_LEFT:
                print("LEFT")
                x_pos = x_pos - 10
                
    # 위에서 아래로 진행하기 때문에, background 먼저 설정해야지 다른 오브젝트가 들어갈 수 있다.
    background.fill((255,255,255)) # 디폴트는 검은색
    #pygame.draw.circle(surface, color, center, radius)
    pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)
    pygame.display.update() # 계속 업데이트 해야한다.
    
pygame.quit()

# print(pygame.K_1)
# print(pygame.K_a)
# print(pygame.K_LEFT)