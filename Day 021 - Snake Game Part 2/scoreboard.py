from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)  # Position the turtle at the center of the top of the screen
        self.show_text()


    def increase_score(self):
        self.score += 1
        self.show_text()

    def show_text(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align=ALIGMENT, font=FONT)