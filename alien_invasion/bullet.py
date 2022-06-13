# bullet.py 子弹模型文件
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''一个对飞船发射的子弹进行管理的类'''

    def __init__(self, ai_settings, screen, ship):
        '''在飞船所在处的位置创建一个子弹的对象'''
        # super()来继承Sprite, 还可简写为super().__init__()
        super(Bullet, self).__init__() 
        self.screen = screen

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        '''
            pygame.Rect()类 创建这个类的实例时,
            必须提供矩形左上角的x坐标和y坐标,还有矩形的宽度和高度.
        '''
        # 子弹并非基于图像的，因此我们必须使用pygame.Rect()类从空白开始创建一个矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
                                    ai_settings.bullet_height) 
        self.rect.centerx = ship.rect.centerx # 子弹的中心继承飞船的中心
        self.rect.top = ship.rect.top # 子弹顶部属性设置为飞船的顶部

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        '''
            # 子弹从左射向右边
            self.rect.centery = ship.rect.centery # 子弹的中心继承飞船的中心
            self.rect.right = ship.rect.right # 子弹顶部属性设置为飞船的顶部

            # 存储用小数表示的子弹位置
            self.x = float(self.rect.x)
        '''
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        '''向上移动子弹'''
        # 更新表示子弹位置的数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y
        '''
            # 更新表示子弹位置的数值
            self.x += self.speed_factor
            # 更新表示子弹的rect位置
            self.rect.x = self.x
        '''


    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)




















































