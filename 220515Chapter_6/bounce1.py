import pygame

pygame.init()

# 이미지 로드
image_bg = pygame.image.load("테스트용 이미지/키보토스 배경.jpeg")
image_aris = pygame.image.load("테스트용 이미지/편하게쓰는아리스.png")

# 배경 크기 변수
size_bg_width = image_bg.get_size()[0]
size_bg_height = image_bg.get_size()[1]

background = pygame.display.set_mode((size_bg_width, size_bg_height)) # 창의 크기 > 배경에 따라 달라짐
pygame.display.set_caption("SONOL") # 창의 제목

fps = pygame.time.Clock() 

# 아리스 크기 변수
size_aris_width = image_aris.get_size()[0]
size_aris_height = image_aris.get_size()[1]

# 아리스를 중앙에 놓기
x_pos_aris = size_bg_width / 2 - size_aris_width / 2
y_pos_aris = 0

x_speed_aris = 1
y_speed_aris = 1

# 게임의 창을 계속 유지시킨다.
play = True
while play:
    deltaTime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    # 스피드 반영!
    x_pos_aris += x_speed_aris
    y_pos_aris += y_speed_aris
    
    # 통통 튀게 하기 
    if x_pos_aris <= 0: # 왼쪽에 부딪힐 때
        x_speed_aris = -x_speed_aris # x쪽으로의 방향이 반대가 되면 이동 방향이 튕기는 것처럼 반대가 됨
        x_pos_aris = 0
        
    elif x_pos_aris >= size_bg_width - size_aris_width: # 오른쪽에 부딪힐 때
        x_speed_aris = -x_speed_aris
        x_pos_aris = size_bg_width - size_aris_width
        
    elif y_pos_aris <= 0: # 위에 부딪힐 때
        y_speed_aris = -y_speed_aris
        y_pos_aris = 0
    elif y_pos_aris >= size_bg_height - size_aris_height: # 아래에 부딪힐 때
        y_speed_aris = -y_speed_aris
        y_pos_aris = size_bg_height - size_aris_height
    
    # 사진 로드하기
    background.blit(image_bg, (0, 0))
    background.blit(image_aris, (x_pos_aris, y_pos_aris))
    
    pygame.display.update()
    
pygame.quit()