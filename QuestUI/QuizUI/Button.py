from tokenize import group
import pygame
import time
from .ImageAndList import *

# 버튼 만들기
# class StartButton:
#     def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None, kind = None):
#         mouse = pygame.mouse.get_pos() # 마우스 좌표 저장
#         click = pygame.mouse.get_pressed() # 클릭시 실행
#         if x + width > mouse[0] > x and y + height > mouse[1] > y: # 마우스가 이미지 안에 있으면
#             gameDisplay.blit(img_act, (x_act, y_act))
#             if click[0] and action != None:
#                 time.sleep(1)
#                 action(kind) # 지정 함수 호출
#         else:
#             gameDisplay.blit(img_in,(x, y))
            
class OXButton(pygame.sprite.Sprite):
    def __init__(self, image, image_touch, position, action = None):
        pygame.sprite.Sprite.__init__(self)
        self.click = False
        size = (70, 70)
        mouse = pygame.mouse.get_pos() # 마우스 좌표 저장
        click = pygame.mouse.get_pressed() # 클릭시 실행
        self.rect = pygame.Rect(position, size)
        self.image = image
        if self.rect.collidepoint(mouse):
            self.image = image_touch
            if click[0]:
                time.sleep(0.2)
                print(self.click)
                self.click = True
        else:
            self.image = image
            self.click = False
    
    def getClick(self):
        return self.click
                    
        
        
            
        
        
            
        