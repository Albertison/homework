import pygame

if __name__ == '__main__':
    pygame.init()
    a = input().split()
    size = x, y = int(a[0]), int(a[1])
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()