from tokenize import group
import pygame
import time
from .ImageAndList import *
           
class OXButton(pygame.sprite.Sprite):
    def __init__(self, image, image_touch, position, action = None):
        pygame.sprite.Sprite.__init__(self)
        self.click = False
        size = BUTTON_SIZE
        mouse = pygame.mouse.get_pos() # 마우스 좌표 저장
        click = pygame.mouse.get_pressed() # 클릭시 실행
        self.rect = pygame.Rect(position, size)
        self.image = image
        if self.rect.collidepoint(mouse):
            self.image = image_touch
            if click[0]:
                pygame.time.delay(80)
                self.click = True
        else:
            self.image = image
            self.click = False
    
    def getClick(self):
        return self.click
                    
        
        
            
        
        
            
        