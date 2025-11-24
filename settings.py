class Settings:
    """세팅 저장 클래스"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 우주선 세팅
        self.ship_speed = 1.5

        # 탄환 세팅
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 외계인 세팅
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1
        # fleet_direction {1:오른쪽, -1:왼쪽}
        self.fleet_direction = 1

