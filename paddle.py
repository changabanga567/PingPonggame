class Paddle:
    def __init__(self, screen, x, y, length=5):
        self.screen = screen
        self.x = x
        self.y = y
        self.length = length

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def draw(self):
        for i in range(self.length):
            self.screen.addch(self.y + i, self.x, '|')
