import pygame
import sys
from random import randint
import numpy as np

white = (255,255,255)
screen_size = (1000, 1000)

color_weight = 1.1
game_display = pygame.display.set_mode((screen_size))
game_display.fill(white)
clock = pygame.time.Clock()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r,g,b)

def initial_seed():
    middle_pos_width  = int(screen_size[0] / 2)
    middle_pos_height = int(screen_size[1] / 2)
    
    for xo in range(-2, 3):
        for yo in range(-2, 3):
            pygame.draw.rect(game_display, random_color(), [middle_pos_height + xo, middle_pos_height + yo, 1, 1])

def can_place_pixel(x,y):
    px = []
    can_place = False
    c1 = game_display.get_at((x-1,y+1))[:3]
    c2 = game_display.get_at((x,y+1))[:3]
    c3 = game_display.get_at((x+1,y+1))[:3]
    c4 = game_display.get_at((x-1,y))[:3]
    c5 = game_display.get_at((x+1,y))[:3]
    c6 = game_display.get_at((x-1,y-1))[:3]
    c7 = game_display.get_at((x,y-1))[:3]
    c8 = game_display.get_at((x+1,y-1))[:3]
    px += c1,c2,c3,c4,c5,c6,c7,c8

    for p in px:
        if p != white:
            can_place = True
    return can_place


#GRID
#   123
#   4P5
#   678
#Read nearby pixels
def average_color_of_px(x,y):
    c1 = game_display.get_at((x-1,y+1))[:3]
    c2 = game_display.get_at((x,y+1))[:3]
    c3 = game_display.get_at((x+1,y+1))[:3]
    c4 = game_display.get_at((x-1,y))[:3]
    c5 = game_display.get_at((x+1,y))[:3]
    c6 = game_display.get_at((x-1,y-1))[:3]
    c7 = game_display.get_at((x,y-1))[:3]
    c8 = game_display.get_at((x+1,y-1))[:3]

    nearby_pixels = []
    if c1 != white:
        nearby_pixels += c1
    if c2 != white:
        nearby_pixels += c2
    if c3 != white:
        nearby_pixels += c3
    if c4 != white:
        nearby_pixels += c4
    if c5 != white:
        nearby_pixels += c5
    if c6 != white:
        nearby_pixels += c6
    if c7 != white:
        nearby_pixels += c7
    if c8 != white:
        nearby_pixels += c8
    
    if len(nearby_pixels) > 1:
        avg_red   = 0
        avg_green = 0
        avg_blue  = 0
        try:
            for r in nearby_pixels:
                avg_red   += r[0]
                avg_green += r[1]
                avg_blue  += r[2]
            avg_red   = int(avg_red   / len(nearby_pixels))
            avg_green = int(avg_green / len(nearby_pixels))
            avg_blue  = int(avg_blue  / len(nearby_pixels))
        except:
            print("Error getting average color.")
            return random_color()
        avg_color = (avg_red, avg_blue, avg_blue)
        return avg_color
    else:
        return random_color()

def draw_random_pixel():
    pos = (randint(10, 790), randint(50, 790))
    px_color = game_display.get_at(pos)[:3]
    if px_color == white:
        avg_color = average_color_of_px(pos[0], pos[1])
        print(str(avg_color))
        pygame.draw.rect(game_display, avg_color, [pos[0], pos[1],2,2])





#pygame.draw.rect(game_display, random_color(), [50, 50, 500, 500])
print(can_place_pixel(100, 100))
initial_seed()
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    #draw_random_pixel()
    pygame.display.update()

pygame.quit()
sys.exit()