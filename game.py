import curses
from ball import Ball
from paddle import Paddle

# Initialize curses
screen = curses.initscr()
curses.curs_set(0)
curses.cbreak()  # React to keys instantly
curses.noecho()  # Don't echo key presses
screen.keypad(True)  # Enable special keys
height, width = screen.getmaxyx()

# Create the Ball and Paddle objects
ball = Ball(screen, width//2, height//2)
paddle = Paddle(screen, width//2, height//2)

try:
    while True:
        # Draw the Ball and Paddle
        ball.draw()
        paddle.draw()

        # Move the Ball
        ball.move()

        # Check if the Ball hit the top or bottom of the screen
        if ball.y <= 0 or ball.y >= height-1:
            ball.bounce()

        # Check if the Ball hit the Paddle
        if ball.x == paddle.x and paddle.y <= ball.y <= paddle.y + paddle.length:
            ball.bounce()

        # Get the user's input
        key = screen.getch()

        # Move the Paddle based on the user's input
        if key == curses.KEY_UP:
            paddle.move_up()
        elif key == curses.KEY_DOWN:
            paddle.move_down()

        # Refresh the screen
        screen.refresh()

        # Clear the screen
        screen.clear()

except KeyboardInterrupt:
    # Clean up curses
    curses.endwin()
    print("Game exited")
