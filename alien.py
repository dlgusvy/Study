import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''함대에 소고한 외계인 하나 담당'''

    def __init__(self, ai_game):
        '''외계인 초기화, 시작위치'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 외계인 이미지 불러오기
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 좌 상단 배치
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 외계인의 정확한 가로 위치 저장
        self.x = float(self.rect.x)

    def check_edges(self):
        '''외계인이 화면 경계에 닿으면 True 반환'''
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True

    def update(self):
        '''외계인을 오른쪽으로 움직임'''
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x