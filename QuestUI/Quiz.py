import pygame
import random
import time

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

# 0. 보통, 1. 문제 맞춤, 2. 문제 틀림 으로 딕셔너리 만듬
rara = {
    0 : pygame.image.load("QuestUI/image/rara.png"),
    1 : pygame.image.load("QuestUI/image/correct_rara.png"),
    2 : pygame.image.load("QuestUI/image/incorrect_rara.png")
}
hoyoung = {
    0 : pygame.image.load("QuestUI/image/hoyoung.png"),
    1 : pygame.image.load("QuestUI/image/correct_hoyoung.png"),
    2 : pygame.image.load("QuestUI/image/incorrect_hoyoung.png")
}


OImg_width = OImg.get_size()[0]
XImg_width = XImg.get_size()[0]

rara_width = rara[0].get_size()[0]
rara_height = rara[0].get_size()[1]

hoyoung_width = hoyoung[0].get_size()[0]
hoyoung_height = hoyoung[0].get_size()[1]

# o, x의 위치 설정
x_pos_O = display_width / 2 - OImg_width * 2
y_pos_O = display_height / 2
x_pos_X = display_width / 2 + XImg_width
y_pos_X = display_height / 2

# 충돌 이벤트(마우스랑 o,x 클릭)를 위한 설정
rect_O = OImg.get_rect()
rect_O.left = x_pos_O
rect_O.top = y_pos_O

rect_X = XImg.get_rect()
rect_X.left = x_pos_X
rect_X.top = y_pos_X

# 퀴즈, 그에 따른 정답 텍스트 설정
Grammar_QuizText = pygame.font.Font('QuestUI/image/Maplestory Light.ttf', 130)
grammar_QuizAnswer = pygame.font.Font('QuestUI/image/Maplestory Light.ttf', 50)

CommonSense_QuizText = pygame.font.Font('QuestUI/image/Maplestory Light.ttf', 30)
CommonSense_QuizAnswer = pygame.font.Font('QuestUI/image/Maplestory Light.ttf', 50)

# Grammar
Grammar_QuizList = (
                ["뚝배기", True, "뚝배기"], 
                ["위쪽", True, "위쪽"], 
                ["미숫가루", True, "미숫가루"],
                ["따뜻이", True, "따뜻이"],
                ["쌍둥이", True, "쌍둥이"],
                ["귀걸이", True, "귀걸이"],
                ["이튿날", True, "이튿날"],
                ["배불뚝이", True, "배불뚝이"],
                ["섣부르다", True, "섣부르다"],
                ["헛되이", True, "헛되이"],
                ["꼼꼼히", True, "꼼꼼히"],
                ["장난꾼", True, "장난꾼"],
                ["씁쓸한", True, "씁쓸한"],
                ["기필코", True, "기필코"],
                ["무릅쓰다", True, "무릅쓰다"],
                
                ["곱배기", False, "곱빼기"],
                ["틈틈히", False, "틈틈이"],
                ["기꺼히", False, "기꺼이"],
                ["오뚜기", False, "오뚝이"],
                ["마구깐", False, "마굿간"],
                ["강남콩", False, "강낭콩"],
                ["바램", False, "바람"],  
                ["귀엄둥이", False, "귀염둥이"],
                ["몇일", False, "며칠"],
                ["딱다구리", False, "딱따구리"],  
                ["암개", False, "암캐"],
                ["홀쭈기", False, "홀쭉이"],
                ["콧베기", False, "코빼기"],
                ["깨끗히", False, "깨끗이"],
                ["분명이", False, "분명히"],
)

# CommonSense
CommonSense_QuizList = (
                ["꿀벌은 꽃에서 꿀을 채취한다. 그러므로 꽃의 꿀과 꿀벌의 꿀은 똑같다.", False], 
                ["통조림을 최초로 생각한 사람은 프랑스의 황제 나폴레옹이다.", True],
                ["달팽이도 이빨이 있다.", True],
                ["투명인간은 장님이다.", True],
                ["프랑스에서는 버섯을 따는데 돼지를 이용한다 ", True],
                ["세계 최초의 접는 부채는 일본에서 만들어졌다.", False],
                ["고기를 많이 먹으면 방귀 냄새도 더 독하다.", True],
                ["큰 충격을 받으면 하룻밤 사이에 머리가 하얗게 변한다.", False],
                ["세계최초로 일기예보를 시작한 나라는 영국이다. ", False],
                ["하늘은 땅에서도 지구 밖에서도 항상 푸르게 보인다.", False],
)
    
# 점수와 문제 수 텍스트 설정하기
point_text = pygame.font.Font('QuestUI/image/Maplestory Light.ttf', 30)
quiz_no_text = pygame.font.Font('QuestUI/image/Maplestory Light.ttf', 30)

clock = pygame.time.Clock()

## 버튼 만들기
class StartButton:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None, kind = None):
        mouse = pygame.mouse.get_pos() # 마우스 좌표 저장
        click = pygame.mouse.get_pressed() # 클릭시 실행
        if x + width > mouse[0] > x and y + height > mouse[1] > y: # 마우스가 이미지 안에 있으면
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action(kind) # 지정 함수 호출
        else:
            gameDisplay.blit(img_in,(x, y))
                
