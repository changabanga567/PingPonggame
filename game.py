import curses
from ball import Ball
from paddle import Paddle
import random

# Initialize curses
screen = curses.initscr()
curses.curs_set(0)
curses.cbreak()  # React to keys instantly
curses.noecho()  # Don't echo key presses
screen.keypad(True)  # Enable special keys
height, width = screen.getmaxyx()

# Define the border position
border_player = width // 4 - 2
border_bot = 3 * width // 4 + 2

# Create the Ball and Paddle objects
ball = Ball(screen, width//2, height//2, dx=1, dy=2)
paddle_player = Paddle(screen, width//4, height//2 - 5)  # Unchanged position
paddle_bot = Paddle(screen, 3*width//4, height//2 + 5)  # Unchanged position

# Set up the screen to not block for user input
screen.nodelay(True)

# Initialize scores
score_player = 0
score_bot = 0

try:
    while True:
        # Draw the Ball and Paddles
        ball.draw()
        paddle_player.draw()
        paddle_bot.draw()

        # Draw the scores
        screen.addstr(0, width//2 - 10, f"Player: {score_player}")
        screen.addstr(0, width//2 + 5, f"Bot: {score_bot}")

        # Draw the borders
        for i in range(height):
            screen.addch(i, border_player, '|')
            screen.addch(i, border_bot, '|')

        # Move the Ball
        ball.move()

        # Occasionally modify the direction of the ball mid-flight
        if random.random() < 0.01:  # 1% chance to change direction
            ball.bounce()

        # Check if the Ball hit the top or bottom of the screen
        if ball.y <= 0 or ball.y >= height-1:
            ball.dy *= -1  # Reverse vertical direction

        # Check if the Ball hit the player's Paddle
        if paddle_player.x <= ball.x <= paddle_player.x + paddle_player.length and \
           paddle_player.y <= ball.y <= paddle_player.y + paddle_player.length:
            ball.dx *= -1  # Reverse horizontal direction

        # Check if the Ball hit the bot's Paddle
        if paddle_bot.x <= ball.x <= paddle_bot.x + paddle_bot.length and \
           paddle_bot.y <= ball.y <= paddle_bot.y + paddle_bot.length:
            ball.dx *= -1  # Reverse horizontal direction

        # Check if the Ball has passed a player's paddle
        if ball.x < border_player:
            ball = Ball(screen, width//2, height//2)  # Reset the ball to the center
            score_bot += 1  # Increment the bot's score
        elif ball.x > border_bot:
            ball = Ball(screen, width//2, height//2)  # Reset the ball to the center
            score_player += 1  # Increment the player's score

        # Get the user's input
        key = screen.getch()

        # Move the player's Paddle based on the user's input
        if key == curses.KEY_UP:
            paddle_player.move_up()
        elif key == curses.KEY_DOWN:
            paddle_player.move_down()

        # Move the bot's Paddle based on the ball's position
        if ball.y < paddle_bot.y:
            paddle_bot.move_up()
        elif ball.y > paddle_bot.y:
            paddle_bot.move_down()

        # Refresh the screen
        screen.refresh()

        # Clear the screen
        screen.clear()

        # Delay to slow down the game
        curses.napms(50)

except KeyboardInterrupt:
    # Clean up curses
    curses.endwin()
    print("Game exited")
