# ship.py 飞船模型文件

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置其初始位置
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        # 是一个处理矩形图像的方法，返回值包含矩形的居中属性（ center centerx centery ）
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        # 飞船x方向中心与屏幕x方向中心重合，也即x方向居中对齐属性（top bottom left right)
        self.rect.centerx = self.screen_rect.centerx 
        # self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom 

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

        # 移动标志位
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        '''根据移动标志调整飞船的位置'''
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right: # 限制移动到最右侧
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left: # 限制移动到最左侧
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: # 限制移动到最底侧
            self.center2 += self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top: # 限制移动到最顶侧
            self.center2 -= self.ai_settings.ship_speed_factor


        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.center2

    
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

















