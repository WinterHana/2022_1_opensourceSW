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

# 게임에서 얻는 포인트 변수 놓기
point = 0
font_point = pygame.font.SysFont(None, 30)

# 게임 종료 폰트 놓기 # text의 bool 형은 True로 하면 글씨가 좀 더 깔끔하게 보일 수 있음
font_gameover = pygame.font.SysFont(None, 80)
text_gameover = font_gameover.render("GAME OVER", True, (255, 0, 0))

size_text_width = text_gameover.get_rect().size[0]
size_text_height = text_gameover.get_rect().size[1]

# 텍스트를 중앙에 배치하기 위해서 변수 두기
x_pos_text = size_bg_width / 2 - size_text_width / 2
y_pos_text = size_bg_height / 2 - size_text_height / 2

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
        print("바닥 충돌")
        background.blit(text_gameover, (x_pos_text, y_pos_text)) # gameover 출력, 위치 지정
        pygame.display.update() # text를 출력하기 위해서 업데이트 하기
        pygame.time.delay(2000) # 2초 후에 게임이 종료되도록 지연시킴
        play = False # while문 중지
        
        y_speed_aris2 = -y_speed_aris2
        y_pos_aris2 = size_bg_height - size_aris2_height
    
    # Chapter7에서 추가
    # 충돌물이 서로 인식할 수 있도록 변수 설정하기 : rect를 이용하자
    rect_aris2 = image_aris2.get_rect()
    rect_aris2.left = x_pos_aris2
    rect_aris2.top = y_pos_aris2
    
    rect_aris = image_aris.get_rect()
    rect_aris.left = x_pos_aris
    rect_aris.top = y_pos_aris
    
    # 충돌하면 속도의 방향을 반대로 해서 튕겨나가게 하기
    if rect_aris2.colliderect(rect_aris):
        print("아리스끼리 충돌")
        point += 1
        x_speed_aris2 = - x_speed_aris2
        y_speed_aris2 = - y_speed_aris2
    
    # 사진 로드하기
    background.blit(image_bg, (0, 0))
    background.blit(image_aris, (x_pos_aris, y_pos_aris))
    background.blit(image_aris2, (x_pos_aris2, y_pos_aris2))
    
    text_point = font_point.render(str(point), True, (0, 0, 0))
    background.blit(text_point, (10, 10))
    
    pygame.display.update()
    
pygame.quit()