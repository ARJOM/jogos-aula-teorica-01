import pygame
from pygame.locals import *
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movimentação com Pygame")

mouse = 'cursor.png'
token = pygame.image.load(mouse).convert_alpha()
token = pygame.transform.scale(token, (40, 40))

white = (255, 255, 255)
blue = (0, 0, 255)

x, y = width // 2, height // 2
speed = 0.3

is_fullscreen = False

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:
            is_fullscreen = not is_fullscreen
            if is_fullscreen:
                screen = pygame.display\
                    .set_mode((width, height), FULLSCREEN)
            else:
                screen = pygame.display.set_mode((width, height), 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += speed

        screen.fill(blue)

        screen.blit(token, (x, y))

        pygame.display.flip()
