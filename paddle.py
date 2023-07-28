class Paddle:
    def __init__(self, screen, x, y, length=5):
        self.screen = screen
        self.x = x
        self.y = y
        self.length = length

    def move_up(self):
        if self.y > 0:  # Only move up if it's not at the top of the screen
            self.y -= 1

    def move_down(self):
        h, w = self.screen.getmaxyx()
        if self.y < h - self.length - 1:  # Only move down if it's not at the bottom of the screen
            self.y += 1

    def draw(self):
        h, w = self.screen.getmaxyx()
        for i in range(self.length):
            if 0 <= self.y + i < h and 0 <= self.x < w:  # Make sure we are not drawing outside of the screen
                self.screen.addch(self.y + i, self.x, '|')
