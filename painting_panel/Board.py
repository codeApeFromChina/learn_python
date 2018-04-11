import pygame
from pygame.locals import *
import math


# 画笔
class Brush:
    def __init__(self, screen):
        '''
        初始化
        '''
        self.screen = screen
        self.color = (0, 0, 0)
        self.size = 1
        self.drawing = False
        self.last_pos = None
        self.style = True
        self.brush = pygame.image.load('resources/image/images/brush.png').convert_alpha()  # type:pygame.Surface
        self.brush_now = self.brush.subsurface((0, 0), (1, 1))
        pass

    def start_draw(self, pos):
        '''
        开始画
        :return: 
        '''
        self.drawing = True
        self.last_pos = pos

    def end_draw(self):
        '''
        结束画
        :return: 
        '''
        self.drawing = False

    def set_brush_style(self, style):
        '''
        设置画笔样式
        :param style: 
        :return: 
        '''
        self.style = style

    def get_brush_style(self):
        '''
        获取画笔style
        :return: 
        '''
        return self.style

    def get_current_brush(self):
        '''
        获取当前画笔
        :return: 
        '''
        return self.brush

    def set_size(self, size):
        '''
        设置笔刷大小
        :param size: 
        :return: 
        '''
        if size < 1:
            self.size = 1
        elif size > 32:
            self.size = 32

        self.size = size
        self.brush.subsurface((0, 0), (size * 2, size * 2))

    def get_size(self):
        '''
        获取笔刷大小
        :return: 
        '''
        return self.size

    def get_color(self):
        '''
        获取笔刷颜色
        :return: 
        '''
        return self.color

    def set_color(self, color):
        '''
        设置笔刷颜色
        :return: 
        '''
        self.color = color

        for i in range(self.brush.get_width()):
            for j in range(self.brush.get_height()):
                self.brush.set_at((i, j), color + (self.brush.get_at((i, j)).a,))

    def draw(self, pos):
        '''
        画
        :return: 
        '''
        if self.drawing:
            for p in self.__get_points(pos):
                if self.style:
                    self.screen.blit(self.brush_now, p)
                else:
                    pygame.draw.circle(self.screen, self.color, p, self.size)

    def __get_points(self, pos):
        points = [(self.last_pos[0], self.last_pos[1])]
        len_x = pos[0] - self.last_pos[0]
        len_y = pos[1] - self.last_pos[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)
        step_x = len_x / length
        step_y = len_y / length

        for i in range(int(length)):
            points.append((points[-1][0] + step_x, points[-1][ 1] + step_y))


        points = map(lambda x: (int(0.5 + x[0]), int(0.5 + x[1])), points)

        return list(set(points))


