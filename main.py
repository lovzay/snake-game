from tkinter import *
import random

GAME_WIDTH: int = 900
GAME_HEIGHT: int = 900
SPEED = 80
SPACE_SIZE: int = 60
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


    class Snake:

    class Food:


    def next_turn(snake, food):
        pass

    def change_direction(new_direction):
        pass

    def check_collision(snake):
        pass
    def game_over():
        pass

window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window.mainloop()