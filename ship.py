import pygame

class Ship:
    '''우주선 관리'''

    def __init__(self, ai_game):
        '''우주선 초기화, 시작위치 설정'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 우주선 이미지 불러오기, 사각형 만듦
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 화면아래 중앙에서 시작
        self.rect.midbottom = self.screen_rect.midbottom

        # 우주선의 가로 위치를 나타내는 소수점 있는 값 저장
        self.x = float(self.rect.x)

        # 움직임 플래그
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''움직임 플래그에 따라 우주선 위치 업데이트'''
        # rect가 아닌 우주선의 x 값을 업데이트
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed


        # self.x를 써서 rect 객체 업데이트
        self.rect.x = self.x


    def blitme(self):
        '''현재위치에 우주선을 그림'''
        self.screen.blit(self.image, self.rect)