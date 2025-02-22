import pygame as py
from classs_game import Circle
py.init()
w = py.display.set_mode((600, 600))
FPS = 30
clock = py.time.Clock()
circles = []
for i in range(50):
    circles.append(Circle(w))
while True:
    w.fill((255, 255, 255))
    for circle in circles:
        circle.draw()
        if circle.end():
            exit()
    py.display.update()
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    if event.type == py.MOUSEBUTTONDOWN:
        for circle in circles:
            circle.click(*py.mouse.get_pos())
    clock.tick(FPS)
