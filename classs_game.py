import random

import pygame as py
class Circle:

    def __init__(self, w, r=20):
        self.w = w
        self.colour = (0, 200, 200)
        self.cord = [random.randint(10, 590), random.randint(-100, -10)]
        self.r = r

    def draw(self):
        self.cord[1] += 1
        py.draw.circle(self.w, self.colour, self.cord, self.r)
    def click(self,x, y):
        if abs(self.cord[0] - x) < 20 and abs(self.cord[1] - y) < 20:
            self.cord = [random.randint(10, 590), random.randint(-600, -10)]
    def end(self):
        if self.cord[1] > 600:
            return True
        else:
            return False