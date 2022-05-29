# 전체 주석 : CTRL + /
import pygame

pygame.init()

background = pygame.display.set_mode((480, 360)) # 창의 크기
pygame.display.set_caption("SONOL") # 창의 제목

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
            if event.key == pygame.K_DOWN:
                print("DOWN")
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
            if event.key == pygame.K_LEFT:
                print("LEFT")

pygame.quit()

# print(pygame.K_1)
# print(pygame.K_a)
# print(pygame.K_LEFT)