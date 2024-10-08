from turtle  import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        #  self.high_score = 0
        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            with open("data.txt", mode="w") as data:
                data.write("0")
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        # self.write(f"Score: {self.score} ", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_Score_board()
        
    def update_Score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_Score_board()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
                
    def increase_score(self):
        self.score += 1
        # self.write(f"Score: {self.score} ", align="center", font=("Arial", 24, "normal"))
        self.update_Score_board()
    
    