from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 230)  # Position the turtle at the center of the top of the screen
        self.show_text()


    def increase_score_left(self):
        self.score_left += 1
        self.show_text()

    def increase_score_right(self):
        self.score_right += 1
        self.show_text()

    def show_text(self):
        self.clear()
        self.write(f"{self.score_left}      {self.score_right}", align=ALIGMENT, font=FONT)

    # Not needed right now
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER.", align=ALIGMENT, font=FONT)