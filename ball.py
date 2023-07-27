class Ball:
    def __init__(self, screen, x, y, dx=1, dy=1):
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def bounce(self):
        self.dx *= -1
        self.dy *= -1

    def draw(self):
        self.screen.addch(self.y, self.x, 'O')
