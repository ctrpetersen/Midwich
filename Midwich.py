import pygame
import sys
from random import randint

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r,g,b)

red = (255,0,0)
white = (255,255,255)
black= (0,0,0)

pygame.display.set_caption("slither game")
game_display = pygame.display.set_mode((800,800))
game_display.fill(white)

clock = pygame.time.Clock()

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    pygame.draw.rect(game_display, random_color(), [randint(0,800),randint(0,800),2,2])
    pygame.display.update()
    #clock.tick(120)

pygame.quit()
sys.exit()