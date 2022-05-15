import pygame

pygame.init()

# 이미지 로드
image_bg = pygame.image.load("테스트용 이미지/키보토스 배경.jpeg")
image_aris = pygame.image.load("테스트용 이미지/편하게쓰는아리스2.png")
image_aris2 = pygame.image.load("테스트용 이미지/편하게쓰는아리스.png")

# 배경 크기 변수 > 미리 설정해서 디스플레이에 맞춤
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
y_pos_aris = size_bg_height - size_aris_height

# 움직이는 아리스 크기
size_aris2_width = image_aris2.get_size()[0]
size_aris2_height = image_aris2.get_size()[1]

# 움직이는 아리스 중앙에 놓기
x_pos_aris2 = size_bg_width / 2 - size_aris2_width / 2
y_pos_aris2 = 0

# 키보드로 이동하기 위해 필요한 변수 지정
to_x = 0

# 움직이는 아리스 속도 조절
x_speed_aris2 = 10
y_speed_aris2 = 10

# 게임의 창을 계속 유지시킨다.
play = True
while play:
    deltaTime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    # 1. 키보드 조작 x 축으로만 이동
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            to_x = 10
        elif event.key == pygame.K_LEFT:
            to_x = -10     
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            to_x = 0
        elif event.key == pygame.K_LEFT:
            to_x = 0
            
    if x_pos_aris < 0:
        x_pos_aris = 0
    elif x_pos_aris > size_bg_width - size_aris_width:
        x_pos_aris = size_bg_width - size_aris_width
    else:
        x_pos_aris += to_x
    
    # 누적된 값을 계속 반영하기
    x_pos_aris += to_x    
         
    # 2. 튕기기
    # 속도 반영
    x_pos_aris2 += x_speed_aris2
    y_pos_aris2 += y_speed_aris2
        
    # 부딪히면 튕기게 하게
    if x_pos_aris2 <= 0: # 왼쪽에 부딪힐 때
        x_speed_aris2 = -x_speed_aris2 # x쪽으로의 방향이 반대가 되면 이동 방향이 튕기는 것처럼 반대가 됨
        x_pos_aris2 = 0
            
    elif x_pos_aris2 >= size_bg_width - size_aris2_width: # 오른쪽에 부딪힐 때
        x_speed_aris2 = -x_speed_aris2
        x_pos_aris2 = size_bg_width - size_aris2_width
            
    elif y_pos_aris2 <= 0: # 위에 부딪힐 때
        y_speed_aris2 = -y_speed_aris2
        y_pos_aris2 = 0
    elif y_pos_aris2 >= size_bg_height - size_aris2_height: # 아래에 부딪힐 때
        y_speed_aris2 = -y_speed_aris2
        y_pos_aris2 = size_bg_height - size_aris2_height
            
    # 사진 로드하기
    background.blit(image_bg, (0, 0))
    background.blit(image_aris, (x_pos_aris, y_pos_aris))
    background.blit(image_aris2, (x_pos_aris2, y_pos_aris2))
    
    pygame.display.update()
    
pygame.quit()