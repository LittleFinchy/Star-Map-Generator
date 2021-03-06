import pygame, sys
from pygame import Surface
from pygame.locals import *
from beta_logic import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y), 0, 32)                      #Main Display
STARFIELDSURF = Surface((field_x + (2 * field_buffer), field_y + (2 * field_buffer)))   #Starfield
OPTIONSURF = Surface((screen_x - field_x - 2 * field_buffer, screen_y))                 #Option Bar
pygame.display.set_caption('StarMap')
display_changed = False

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
NIGHTSKY = (7, 11, 15)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NEWBLUE = (43, 67, 244)

field_point = (int(screen_x - field_x - 2 * field_buffer), int((screen_y - field_y - 2 * field_buffer) / 2))
click_areas = [((0, 0), (100, 100))]



def star_generator():
    draw_initial()
    star_data = star_placer()
    for star in star_data:
        pygame.draw.circle(STARFIELDSURF, star.color, (star.x, star.y), star.size, 0)

    list_of_lines = random_line_placer(star_data, 10, [3,4])
    for line in list_of_lines:
        pygame.draw.aalines(STARFIELDSURF, WHITE, False, line, 1)


def draw_initial():
    DISPLAYSURF.fill(BLACK)
    STARFIELDSURF.fill(BLACK)
    pygame.draw.circle(STARFIELDSURF, NIGHTSKY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), 400, 0)
    pygame.draw.circle(STARFIELDSURF, GRAY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), 400, 1)
    OPTIONSURF.fill(WHITE)

def draw_surfaces():
    DISPLAYSURF.blit(STARFIELDSURF, field_point)
    DISPLAYSURF.blit(OPTIONSURF, (0, 0))

draw_initial()
star_generator()
draw_surfaces()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for area in click_areas:
                if area[0][0] <= mouse[0] <=area[1][0] and area[0][1] <= mouse[1] <=area[1][1]:
                    if not display_changed:
                        draw_initial()
                        display_changed = True
                    star_generator()
    if display_changed:
        display_changed = False
        draw_surfaces()
    pygame.display.update()