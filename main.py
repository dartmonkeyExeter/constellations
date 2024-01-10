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
color = (255,255,255)
colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255), (255,255,255)]

def middle_color(color1, color2):
    middle1 = (color1[0] + color2[0]) / 2
    middle2 = (color1[1] + color2[1]) / 2
    middle3 = (color1[2] + color2[2]) / 2
    return (middle1, middle2, middle3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            new_planet = Planet_class(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], random.randint(3, 5), 
                                color)
            planets.append(new_planet)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            cur_mouse_pos = pygame.mouse.get_pos()
            for planet in planets:
                if planet.x - planet.radius <= cur_mouse_pos[0] <= planet.x + planet.radius and planet.y - planet.radius <= cur_mouse_pos[1] <= planet.y + planet.radius:
                    planets.remove(planet)
                    break
        if event.type == pygame.MOUSEWHEEL and event.y == 1:
            color = colors[(colors.index(color) + 1) % len(colors)]
        if event.type == pygame.MOUSEWHEEL and event.y == -1:
            color = colors[(colors.index(color) - 1) % len(colors)]
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            planets = []
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
        for i in range(len(distances)):  # Draw lines between planets
            if distances[i] == lowest:
                pygame.draw.line(win,
                                 middle_color(plan.color, planet_connections[i].color),
                                 (plan.x, plan.y), (planet_connections[i].x, planet_connections[i].y))
            if distances[i] == second_lowest and distances[i] < (lowest + 50):
                pygame.draw.line(win,
                                 middle_color(plan.color, planet_connections[i].color),
                                 (plan.x, plan.y), (planet_connections[i].x, planet_connections[i].y))

    pygame.draw.rect(win, color, (5, 5, 25, 25))  # Color indicator


    pygame.display.update()
    
