from turtle import Turtle
STARTTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    """class Snake, creating our snake class"""
    def __init__(self, new_turtle ='', snake_segments = [],):
        """
           Args:
               new_turtle: new instance of a turtle
               snake_segments: segment list of the snake
               pos: position of the snake
        """
        self.snake_segments = snake_segments
        self.new_turtle = new_turtle
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        """function to create our snake"""
        for i in range(0, 3):
            self.new_turtle = Turtle(shape="square")
            self.new_turtle.penup()
            self.new_turtle.color("white")
            # self.new_turtle.speed('fast')
            self.new_turtle.goto(STARTTING_POSITIONS[i][0], STARTTING_POSITIONS[i][1])

            self.snake_segments.append(self.new_turtle)
    def increase_position(self):
        """increase position list"""
        last_pos_x = self.snake_segments[-1].xcor() - 20
        last_pos_y = self.snake_segments[-1].ycor()
        STARTTING_POSITIONS.append((last_pos_x, last_pos_y))

    def create_more_snake(self):
        """create more snakes when food is eaten"""
        num_continue = len(self.snake_segments)
        for i in range(num_continue, len(STARTTING_POSITIONS) - 1):
            self.new_turtle = Turtle(shape="square")
            
            self.new_turtle.penup()
            self.new_turtle.color("white")
            self.new_turtle.hideturtle()
            self.new_turtle.goto(STARTTING_POSITIONS[i][0], STARTTING_POSITIONS[i][1])
            self.new_turtle.showturtle()

            self.snake_segments.append(self.new_turtle)

    def move(self):
        """function to move the snake forward"""
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
             new_x = self.snake_segments[seg_num - 1].xcor()
             new_y = self.snake_segments[seg_num - 1].ycor()
             self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(20)

    def check_collision(self, latest_pos):
        for i in range(1, len(STARTTING_POSITIONS) - 1):
            if latest_pos == self.snake_head.xcor():
                pass
            elif latest_pos == STARTTING_POSITIONS[i][0]:
                return True

    def direction(self, direct,param):
        """function to assert the direction"""
        """You can make it more compact tho by combining the or to 1, which is what is excluded"""
        """e.g  elif new_heading != 90 : self.snake_head(270)"""
        new_heading = self.snake_segments[0].heading()
        if new_heading == direct:
            self.snake_head.setheading(new_heading)

        elif (new_heading == 90 or new_heading == 270) and (direct == 0 and param == 'right'):
            """for right"""
            self.snake_head.setheading(direct)

        elif (new_heading == 0 or new_heading == 180) and (direct == 90 and param == 'up'):
            """for up"""
            self.snake_head.setheading(direct)

        elif (new_heading == 90 or new_heading == 270) and (direct == 180 and param == 'left'):
            """for left"""
            self.snake_head.setheading(direct)

        elif (new_heading == 0 or new_heading == 180) and (direct == 270 and param == 'down'):
            """for down"""
            self.snake_head.setheading(direct)
        
            
    def up(self):
        """change the direction of the snake"""
        self.direction(90, 'up')

    def down(self):
        """change the direction of the snake to down"""
        self.direction(270, 'down')

    def left(self):
        """change the direction of the snake to the left"""
        self.direction(180, 'left')

    def right(self):
        """change the direction of the snake to the right"""
        self.direction(0, 'right')