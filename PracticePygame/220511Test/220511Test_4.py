# 전체 주석 : CTRL + /
# 한 단어 동시에 바꾸기 : CTRL + SHIFT + L
# Test_3에서 키보드를 꾹 누를 때 계속 움직일 수 있도록 개선함
import pygame

pygame.init()

# 좌표는 좌측 상단 끝이 (0, 0)이다.
#    오른쪽 X축   으로 이동해서 측정
#아래 Y축

background = pygame.display.set_mode((480, 360)) # 창의 크기
pygame.display.set_caption("SONOL") # 창의 제목

fps = pygame.time.Clock() # 프레임 조정

# 배경의 중심 좌표
x_pos = background.get_size()[0] // 2 # 240
y_pos = background.get_size()[1] // 2 # 180
# print(background.get_size()) # 사이즈의 크기가 튜플의 형태로 주어진다.

# 이동하기 위해 필요한 변수 지정
to_x = 0
to_y = 0

# 게임의 창을 계속 유지시킨다.
play = True
while play:
    deltaTime = fps.tick(60) # 프레임을 60으로 조정
    for event in pygame.event.get():
        # print(event.type) # 이벤트 코드 출력 : 아스키코드로 출력
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y = -1
            elif event.key == pygame.K_DOWN:
                to_y = 1
            elif event.key == pygame.K_RIGHT:
                to_x = 1
            elif event.key == pygame.K_LEFT:
                to_x = -1
        
        if event.type == pygame.KEYUP:
            # to_x = 0
            # to_y = 0
            if event.key == pygame.K_UP:
                to_y = 0
            elif event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0
    
    # 누적된 값을 계속 반영하기
    x_pos += to_x
    y_pos += to_y
    
    # 위에서 아래로 진행하기 때문에, background 먼저 설정해야지 다른 오브젝트가 들어갈 수 있다.
    background.fill((255,255,255)) # 디폴트는 검은색
    #pygame.draw.circle(surface, color, center, radius)
    pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)
    pygame.display.update() # 계속 업데이트 해야한다.
    
pygame.quit()

# print(pygame.K_1)
# print(pygame.K_a)
# print(pygame.K_LEFT)