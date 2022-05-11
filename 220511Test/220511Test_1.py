import pygame

pygame.init()

background = pygame.display.set_mode((480, 360)) # 창의 크기
pygame.display.set_caption("SONOL") # 창의 제목

# 게임의 창을 계속 유지시킨다.
play = True
while play:
    for event in pygame.event.get():
        # print(event.type) # 이벤트 코드 출력
        if event.type == pygame.QUIT:
            play = False

pygame.quit()

# print(pygame.K_0) # 이벤트 코드가 몇인지 알 수 있음