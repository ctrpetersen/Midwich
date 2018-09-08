import pygame
import sys
from random import randint
import numpy as np

white = (255,255,255)
screen_size = (800, 800)

color_weight = 1.1
game_display = pygame.display.set_mode((screen_size))
game_display.fill(white)
clock = pygame.time.Clock()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r,g,b)

#GRID
#   123
#   4P5
#   678
#Read nearby pixels
def average_color_of_px(x,y):
    nearby_pixels = []
    c1 = game_display.get_at((x-1,y+1))[:3]
    c2 = game_display.get_at((x,y+1))[:3]
    c3 = game_display.get_at((x+1,y+1))[:3]
    c4 = game_display.get_at((x-1,y))[:3]
    c5 = game_display.get_at((x+1,y))[:3]
    c6 = game_display.get_at((x-1,y-1))[:3]
    c7 = game_display.get_at((x,y-1))[:3]
    c8 = game_display.get_at((x+1,y-1))[:3]
    nearby_pixels += c1,c2,c3,c4,c5,c6,c7,c8

    avg_red   = 0
    avg_green = 0
    avg_blue  = 0
    for r in nearby_pixels:
        avg_red   += r[0]
        avg_green += r[1]
        avg_blue  += r[2]
    avg_red   = int(avg_red   / len(nearby_pixels))
    avg_green = int(avg_green / len(nearby_pixels))
    avg_blue  = int(avg_blue  / len(nearby_pixels))

    avg_color = (avg_red, avg_blue, avg_blue)
    return avg_color

def draw_random_pixel():
    pos = (randint(10, 790), randint(50, 790))
    px_color = game_display.get_at(pos)[:3]
    if px_color == white:
        avg_color = average_color_of_px(pos[0], pos[1])
        print(str(avg_color))
        pygame.draw.rect(game_display, avg_color, [pos[0], pos[1],2,2])

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    draw_random_pixel()
    pygame.display.update()

pygame.quit()
sys.exit()