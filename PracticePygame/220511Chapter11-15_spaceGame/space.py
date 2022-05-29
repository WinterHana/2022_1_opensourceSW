import pygame
import random

pygame.init()

# 이미지 설정
image_bg = pygame.image.load("테스트용 이미지/연습용_로켓게임/우주 배경.jpg")
image_aris = pygame.image.load("테스트용 이미지/연습용_로켓게임/성검아리스.png")
image_magnus = pygame.image.load("테스트용 이미지/연습용_로켓게임/매그너스.png")
image_meteor = pygame.image.load("테스트용 이미지/연습용_로켓게임/운석이당.png")
image_attack = pygame.image.load("테스트용 이미지/연습용_로켓게임/참격.png")

# 이미지의 가로, 세로 크기 구히가
size_bg_width = image_bg.get_size()[0]
size_bg_height = image_bg.get_size()[1]

size_aris_width = image_aris.get_rect().size[0]
size_aris_height = image_aris.get_rect().size[1]

size_magnus_width = image_magnus.get_rect().size[0]
size_magnus_height = image_magnus.get_rect().size[1]

size_meteor_width = image_meteor.get_rect().size[0]
size_meteor_height = image_meteor.get_rect().size[1]

size_attack_width = image_attack.get_rect().size[0]
size_attack_height = image_attack.get_rect().size[1]

# 배경화면과 타이틀 크기 조절
background = pygame.display.set_mode((size_bg_width, size_bg_height))
pygame.display.set_caption("UniverseGame")

# 이미지의 x, y좌표 설정하기
x_pos_aris = size_bg_width / 2 - size_aris_width / 2
y_pos_aris = size_bg_height - size_aris_height

x_pos_magnus = size_bg_width / 2 - size_magnus_width / 2
y_pos_magnus = 0

x_pos_attack = size_bg_width / 2 - size_attack_width / 2
y_pos_attack = size_bg_height - size_aris_height - size_attack_height

x_pos_meteor = size_bg_width / 2 - size_meteor_width / 2
y_pos_meteor = size_magnus_height


# 움직이기 위한 변수
to_x_aris = 0
to_x_magnus = 0

# x축에 대한 랜덤 값 출력하기! > magnus가 이 랜덤좌표로 향하도록 할 것
random_magnus = random.randrange(0, size_bg_width - size_magnus_width) 
speed_magnus = 3 # magnus가 움직이는 속도

# 공격 리스트
attacks = []

# 운석 발생 타이밍, 리스트
meteor_time = 0
meteors = []
random_time = random.randrange(100, 200) # 난수로 운석이 떨어지게 할 수 있음

# magnus와 aris의 체력 설정
hp_magnus = 10
hp_aris = 10

# 충돌 1-1 : 각각의 사각형 크기 가져오기
rect_magnus = image_magnus.get_rect()
rect_aris = image_aris.get_rect()

rect_magnus.topleft = (x_pos_magnus, y_pos_magnus)
rect_aris.topleft = (x_pos_aris, y_pos_aris)

# 충돌 1-2 : rect도 여러 개 생길 수 있으므로 리스트로 생성
rect_attacks = []
rect_meteors = []

# 폰트 준비
font_hp = pygame.font.SysFont(None, 30)
font_gameover = pygame.font.SysFont(None, 100)

# gameover 판정 변수
gameover = False

