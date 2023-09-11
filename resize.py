import pygame
from pygame.locals import *
from sys import exit

image_bg = 'background.jpg'
mouse = 'cursor.png'

pygame.init()

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE)
pygame.display.set_caption("Jojo")

background = pygame.image.load(image_bg).convert()
background = pygame.transform.scale(background, SCREEN_SIZE)

if __name__=="__main__":
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE)
            pygame.display.set_caption(f"Dimensões atuais: {str(event.size)}")

        screen_width, screen_height = SCREEN_SIZE
        for y in range(0, screen_height, background.get_height()):
            for x in range(0, screen_width, background.get_width()):
                screen.blit(background, (x, y))

        pygame.display.update()