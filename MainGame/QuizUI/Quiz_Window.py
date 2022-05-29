from tkinter import Button
import pygame
import random

from scripts import *

from .ImageAndList import *
from .Button import *
from .Quiz_play import *

class Quiz_Window:
    # 전시할 스크린 / 스크린의 크기 , 폰트 사이즈, count, 퀴즈 리스트
    def __init__(self, screen, screen_size, Max_count, FontSize, width_scale = 1, List = None):
        # 창 크기
        self.height = 300
        self.width = self.height * 2 * width_scale
        self.DisplayWidth = screen_size[0]
        self.DisplayHeight = screen_size[1]
        # 전시할 화면 저장
        self.screen = screen
        # 퀴즈 리스트 저장
        self.List = List
        # 간격 조절용 상수
        self.margin = 50
        # 랜덤 퀴즈 번호
        self.random_quiz = random.randrange(0, len(self.List))
        # ox 버튼 위치, 퀴즈 내용, 답 내용 위치 설정
        self.OButton_pos = (self.DisplayWidth / 2 - self.margin * 3, self.margin + self.height / 2)
        self.XButton_pos = (self.DisplayWidth / 2 + self.margin, self.margin + self.height / 2)
        self.Quiz_pos = (self.DisplayWidth / 2 - self.width / 2 + self.margin , self.margin)
        self.Answer_pos = (self.DisplayWidth / 2 - self.width / 2 + self.margin, self.margin + self.height)
        self.rect_pos = (self.DisplayWidth / 2 - self.width / 2, self.margin, self.width, self.height)
        
        # 퀴즈 개수 설정
        self.Count = 0
        self.Max_Count = Max_count
        
        # 퀴즈 실행 여부 확인
        self.PlayQuiz = True
        
        # Quiz_play 객체 설정
        self.Quiz_play = Quiz_play(self.random_quiz, self.List)
        # 퀴즈 내용 폰트 크기 설정
        self.FontSize = FontSize
        # 퀴즈 답 출력 용 변수
        self.Answer = " "
    
    # 퀴즈 창 만듬
    def makeQuizWindow(self):
        # 틀 출력
        pygame.draw.rect(self.screen, White, self.rect_pos)
        
        # 버튼 출력
        self.OXButton_group = pygame.sprite.Group()
        self.OButton = OXButton(OX_List[2], OX_List[0], self.OButton_pos)
        self.XButton = OXButton(OX_List[3], OX_List[1], self.XButton_pos)
        self.OXButton_group.add(self.OButton)
        self.OXButton_group.add(self.XButton)
        self.OXButton_group.draw(self.screen)
        
        # 퀴즈 내용 출력
        self.QuizText = pygame.font.Font('MainGame/QuizImage/Maplestory Light.ttf', int(self.FontSize))
        self.Quiz_content = self.QuizText.render(self.List[self.random_quiz][0], True, (0, 0, 0))
        self.screen.blit(self.Quiz_content, self.Quiz_pos)
        
        # 퀴즈 답 출력
        self.AnswerText = pygame.font.Font('MainGame/QuizImage/Maplestory Light.ttf', ANSWERQUIZ_SIZE)
        self.Answer_content = self.AnswerText.render(self.Answer, True, (0, 0, 0))
        self.screen.blit(self.Answer_content, self.Answer_pos)
    
        
    # 퀴즈의 정답 유무 확인    
    def QuizManager(self):
        if self.OButton.getClick() == True and self.List[self.random_quiz][1] == True:
            self.Answer = "정답!"
            self.Quiz_play.AnswerCorrect()
            self.random_quiz = self.Quiz_play.AnswerReset()
            self.Count += 1
            print(self.Count)
            print(self.Max_Count)
            
        elif self.OButton.getClick() == True and self.List[self.random_quiz][1] == False:
            self.Answer =  "오답!"
            self.Quiz_play.AnswerIncorrect()
            self.random_quiz = self.Quiz_play.AnswerReset()
            self.Count += 1
            print(self.Count)
            print(self.Max_Count)
            
        elif self.XButton.getClick() == True and self.List[self.random_quiz][1] == False:
            self.Answer = "정답!"
            self.Quiz_play.AnswerCorrect()
            self.random_quiz = self.Quiz_play.AnswerReset()
            self.Count += 1
            print(self.Count)
            print(self.Max_Count)
        
        elif self.XButton.getClick() == True and self.List[self.random_quiz][1] == True:
            self.Answer = "오답!"
            self.Quiz_play.AnswerIncorrect()
            self.random_quiz = self.Quiz_play.AnswerReset()
            self.Count += 1
            print(self.Count)
            print(self.Max_Count)
        
        if self.Count == self.Max_Count:
            self.PlayQuiz = False
        
    # 소멸자
    def __del__(self):
        print("객체가 소멸됩니다.")
    
    def getPlayQuiz(self):
        return self.PlayQuiz
    
    def gameover(self):
        del self.OButton
        del self.XButton
        pygame.draw.rect(self.screen, White, self.rect_pos)
        self.GameOverText = pygame.font.Font('MainGame/QuizImage/Maplestory Light.ttf', 50)
        self.Quiz_content = self.GameOverText.render("게임에서 졌습니다...", True, (0, 0, 0))
        