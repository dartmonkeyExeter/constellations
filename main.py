# main.py

import pygame
import math
import random

pygame.init()
win = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("constellation maker")

running = True

class Planet_class:
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

planets = []
colour = (255,255,255)
colours = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255), (255,255,255)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            new_planet = Planet_class(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], random.randint(3, 5), 
                                colour)
            planets.append(new_planet)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            cur_mouse_pos = pygame.mouse.get_pos()
            for planet in planets:
                if planet.x - planet.radius <= cur_mouse_pos[0] <= planet.x + planet.radius and planet.y - planet.radius <= cur_mouse_pos[1] <= planet.y + planet.radius:
                    planets.remove(planet)
                    break
        if event.type == pygame.MOUSEWHEEL and event.y == 1:
            colour = colours[(colours.index(colour) + 1) % len(colours)]
        if event.type == pygame.MOUSEWHEEL and event.y == -1:
            colour = colours[(colours.index(colour) - 1) % len(colours)]
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            planets = []
    win.fill((0,0,0))
    for plan in planets:
        pygame.draw.circle(win, plan.colour, (plan.x, plan.y), plan.radius)
    
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
                pygame.draw.line(win, plan.colour, (plan.x, plan.y), (planet_connections[i].x, planet_connections[i].y))
            if distances[i] == second_lowest and distances[i] < (lowest + 50):
                pygame.draw.line(win, plan.colour, (plan.x, plan.y), (planet_connections[i].x, planet_connections[i].y))

    pygame.draw.rect(win, colour, (5, 5, 25, 25))


    pygame.display.update()
