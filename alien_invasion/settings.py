# settings.py 配置文件

# 创建设置类
class Settings():
    """存储<<外星人入侵>>的所有设置类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200        # 屏幕宽度
        self.screen_height = 800        # 屏幕高度
        self.bg_color = (230, 230, 230) # 背景颜色

        # 飞船的设置
        self.ship_speed_factor = 1.5    # 移动像素宽度
        self.ship_limit = 3             # 飞船数量

        # 子弹设置
        self.bullet_speed_factor = 3        # 子弹速度
        self.bullet_width = 3               # 子弹宽度
        self.bullet_height = 15             # 子弹长度
        self.bullet_color = (60, 60 ,60)    # 子弹颜色
        self.bullets_allowed = 300            # 子弹最大数量

        # 外星人的设置
        self.alien_speed_factor = 1         # 外星人左右移动速度
        self.fleet_drop_speed = 3          # 外星人下降速度
        self.fleet_direction = 1            # 为1表示向右移，-1为向左移

        # 以什么样的速度加快游戏节奏
        """
            用于控制游戏节奏的加快速度:2表示玩家每提高一个等级,游戏的节奏就翻倍;
            1表示游戏节奏始终不变.
            将其设置为1.1能够将游戏节奏提高到够快,让游戏既有难度,又并非不可完成
        """
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self):
        """初始化随游戏进行进而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    
    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)