# while문 작동
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
        # aris는 키보드 좌우키로 움직이게 하기 >> for문 안에서 해주기
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x_aris = 3
            if event.key == pygame.K_LEFT:
                to_x_aris = -3
                
            # space를 누르면 공격
            if event.key == pygame.K_SPACE:
                x_pos_attack = x_pos_aris + size_attack_width / 2
                attacks.append([x_pos_attack, y_pos_attack])
                # 충돌 2-1 : get_rect()를 리스트에 추가
                rect_attacks.append(image_attack.get_rect())
                
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT:
                to_x_aris = 0
            if event.key == pygame.K_LEFT:
                to_x_aris = 0
                
    # magnus의 x좌표를 랜덤으로 움직이기
    if random_magnus - x_pos_magnus > 0:
        x_pos_magnus += speed_magnus
    elif random_magnus - x_pos_magnus < 0:
        x_pos_magnus -= speed_magnus
    
    if x_pos_magnus - random_magnus < speed_magnus and x_pos_magnus - random_magnus > -speed_magnus:
        random_magnus = random.randrange(0, size_bg_width - size_magnus_width)
        print(random_magnus)
    # 충돌 3-1 : topleft 값 지정
    rect_magnus.topleft = (x_pos_magnus, y_pos_magnus)
    
    # aris가 화면 밖으로 나가지 않게 움직이도록 설정하기
    if x_pos_aris < 0:
        x_pos_aris = 0
    elif x_pos_aris > size_bg_width - size_aris_width:
        x_pos_aris = size_bg_width - size_aris_width
    else:
        x_pos_aris += to_x_aris
    # 충돌 3-2 : topleft 값 지정
    rect_aris.topleft = (x_pos_aris, y_pos_aris)
    
    # 운석 공격
    meteor_time += 1 # 운석 지연 시간
    if meteor_time == random_time: # 일정한 랜덤 시간이 지나면 실행
        random_time = random.randrange(100, 200) # 랜덤 시간 다시 설정
        meteor_time = 0 # 운석 지연 시간 초기화
        x_pos_meteor = x_pos_magnus + size_meteor_width / 2
        meteors.append([x_pos_meteor, y_pos_meteor])   
        # 충돌 2-1 : get_rect()를 리스트에 추가
        rect_meteors.append(image_meteor.get_rect())
     
    
    # 이미지 그리기
    background.blit(image_bg, (0, 0))
    background.blit(image_aris, (x_pos_aris, y_pos_aris))
    background.blit(image_magnus, (x_pos_magnus, y_pos_magnus))
    
    # attacks 그리기
    if len(attacks):
        for attack in attacks:
            i = attacks.index(attack)
            attack[1] -=  3 # star[[200, 150], [250. 150], [100, 150]]에서 (200, 150) 중 150을 줄임 > y좌표 줄임
            background.blit(image_attack, (attack[0], attack[1]))
            
            # 충돌 3-3 : topleft 값 지정
            rect_attacks[i].topleft = (attack[0], attack[1])
            
            # 충돌 4-1 : 부딪히면 체력에 반영 및 물체 지우기
            if rect_attacks[i].colliderect(rect_magnus):
                attacks.remove(attack)
                rect_attacks.remove(rect_attacks[i])
                hp_magnus -= 1
                if hp_magnus == 0:
                    gameover = "Aris WIN!"
                
            if attack[1] <= 0:
                attacks.remove(attack) # 객체 하나 제거하기!
    
    # meteors 그리기
    if len(meteors):
        for meteor in meteors:
            i = meteors.index(meteor)
            meteor[1] +=  3
            background.blit(image_meteor, (meteor[0], meteor[1]))
            
            # 충돌 3-4 : topleft 값 지정
            rect_meteors[i].topleft = (meteor[0], meteor[1])
            
            # 충돌 4-2 : 부딪히면 체력에 반영 및 물체 지우기
            if rect_meteors[i].colliderect(rect_aris):
                meteors.remove(meteor)
                rect_meteors.remove(rect_meteors[i])
                hp_aris -= 1
                if hp_aris == 0:
                    gameover = "Magnus WIN!"
                    
            if meteor[1] >= size_bg_height:
                meteors.remove(meteor) # 객체 하나 제거하기!
    
    text_hp_aris = font_hp.render('Aris : ' + str(hp_aris), True, (255, 255, 0))
    background.blit(text_hp_aris, (10, 10))
    
    text_hp_magnus = font_hp.render('Magnus : ' + str(hp_magnus), True, (255, 255, 0))
    background.blit(text_hp_magnus, (size_bg_width - 130, 10))
    
    
    if gameover: # gameover에  false외에 다른 값이 들어가면 작동
        text_gameover = font_gameover.render(gameover, True, (255, 0, 0))
        
        size_text_width = text_gameover.get_rect().size[0]
        size_text_height = text_gameover.get_rect().size[1]
        
        x_pos_text = size_bg_width / 2 - size_text_width / 2
        y_pos_text = size_bg_height / 2 - size_text_height / 2
        
        background.blit(text_gameover, (x_pos_text, y_pos_text))
        pygame.display.update()
        pygame.time.delay(3000)
        
        play = False
        
    print(hp_aris, hp_magnus)  
                     
    pygame.display.update()

pygame.quit()