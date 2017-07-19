import pygame
from pygame.image import load


def main():
    # 创建窗口
    screen = pygame.display.set_mode((480, 800)) # type:pygame.Surface


    # 设置名称
    pygame.display.set_caption("first game")

    # 创建clock对象
    clock = pygame.time.Clock()


    # 加载图像并获得图像的副本
    bg = load('resources/image/background.png').convert()
    plane = load('resources/image/plane.png').convert()

    while True:
        # 设置刷新频率
        clock.tick(30)
        screen.blit(bg, (0, 0))

        (x, y) = pygame.mouse.get_pos()

        x -= plane.get_width() / 2
        y -= plane.get_height() / 2
        screen.blit(plane, (x, y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.update()


if __name__ == '__main__':
    main()
