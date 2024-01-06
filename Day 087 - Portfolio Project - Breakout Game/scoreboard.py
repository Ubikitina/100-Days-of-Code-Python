from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_lives = 3
        self.color("white")
        self.hideturtle()
        self.goto(290, 150)  # Position the turtle at the top of the screen
        self.show_text()

    def decrease_lives(self):
        self.score_lives -= 1
        self.show_text()

    def show_text(self):
        self.clear()
        self.write(f"Lives: {self.score_lives}", align=ALIGMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align=ALIGMENT, font=FONT)

    def you_win(self):
        self.goto(0, 0)
        self.write("CONGRATS! You win!", align=ALIGMENT, font=FONT)