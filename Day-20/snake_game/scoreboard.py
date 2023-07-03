from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape('classic')
        self.penup()
        self.hideturtle()
        self.goto(-20, 280)
        self.color('white')
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)
        
    def reload(self):
        """function to reload and update the score"""
        self.clear()
        self.goto(-55, 280)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)     
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)  

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!\n  Score: {self.score}", True, align=ALIGNMENT, font=("Courier", 25, "normal"))