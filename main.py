# main.py

import pygame
import math
import random

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("")

running = True

class Planet_class:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.connections = 0
        self.lines_to_draw = []

planets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            new_planet = Planet_class(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], random.randint(3, 5), 
                                (255,255,255))
            planets.append(new_planet)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            cur_mouse_pos = pygame.mouse.get_pos()
            for planet in planets:
                if planet.x - planet.radius <= cur_mouse_pos[0] <= planet.x + planet.radius and planet.y - planet.radius <= cur_mouse_pos[1] <= planet.y + planet.radius:
                    planets.remove(planet)
                    break
    win.fill((0,0,0))
    for plan in planets:
        pygame.draw.circle(win, plan.color, (plan.x, plan.y), plan.radius)
    
    for plan in planets:
        for plan2 in planets:
                if plan2 != plan and plan2.connections < 3 and plan.connections < 3:
                    plan.lines_to_draw.append(((255,255,255), (plan.x, plan.y), (plan2.x, plan2.y), 1))
                    plan2.lines_to_draw.append(((255,255,255), (plan.x, plan.y), (plan2.x, plan2.y), 1))
                    plan.connections += 1
                    plan2.connections += 1

    for plan in planets:
        for line in plan.lines_to_draw:
            pygame.draw.line(win, line[0], line[1], line[2], line[3])


    pygame.display.update()