## Quiz 클래스 작성
class Quiz_play:
    def __init__(self, face, random_quiz, kind, List, point = 0, quiz_no = 1, quizAnswer = " "):
        self.__point = point # 점수
        self.__quiz_no = quiz_no # 문제 수
        self.__faceDic = face  # 표정 딕셔너리 들고 와서        
        self.__face = self.__faceDic[0] # 표정 설정
        self.__kind = kind
        self.__quizAnswer = quizAnswer
        self.__random_quiz = random_quiz
        self.__List = List
    
    # 접근자 설정    
    def getPoint(self):
        return self.__point
    
    def getQuizNo(self):
        return self.__quiz_no
    
    def getface(self):
        return self.__face
    
    def getKind(self):
        return self.__kind
    
    def getQuizAnswer(self):
        return self.__quizAnswer
    
    def getRandomquiz(self):
        return self.__random_quiz
    
     # 문제를 맞췄을 때와 틀렸을 때에 따라 다른 함수 호출하기
    def AnswerCorrect(self, random_quiz):
        self.__point += 1
        self.__quiz_no += 1
        self.__face = self.__faceDic[1]
        if self.__kind == "Grammar":
            self.__quizAnswer = "정답입니다!" + " 답은 " + self.__List[random_quiz][2] + "입니다!"
        elif self.__kind == "CommonSense":
            self.__quizAnswer = "정답입니다!"
        print("맞추셨습니다.")

    def AnswerIncorrect(self, random_quiz):
        self.__point -= 1
        self.__quiz_no += 1
        self.__face = self.__faceDic[2]
        if self.__kind == "Grammar":
            self.__quizAnswer = "오답입니다!" + " 답은 " + self.__List[random_quiz][2] + "입니다!"
        elif self.__kind == "CommonSense":
            self.__quizAnswer = "오답입니다!"
        print("틀리셨습니다.")
        
    def AnswerReset(self):
        self.__random_quiz = random.randrange(0, len(self.__List))
        return self.__random_quiz

class Quiz_Window:
    def __init__(self, DisplayWidth, DisplayHeight):
        self.__height = 300
        self.__width = self.__height * 1.61
        self.__DisplayWidth = DisplayWidth
        self.__DisplayHeight = DisplayHeight
        self.__margin = 50
        
    def makeQuizWindow(self):
        pygame.draw.rect(gameDisplay, (0, 0, 0), (self.__DisplayWidth / 2 - self.__width / 2, self.__margin, self.__width, self.__height), 5)
        gameDisplay.blit(OImg, (self.__DisplayWidth / 2 - self.__margin * 3, self.__margin + self.__height / 2))
        gameDisplay.blit(XImg, (self.__DisplayWidth / 2 + self.__margin, self.__margin + self.__height / 2))
    
    
def mainmenu():
    
    mainmenu = True
    while mainmenu:
        dt = clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        gameDisplay.fill(white)
        
        myQuizWindow = Quiz_Window(display_width, display_height)
        myQuizWindow.makeQuizWindow()
        
        raraButton = StartButton(rara[0], 445, 260, rara_width, rara_height, rara[1], 445, 260, quiz_screen, "Grammar");
        
        hoyoungButton = StartButton(hoyoung[0], 280, 260, hoyoung_width, hoyoung_height, hoyoung[1], 280, 260, quiz_screen, "CommonSense")
        
        pygame.display.update()
        clock.tick(15)

    
def quiz_screen(kind):
    
    quiz = False
    
    if(kind == "Grammar"):
        quiz = True
        List = Grammar_QuizList
        random_quiz = random.randrange(0, len(List))
        myQuiz = Quiz_play(rara, random_quiz, kind, List)
        
    elif(kind == "CommonSense"):
        quiz = True
        List = CommonSense_QuizList
        random_quiz = random.randrange(0, len(List))
        myQuiz = Quiz_play(hoyoung, random_quiz, kind, List)

    while quiz:
        dt = clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                if rect_O.collidepoint(event.pos) and List[random_quiz][1] == True:
                    myQuiz.AnswerCorrect(random_quiz)
                    random_quiz = myQuiz.AnswerReset()
                    
                elif rect_X.collidepoint(event.pos) and List[random_quiz][1] == False:
                    myQuiz.AnswerCorrect(random_quiz)
                    random_quiz = myQuiz.AnswerReset()
                    
                elif rect_O.collidepoint(event.pos) and List[random_quiz][1] == False:
                    myQuiz.AnswerIncorrect(random_quiz)
                    random_quiz = myQuiz.AnswerReset()
                    
                elif rect_X.collidepoint(event.pos) and List[random_quiz][1] == True:
                    myQuiz.AnswerIncorrect(random_quiz)
                    random_quiz = myQuiz.AnswerReset()
                    
        Quiz_content = Grammar_QuizText.render(List[random_quiz][0], True, (0, 0, 0))
        QuizAnswer_content = grammar_QuizAnswer.render(myQuiz.getQuizAnswer(), True, (0, 0, 0))
        point_content = point_text.render("Point : " + str(myQuiz.getPoint()), True, (0, 0, 0))
        quiz_no_content = quiz_no_text.render("No : " + str(myQuiz.getQuizNo()), True, (0, 0, 0))
        face_content = myQuiz.getface()
        
        gameDisplay.fill(white)
        gameDisplay.blit(OImg, (x_pos_O, y_pos_O))
        gameDisplay.blit(XImg, (x_pos_X, y_pos_X))
        gameDisplay.blit(Quiz_content, (display_width / 2 - 200 , 100))
        gameDisplay.blit(point_content, (10 , 10))
        gameDisplay.blit(quiz_no_content, (10, 40))
        gameDisplay.blit(face_content, (0, display_height - rara_height))
        gameDisplay.blit(QuizAnswer_content, (0, display_height - rara_height - 50)) 
        
        pygame.display.update()


mainmenu()