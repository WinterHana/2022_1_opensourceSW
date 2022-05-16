import pygame
import random

pygame.init()

# 색깔
white = (255, 255, 255)
# 회면 크기 및 타이틀 설정
display_width = 1300 # 가로 길이
display_height = 600 # 세로 길이
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("퀴즈 UI 제작")

# o,x, 표정 저장, rect 가져오기
OImg = pygame.image.load("QuestUI/image/o.png")
XImg = pygame.image.load("QuestUI/image/x.png")
rara = pygame.image.load("QuestUI/image/rara.png")
correct_rara = pygame.image.load("QuestUI/image/correct_rara.png")
incorrect_rara = pygame.image.load("QuestUI/image/incorrect_rara.png")

OImg_width = OImg.get_size()[0]
XImg_width = XImg.get_size()[0]
rara_height = rara.get_size()[1]

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
                ["미숫가루", "True", "미숫가루"],
                ["따뜻이", "True", "따뜻이"],
                ["쌍둥이", "True", "쌍둥이"],
                ["귀걸이", "True", "귀걸이"],
                ["이튿날", "True", "이튿날"],
                ["배불뚝이", "True", "배불뚝이"],
                ["섣부르다", "True", "섣부르다"],
                ["헛되이", "True", "헛되이"],
                ["꼼꼼히", "True", "꼼꼼히"],
                ["장난꾼", "True", "장난꾼"],
                ["씁쓸한", "True", "씁쓸한"],
                ["기필코", "True", "기필코"],
                ["무릅쓰다", "True", "무릅쓰다"],
                
                ["곱배기", "False", "곱빼기"],
                ["틈틈히", "False", "틈틈이"],
                ["기꺼히", "False", "기꺼이"],
                ["오뚜기", "False", "오뚝이"],
                ["마구깐", "False", "마굿간"],
                ["강남콩", "False", "강낭콩"],
                ["바램", "False", "바람"],  
                ["귀엄둥이", "False", "귀염둥이"],
                ["몇일", "False", "며칠"],
                ["딱다구리", "False", "딱따구리"],  
                ["암개", "False", "암캐"],
                ["홀쭈기", "False", "홀쭉이"],
                ["콧베기", "False", "코빼기"],
                ["깨끗히", "False", "깨끗이"],
                ["분명이", "False", "분명히"],
                
            ]

# 점수와 문제 수 텍스트 설정하기
point_text = pygame.font.Font('QuestUI/image/Maplestory Light.ttf', 30)
quiz_no_text = pygame.font.Font('QuestUI/image/Maplestory Light.ttf', 30)

clock = pygame.time.Clock()

# 문제를 맞췄을 때와 틀렸을 때에 따라 다른 함수 호출하기
def AnswerCorrect(point, quiz_no):
    point += 1
    quiz_no += 1
    rara_face = correct_rara
    print("맞추셨습니다.")
    return point, quiz_no, rara_face

def AnswerIncorrect(point, quiz_no):
    point -= 1
    quiz_no += 1
    rara_face = incorrect_rara
    print("틀리셨습니다.")
    return point, quiz_no, rara_face

# 약간의 딜레이 후 원래대로 돌아감
def AnswerReturn():
    random_quiz = random.randrange(0, len(QuizList))
    rara_face = rara
    return random_quiz, rara_face
    
def mainmenu():
    menu = True
    
    point = 0 # 점수
    quiz_no = 1 # 문제 수               
    rara_face = rara # 표정 관리해!
    random_quiz = random.randrange(0, len(QuizList))
    
    while menu:
        dt = clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                if rect_O.collidepoint(event.pos) and QuizList[random_quiz][1] == "True":
                    point, quiz_no, rara_face = AnswerCorrect(point, quiz_no)
                    random_quiz = random.randrange(0, len(QuizList))
                    
                    
                elif rect_X.collidepoint(event.pos) and QuizList[random_quiz][1] == "False":
                    point, quiz_no, rara_face = AnswerCorrect(point, quiz_no)
                    random_quiz = random.randrange(0, len(QuizList))
                    
                elif rect_O.collidepoint(event.pos) and QuizList[random_quiz][1] == "False":
                    point, quiz_no, rara_face = AnswerIncorrect(point, quiz_no)
                    random_quiz = random.randrange(0, len(QuizList))
                    # pygame.time.delay(1000)
                    
                elif rect_X.collidepoint(event.pos) and QuizList[random_quiz][1] == "True":
                    point, quiz_no, rara_face = AnswerIncorrect(point, quiz_no)
                    random_quiz = random.randrange(0, len(QuizList))
                    # pygame.time.delay(1000)
                    # random_quiz , rara_face = AnswerReturn()
            
        Quiz_content = Quiz_text.render(QuizList[random_quiz][0], True, (0, 0, 0))
        point_content = point_text.render("Point : " + str(point), True, (0, 0, 0))
        quiz_no_content = quiz_no_text.render("No : " + str(quiz_no), True, (0, 0, 0))
        
        gameDisplay.fill(white)
        gameDisplay.blit(OImg, (x_pos_O, y_pos_O))
        gameDisplay.blit(XImg, (x_pos_X, y_pos_X))
        gameDisplay.blit(Quiz_content, (display_width / 2 - 200 , 100))
        gameDisplay.blit(point_content, (10 , 10))
        gameDisplay.blit(quiz_no_content, (10, 40))
        gameDisplay.blit(rara_face, (0, display_height - rara_height))
        
        pygame.display.update()
        
        
mainmenu()
