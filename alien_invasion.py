import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """게임 전체의 자원과 동작을 관리하는 클래스"""

    def __init__(self):
        '''게임 초기화, 게임자원 생성'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.ailens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        '''게임 메인루프'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

            # 사라진 탄환 제거
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                

    def _check_events(self):

        '''키보드와 마우스 주시'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # 키 입력에 반응
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # 키 뗄 때 반응
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''탄환 생성, bullets 그룹에 추가'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
            '''탄환 위치 업데이트, 사라진 탄환 제거'''
            # 탄환 위치 업데이트
            self.bullets.update()

            # 사라진 탄환 제거
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _update_aliens(self):
        '''
        Check if the fleet is at an edge,
            then update the positions of all aliens in the fleet
        '''
        self._check_fleet_edges()
        self.ailens.update()

    def _create_fleet(self):
        '''외계인 함대 생성'''
        # 외계인 하나를 만들고 한 줄에 몇이 들어갈지 정함
        # 외계인 사이의 공간은 외계인 하나의 너비
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # 화면 높이에 알맞은 외계인 줄 수 결정
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # 외계인 함대 생성
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # 외계인을 만들고 줄에 배치
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.ailens.add(alien)

    def _check_fleet_edges(self):
        '''외계인이 경계에 닿으면 반응'''
        for alien in self.ailens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''함대 전체를 아래로 내리고 방향 바꿈'''
        for alien in self.ailens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):        
        '''화면에 이미지를 업데이트하고 새 화면으로 그림'''

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ailens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    '''게임 인스턴스 생성, 게임실행'''
    ai = AlienInvasion()
    ai.run_game()
    

