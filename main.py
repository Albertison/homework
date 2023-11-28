import pygame

if __name__ == '__main__':
    pygame.init()
    a = input().split()
    size = height, weight = int(a[0]), int(a[1])
    screen = pygame.display.set_mode(size)
    color = pygame.Color('white')
    pygame.draw.line(screen, color, (0, 0), (height, weight), 5)
    pygame.draw.line(screen, color, (height, 0), (0, weight), 5)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
