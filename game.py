import curses
from ball import Ball
from paddle import Paddle
import random

# start up curses
screen = curses.initscr()
curses.curs_set(0)  # Hide the cursor
curses.cbreak()  # React to keys instantly
curses.noecho()  # Don't echo key presses
screen.keypad(True)  # Enable special keys
height, width = screen.getmaxyx()  # Get the size of the window

#border position
border_player = width // 4 - 2
border_bot = 3 * width // 4 + 2

# Create the Ball and Paddle 
ball = Ball(screen, width//2, height//2, dx=2, dy=random.choice([-2, 4])) # Use dx and dy to control the speed of the ball
paddle_player = Paddle(screen, width//4, height//2 - 5)  # Position the player paddle
paddle_bot = Paddle(screen, 3*width//4, height//2 + 5)  # Position the bot paddle

# Set up the screen to not block for user input
screen.nodelay(True)

# starting scores
score_player = 0
score_bot = 0

# Winning score
winning_score = 5

try:
    while True:
        # Draw the Ball and Paddles
        ball.draw()
        paddle_player.draw()
        paddle_bot.draw()

        # Draw the scores
        screen.addstr(0, width//2 - 10, f"Player: {score_player}")
        screen.addstr(0, width//2 + 5, f"Bot: {score_bot}")

        # Check if the game is over
        if score_player >= winning_score:
            screen.addstr(height//2, width//2 - 7, "Player wins!")
            screen.refresh()
            curses.napms(2000)
            break
        elif score_bot >= winning_score:
            screen.addstr(height//2, width//2 - 6, "Bot wins!")
            screen.refresh()
            curses.napms(2000)
            break

        # Draw the borders
        for i in range(height):
            screen.addch(i, border_player, '|')
            screen.addch(i, border_bot, '|')

        # Move the Ball
        ball.move()

        # Check if the Ball hit the top or bottom of the screen
        if ball.y <= 0 or ball.y >= height-1:
            ball.dy *= -1  # Reverse vertical direction

        # Check if the Ball hit the player's Paddle
        if paddle_player.x == ball.x and paddle_player.y <= ball.y <= paddle_player.y + paddle_player.length:
            ball.dx *= -1  # Reverse horizontal direction
            ball.dy = random.choice([-1, 1])  # Random new vertical direction

        # Check if the Ball hit the bot's Paddle
        if paddle_bot.x == ball.x and paddle_bot.y <= ball.y <= paddle_bot.y + paddle_bot.length:
            ball.dx *= -1  # Reverse horizontal direction
            ball.dy = random.choice([-1, 1])  # Random new vertical direction

        # Check if the Ball has passed a player's paddle
        if ball.x < border_player:
            # Reset the ball to the center with random vertical direction
            ball = Ball(screen, width//2, height//2, dx=1, dy=random.choice([-1, 1]))  
            score_bot += 1  # Increment the bot's score
        elif ball.x > border_bot:
            # Reset the ball to the center with random vertical direction
            ball = Ball(screen, width//2, height//2, dx=1, dy=random.choice([-1, 1]))  
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

# lets the game exit with input (i use cctrl +C)
except KeyboardInterrupt:
    # Clean up curses
    curses.endwin()
    print("Game exited")
