
import pygame, sys

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


'''
* 项目名:外星人入侵
* 日期:2022/06/13
* 283页
'''

def test():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('12-4')
    bg_color = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    bg_color = (255, 0, 0)
                elif event.key == pygame.K_LEFT:
                    bg_color = (0, 255, 0)
                elif event.key == pygame.K_UP:
                    bg_color = (0, 0, 255)
                elif event.key == pygame.K_DOWN:
                    bg_color = (0, 0, 0)
                elif event.key == pygame.K_q:
                    bg_color = (255, 255, 0)
        
        screen.fill(bg_color)
        pygame.display.flip()


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init() # 初始化背景设置
    ai_settings = Settings()
    # 创建显示窗口大小
    screen = pygame.display.set_mode((ai_settings.screen_width, 
                                        ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建存储游戏统计信息的实例，并创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组 
    bullets = Group()
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    # 创建一个用于存储外星人的编组 
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标的事件，即玩家的输入
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            aliens, bullets)

        if stats.game_active:
            # 更新飞船的位置
            ship.update()
            # 更新子弹的位置，并删除已消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
                bullets)
            # 更新外星人群位置
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, 
                bullets)

        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
            bullets, play_button)



if __name__ == '__main__':

    run_game()
    # test() # 测试四个方向按键












