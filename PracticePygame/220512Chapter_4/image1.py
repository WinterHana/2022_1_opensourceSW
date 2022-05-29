from ctypes import sizeof
import pygame

pygame.init()

background = pygame.display.set_mode((2000, 1000))
pygame.display.set_caption("SONOL")
# jpg로 하면 배경이 안 잘릴 수도 있음
# 사진이 같은 위치에 있으면, 그 경로는 생략이 가능!
image_aris_1 = pygame.image.load("테스트용 이미지/아리스_1.png") 
image_aris_2 = pygame.image.load("테스트용 이미지/아리스_2.png")
image_aris_3 = pygame.image.load("테스트용 이미지/아리스_3.png")
image_aris_4 = pygame.image.load("테스트용 이미지/아리스_4.png")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_aris_width  = image_aris_1.get_rect().size[0]
size_aris_height  = image_aris_1.get_rect().size[1]

# 중심 밑에 물체 놓기!
x_pos_aris = size_bg_width / 2 - size_aris_width / 2
y_pos_aris = size_bg_height - size_aris_height

print(size_aris_width, size_aris_height)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    background.blit(image_aris_1, (0, 0)) # 사각형 좌측 상단의 점을 기준으로 하기 때문에, 사진의 가로, 세로 사이즈를 구하는게 좋다.
    background.blit(image_aris_2, (500, 0))
    background.blit(image_aris_3, (1000, 0))
    background.blit(image_aris_4, (x_pos_aris, y_pos_aris + 500))
    
    pygame.draw.line(background, (255, 255, 255), (size_bg_width / 2, 0), (size_bg_width / 2, size_bg_height))
    pygame.draw.line(background, (255, 255, 255), (0, size_bg_height / 2), (size_bg_width, size_bg_height / 2)) 
    
    pygame.display.update() # 이거 빼먹지 마!

pygame.quit()
