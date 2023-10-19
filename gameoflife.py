import turtle
import random
import time

GRID_SIZE = 50
CELL_SIZE = 10
ON = 1
OFF = 0
DELAY = 0.1

running = False


screen = turtle.Screen()
screen.setup(GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE + 20)
screen.bgcolor("purple")
screen.title("Conway's Game of Life with Turtle")


grid = [[OFF for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def draw_grid():
    turtle.clear()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == ON:
                draw_cell(i, j, "green")
            else:
                draw_cell(i, j, "purple")

def draw_caption():
    turtle.up()
    turtle.goto(-GRID_SIZE * CELL_SIZE / 2, GRID_SIZE * CELL_SIZE / 2 + 5)
    turtle.down()
    turtle.write("Simulate: s | Pause: p", align="left", font=("Arial", 10, "normal"))

def draw_cell(x, y, color):
    turtle.up()
    turtle.goto(x * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2, y * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(CELL_SIZE)
        turtle.left(90)
    turtle.end_fill()
def draw_caption():
    caption_turtle = turtle.Turtle()
    caption_turtle.hideturtle()
    caption_turtle.penup()
    caption_turtle.color("white")
    caption_turtle.goto(-GRID_SIZE * CELL_SIZE / 2 + 10, GRID_SIZE * CELL_SIZE / 2 - 20)  
    caption_turtle.write("simulate -s , pause- p", font=("Arial", 12, "normal"))

def toggle_cell(x, y):
    grid[x][y] = ON if grid[x][y] == OFF else OFF
    draw_grid()
    draw_caption()

def update():
    global grid, running
    if not running:
        return
    new_grid = [[OFF] * GRID_SIZE for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            total = sum([grid[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2) if (0 <= x < GRID_SIZE) and (0 <= y < GRID_SIZE)]) - grid[i][j]
            if grid[i][j] == ON:
                if total in [2, 3]:
                    new_grid[i][j] = ON
            elif total == 3:
                new_grid[i][j] = ON
    grid = new_grid
    draw_grid()
    draw_caption()
    screen.ontimer(update, int(DELAY * 1000))

def start_game():
    global running
    running = True
    update()

def pause_game():
    global running
    running = False

def main():
    turtle.speed(0)
    turtle.hideturtle()
    screen.tracer(0)
    draw_grid()
    draw_caption()
    screen.onclick(lambda x, y: toggle_cell(int((x + GRID_SIZE * CELL_SIZE / 2) // CELL_SIZE), int((y + GRID_SIZE * CELL_SIZE / 2) // CELL_SIZE)))
    screen.onkey(start_game, "s")
    screen.onkey(pause_game, "p")
    screen.listen()
    turtle.done()

if __name__ == "__main__":
    main()
