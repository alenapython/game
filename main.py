import pygame as py
from classs import Pole
py.init()
w = py.display.set_mode((600, 600))
FPS = 10
clock = py.time.Clock()
line = Pole(w, 600, 600, 200)
r = 100
while True:
    w.fill((255, 255, 255))
    line.draw()
    if py.mouse.get_pressed()[0]:
        line.click(*py.mouse.get_pos(), 1)
    if py.mouse.get_pressed()[2]:
         line.click(*py.mouse.get_pos(), 2)
    py.display.update()
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    clock.tick(FPS)