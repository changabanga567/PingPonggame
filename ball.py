import curses
import random

class Ball:
    def __init__(self, screen, x, y, dx=2, dy=2):
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        if 0 < self.x + self.dx < curses.COLS-1:  # Check horizontal boundaries
            self.x += self.dx
        if 0 < self.y + self.dy < curses.LINES-1:  # Check vertical boundaries
            self.y += self.dy

    def bounce(self):
        self.dx = random.choice([-2, 2])  # Randomly pick either -2 or 2
        self.dy = random.choice([-2, 2])  # Randomly pick either -2 or 2

    def draw(self):
        self.screen.addch(self.y, self.x, 'O')
