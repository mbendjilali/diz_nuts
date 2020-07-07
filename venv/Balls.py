"""
Platformer Game
"""
import arcade
import random

# Gravity & BOUNCYNESS
GRAVITY = 1
BOUNCYNESS = 1

SCREEN_TITLE = "Platform"

# How big are our image tiles ?
SPRITE_IMAGE_SIZE=128

# Scale sprites up or down
SPRITE_SCALING_TILES = 0.5

# Scaled sprite size for tiles
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_TILES)

# Size of grid to show on screen, in number of tiles
SCREEN_GRID_WIDTH = 10
SCREEN_GRID_HEIGHT = 10

# Size of screen to show, in pixels
SCREEN_WIDTH = SPRITE_SIZE * SCREEN_GRID_WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * SCREEN_GRID_HEIGHT

class Ball:
    """ Class to keep track of a ball's location and vector"""

    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size     = SPRITE_SIZE/10
        self.color    = None

def make_ball(x, y):
    """ Function to make a ball"""

    ball = Ball()

    """ Give position to the ball"""
    ball.x = x
    ball.y = y

    """ Give an angle to the ball"""
    ball.change_x = random.random()*2 -1

    """ Give a color to the ball"""
    ball.color = arcade.color.BLACK

    return ball

class myGame(arcade.Window):
    """ Main Window """

    def __init__(self):
        """ Create the variables """

        # Init the parent class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.ball_list = []
        ball = make_ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.wall_list = None
        self.ball_list.append(ball)

        arcade.set_background_color(arcade.csscolor.WHITE_SMOKE)

    def setup(self):
        """ Set up everything with the game """
        # Create the Sprite lists
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, SCREEN_WIDTH, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING_TILES)
            wall.center_x = x + 32
            wall.center_y = 32
            self.wall_list.append(wall)
        for y in range(0, SCREEN_HEIGHT, 64):
            wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING_TILES)
            wall.center_x = 32
            wall.center_y = y + 32 + 64
            self.wall_list.append(wall)
            wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING_TILES)
            wall.center_x = 32 + SCREEN_WIDTH - 64
            wall.center_y = y + 32 + 64
            self.wall_list.append(wall)

    def on_draw(self):
        """ Render  the screen."""

        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()

        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)

    def on_update(self, delta_time):
        """ Movement and game logic"""
        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.x < ball.size:
                ball.change_x *= -BOUNCYNESS

            if ball.y < ball.size:
                if ball.change_y < GRAVITY * 0.1:
                    ball.change_y *= -BOUNCYNESS
                else :
                    ball.change_y *= -BOUNCYNESS/2

            if ball.x > SCREEN_WIDTH - ball.size:
                ball.change_x *= -BOUNCYNESS

            if ball.y > SCREEN_HEIGHT - ball.size:
                ball.change_y *= -BOUNCYNESS

            ball.change_y -= GRAVITY


    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        ball = make_ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.ball_list.append(ball)

def main():
    """Main Method"""

    window=myGame()
    window.setup()

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(window.on_update, 100)

    arcade.run()


if __name__ == '__main__':
    main()