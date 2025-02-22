import pygame as py
BLACK = (0, ) * 3
GREY = (100, ) * 3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 200)
class Pole:
    def __init__(self, w, shirina, long,size):
        self.shirina = shirina
        self.long = long
        self.colour = GREY
        self.w = w
        self.size = size
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.board[0][1]=1
    def draw(self):
        py.draw.line(self.w, GREY, (0, self.size), (self.shirina, self.size))
        py.draw.line(self.w, GREY, (0, self.size * 2), (self.shirina, self.size * 2))
        py.draw.line(self.w, GREY, (self.size, 0), (self.size, self.long))
        py.draw.line(self.w, GREY, (self.size * 2, 0), (self.size * 2, self.long))
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 1:
                    pass
                if self.board[x][y] == 2:
                    pass

    def click(self, x, y, player):
        x = x//self.size
        y = y // self.size
        self.board[y][x] = player
        print(self.board)

class Circle:
    def __init__(self, w, x, y, r):
        self.w = w
        self.r = r
        self.x = x
        self.y = y
        self.r = r
        self.colour = RED



