# main.py

import pygame
import math
import random

pygame.init()
win = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("constellation maker")

running = True

class Planet_class:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

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
        distances = []
        planet_connections = []
        for plan2 in planets:
            if plan2 != plan:
                x = plan2.x - plan.x
                y = plan2.y - plan.y
                distance = math.sqrt(x**2 + y**2)
                distances.append(distance)
                planet_connections.append(plan2)
        lowest = min(distances, default=0)
        second_lowest = min([i for i in distances if i != lowest], default=0)
        for i in range(len(distances)):
            if distances[i] == lowest:
                pygame.draw.line(win, (255,255,255), (plan.x, plan.y), (planet_connections[i].x, planet_connections[i].y))
            if distances[i] == second_lowest and distances[i] < (lowest + 50):
                pygame.draw.line(win, (255,255,255), (plan.x, plan.y), (planet_connections[i].x, planet_connections[i].y))

            


    pygame.display.update()

