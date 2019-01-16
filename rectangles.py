#Tyler Strouth & Kaitlin Sine
#Create a class for making rectangular objects
#for the game breakout

#constants for tkinter window
HEIGHT = 500
WIDTH  = 400
class blocks:
    #CI: class that will create the blocks on top of the screen
    #    we need a canvas and coordinates and color for each block
    def __init__(self, canvas):
        self.canvas   = canvas
        self.x_coor_1 = 0
        self.y_coor_1 = 0
        self.x_coor_2 = 0
        self.y_coor_2 = 0
        self.color    = None

    # pre: none
    #post: draws the blocks on the canvas
    def draw_blocks(self):
        blocks = self.canvas.create_rectangle(self.x_coor_1, self.y_coor_1,
                                              self.x_coor_2, self.y_coor_2,
                                              fill = self.color)
        return blocks
    

    
class paddle(blocks):

    #CI: this is the class for the paddle that will bounce the box back and
    #    forth
    #    we need coordinates for the paddle and an event handler to move the
    #    paddle around the screen
    def __init__(self, canvas):
        super().__init__(canvas)
        self.velocity = 0
        self.canvas   = canvas
        self.x_coor_1 = 0
        self.y_coor_1 = 0
        self.x_coor_2 = 0
        self.y_coor_2 = 0
        self.color    = None
        

    # pre: none
    #post: draws the paddle at desired point in the canvas
    def draw_paddle(self):
        paddle = self.canvas.create_rectangle(self.x_coor_1, self.y_coor_1,
                                              self.x_coor_2, self.y_coor_2,
                                              fill = self.color)
        return paddle

    # pre: needs an event like a keyboard press
    #post: moves the paddle accordinly
    def move_paddle(self, event):
        if event.keysym == 'Left' and self.x_coor_1 > 0:
            self.x_coor_1 -= self.velocity
            self.x_coor_2 -= self.velocity
        elif event.keysym == 'Right' and self.x_coor_2 < WIDTH:
            self.x_coor_1 += self.velocity
            self.x_coor_2 += self.velocity

class box(blocks):
    #CI: this the class for the box that will bouncing around the screen &
    #    collides with the blocks
    #    we need coordinates and velocity of the box and a method to determine
    #    if the box collides with the blocks
    def __init__(self, canvas):
        super().__init__(canvas)
        self.x_velocity = 0
        self.y_velocity = 0
        self.canvas     = canvas
        self.x_coor_1   = 0
        self.y_coor_1   = 0
        self.diameter   = 0
        self.color      = None

    # Pre: None
    #Post: Begins the movement of the ball
    def move_box(self):
        self.x_coor_1 += self.x_velocity
        self.y_coor_1 -= self.y_velocity
        if ((self.x_coor_1 == 0) or (self.x_coor_1 + self.diameter >= WIDTH)):
            self.x_velocity *= -1
        if ((self.y_coor_1 <= 0) or (self.y_coor_1 >= HEIGHT)):
            self.y_velocity *= -1
            


    # pre: None
    #post: draws a square box with a specified diameter
    #      sometimes referred to as euclidian distance
    def draw_box(self):
        box = self.canvas.create_rectangle(self.x_coor_1, self.y_coor_1,
                                           self.x_coor_1 + self.diameter,
                                           self.y_coor_1 + self.diameter,
                                           fill = self.color)
    # pre: needs the x1, x2, y1, y2, of a rectangle
    #post: determines if a collision happens between the rectangle and the box
    def check_collision(self, object_x1, object_x2, object_y1, object_y2):
        collision = False
        if (((object_x1 <= self.x_coor_1 <= object_x2) 
            or (object_x1 <= self.x_coor_1 + self.diameter <= object_x2))
            and ((object_y1 == self.y_coor_1 + self.diameter) or
            (object_y2 == self.y_coor_1))):
            collision = True
        return collision
    

        

    
