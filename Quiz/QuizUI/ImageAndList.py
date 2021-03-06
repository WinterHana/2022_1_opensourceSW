import pygame

from .Button import *

pygame.init()

# 색깔
White = (255, 255, 255)
Red = (255, 0, 0)
Blue = (0, 0, 255)

# FPS
FPS = 30

# 회면 크기 및 타이틀 설정
display_width = 400 * 1.61 # 가로 길이
display_height = 400 # 세로 길이
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("퀴즈 UI 제작")

# o,x 저장
OImg = pygame.image.load("QuestUI/image/o.png")
XImg = pygame.image.load("QuestUI/image/x.png")
O_blueImg = pygame.image.load("QuestUI/image/o_blue.png")
X_blueImg = pygame.image.load("QuestUI/image/x_blue.png")

OX_List = [OImg, XImg, O_blueImg, X_blueImg]

# 0. 보통, 1. 문제 맞춤, 2. 문제 틀림 으로 딕셔너리 만듬
# rara = {
#     0 : pygame.image.load("QuestUI/image/rara.png"),
#     1 : pygame.image.load("QuestUI/image/correct_rara.png"),
#     2 : pygame.image.load("QuestUI/image/incorrect_rara.png")
# }

# hoyoung = {
#     0 : pygame.image.load("QuestUI/image/hoyoung.png"),
#     1 : pygame.image.load("QuestUI/image/correct_hoyoung.png"),
#     2 : pygame.image.load("QuestUI/image/incorrect_hoyoung.png")
# }


OImg_width = OX_List[0].get_size()[0]
XImg_width = OX_List[1].get_size()[0]

# 퀴즈, 그에 따른 정답 텍스트 설정
GRAMMARQUIZ_SIZE = 100
HISTORYQUIZ_SIZE = 30
ANSWERQUIZ_SIZE = 50

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