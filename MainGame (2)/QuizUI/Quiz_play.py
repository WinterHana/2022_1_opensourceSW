import random
from scripts import *

class Quiz_play:
    def __init__(self,  random_quiz, List):      
        self.random_quiz = random_quiz
        self.List = List
        
    # 접근자 설정    
    def getRandomquiz(self):
        return self.random_quiz
    
     # 문제를 맞췄을 때와 틀렸을 때에 따라 다른 함수 호출하기
    def AnswerCorrect(self):
        print("맞추셨습니다.")

    def AnswerIncorrect(self):
        print("틀리셨습니다.")
        PLAYER.sprite.hp -= 10
        
    def AnswerReset(self):
        self.random_quiz = random.randrange(0, len(self.List))
        return self.random_quiz
    

        