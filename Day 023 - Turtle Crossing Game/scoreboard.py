from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.goto(-250, 250)  # Position the turtle at the center of the top of the screen
        self.show_text()

    def increase_level(self):
        self.level += 1
        self.show_text()

    def show_text(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)