import pygame
import random

pygame.init()

# 색깔
white = (255, 255, 255)
# 회면 크기 및 타이틀 설정
display_width = 800 # 가로 길이
display_height = 600 # 세로 길이
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("퀴즈 UI 제작")

# o,x 저장, rect 가져오기
OImg = pygame.image.load("QuestUI/image/o.png")
XImg = pygame.image.load("QuestUI/image/x.png")
OImg_width = OImg.get_size()[0]
XImg_width = XImg.get_size()[0]

# o, x의 위치 설정
x_pos_O = display_width / 2 - OImg_width * 2
y_pos_O = display_height / 2
x_pos_X = display_width / 2 + XImg_width
y_pos_X = display_height / 2

# 충돌 이벤트를 위한 설정
rect_O = OImg.get_rect()
rect_O.left = x_pos_O
rect_O.top = y_pos_O

rect_X = XImg.get_rect()
rect_X.left = x_pos_X
rect_X.top = y_pos_X

# 퀴즈 텍스트 설정 및 랜덤 생성
Quiz_text = pygame.font.Font('QuestUI/image/Maplestory Light.ttf', 130)

QuizList =  [
                ["뚝배기", "True", "뚝배기"], 
                ["위쪽", "True", "위쪽"], 
                ["곱배기", "False", "곱빼기"]
            ]



clock = pygame.time.Clock()

def mainmenu():
    menu = True
    point = 0 # 점수
    random_quiz = random.randrange(0, len(QuizList))
    while menu:
        dt = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                if rect_O.collidepoint(event.pos) and QuizList[random_quiz][1] == "True":
                    print("맞춤")
                    point += 1
                    random_quiz = random.randrange(0, len(QuizList))
                    print(point)
                elif rect_X.collidepoint(event.pos) and QuizList[random_quiz][1] == "False":
                    print("맞춤")
                    point += 1
                    random_quiz = random.randrange(0, len(QuizList))
                    print(point)
                elif rect_O.collidepoint(event.pos) and QuizList[random_quiz][1] == "False":
                    print("틀림")
                    print(point)
                elif rect_X.collidepoint(event.pos) and QuizList[random_quiz][1] == "True":
                    print("틀림")
                    print(point)
                    

        Quiz = Quiz_text.render(QuizList[random_quiz][0], True, (0, 0, 0))
        gameDisplay.fill(white)
        gameDisplay.blit(OImg, (x_pos_O, y_pos_O))
        gameDisplay.blit(XImg, (x_pos_X, y_pos_X))
        gameDisplay.blit(Quiz, (display_width / 2 - 200 , 100))
        
        pygame.display.update()
        
        
mainmenu()