# 菜单
class Menu:
    pass

    def __init__(self, screen):
        '''
        初始化
        '''
        self.screen = screen
        self.colors = [
            (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),
            (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),
            (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),
            (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),
            (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),
            (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),
            (0xc0, 0xc0, 0xc0), (0xff, 0xff, 0xff),
            (0x00, 0x00, 0x00), (0x80, 0x80, 0x80),
        ]
        self.colors_rect = []
        for (i, rgb) in enumerate(self.colors):
            rect = pygame.Rect(10 + i % 2 * 32, 254 + i / 2 * 32, 32, 32)
            self.colors_rect.append(rect)

        self.pens = [
            pygame.image.load("resources/image/images/pen1.png").convert_alpha(),
            pygame.image.load("resources/image/images/pen2.png").convert_alpha()
        ]
        self.pens_rect = []
        for (i, image) in enumerate(self.pens):
            self.pens_rect.append(pygame.Rect(10, 10 + i * 64, 64, 64))

        self.sizes_rect = []
        self.sizes = [
            pygame.image.load("resources/image/images/big.png").convert_alpha(),
            pygame.image.load("resources/image/images/small.png").convert_alpha()
        ]

        for (i, image) in enumerate(self.sizes):
            self.sizes_rect.append(pygame.Rect(10 + i * 32, 138, 32, 32))

    def set_brush(self, brush):
        '''
        设置画笔
        :return: 
        '''
        self.brush = brush

    def draw(self, ):
        '''
        绘制菜单栏
        :return: 
        '''
        # 绘制画笔样式按钮
        for (i, img) in enumerate(self.pens):
            self.screen.blit(img, self.pens_rect[i].topleft)
        # 绘制 + - 按钮
        for (i, img) in enumerate(self.sizes):
            self.screen.blit(img, self.sizes_rect[i].topleft)
        # 绘制用于实时展示笔刷的小窗口
        self.screen.fill((255, 255, 255), (10, 180, 64, 64))
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 180, 64, 64), 1)
        size = self.brush.get_size()
        x = 10 + 32
        y = 180 + 32
        # 如果当前画笔为 png 笔刷，则在窗口中展示笔刷
        # 如果为铅笔，则在窗口中绘制原点
        if self.brush.get_brush_style():
            x = x - size
            y = y - size
            self.screen.blit(self.brush.get_current_brush(), (x, y))
        else:
            # BUG
            pygame.draw.circle(self.screen,
                               self.brush.get_color(), (x, y), size)
        # 绘制色块
        for (i, rgb) in enumerate(self.colors):
            pygame.draw.rect(self.screen, rgb, self.colors_rect[i])

    def click_button(self, pos):
        '''
        菜单的点击相应按钮
        :param pos: 
        :return: 
        '''
        # 笔刷
        for (i, rect) in enumerate(self.pens_rect):
            if rect.collidepoint(pos):
                self.brush.set_brush_style(bool(i))
                return True
        # 笔刷大小
        for (i, rect) in enumerate(self.sizes_rect):
            if rect.collidepoint(pos):
                # 画笔大小的每次改变量为 1
                if i:
                    self.brush.set_size(self.brush.get_size() - 1)
                else:
                    self.brush.set_size(self.brush.get_size() + 1)
                return True
        # 颜色
        for (i, rect) in enumerate(self.colors_rect):
            if rect.collidepoint(pos):
                self.brush.set_color(self.colors[i])
                return True
        return False


# 画板
class Painter:
    pass

    def __init__(self):
        # 设置了画板窗口的大小与标题
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Painter")
        # 创建 Clock 对象
        self.clock = pygame.time.Clock()
        # 创建 Brush 对象
        self.brush = Brush(self.screen)
        # 创建 Menu 对象，并设置了默认笔刷
        self.menu = Menu(self.screen)
        self.menu.set_brush(self.brush)

    def run(self):
        self.screen.fill((255, 255, 255))
        # 程序的主体是一个循环，不断对界面进行重绘，直到监听到结束事件才结束循环
        while True:
            # 设置帧率
            self.clock.tick(30)
            # 监听事件
            for event in pygame.event.get():
                # 结束事件
                if event.type == QUIT:
                    return
                # 键盘按键事件
                elif event.type == KEYDOWN:
                    # 按下 ESC 键，清屏
                    if event.key == K_ESCAPE:
                        self.screen.fill((255, 255, 255))
                # 鼠标按下事件
                elif event.type == MOUSEBUTTONDOWN:
                    # 若是当前鼠标位于菜单中，则忽略掉该事件
                    # 否则调用 start_draw 设置画笔的 drawing 标志为 True
                    if event.pos[0] <= 74 and self.menu.click_button(event.pos):
                        pass
                    else:
                        self.brush.start_draw(event.pos)
                # 鼠标移动事件
                elif event.type == MOUSEMOTION:
                    self.brush.draw(event.pos)
                # 松开鼠标按键事件
                elif event.type == MOUSEBUTTONUP:
                    # 调用 end_draw 设置画笔的 drawing 标志为 False
                    self.brush.end_draw()
            # 绘制菜单按钮
            self.menu.draw()
            # 刷新窗口
            pygame.display.update()


def main():
    pass
    app = Painter()
    app.run()


if __name__ == '__main__':
    main()
    a = [1, 2, 3]
    print(list(map(lambda x: x + 1, a)))
