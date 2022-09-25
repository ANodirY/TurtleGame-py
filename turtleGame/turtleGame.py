import turtle
import time
import random

WIDHT, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'pink', 'purple','brown', 'cyan', 'maroon', 'lime', 'gold', 'aquamarine', 'chocolate', 'chartreuse']

def get_racer_number():
    racers = 0
    while True:
        racers = input('enter racers number(2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('input isnot numeric...try one more')
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print('number isnot in range 2 to 10!')

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
            
def create_turtles(colors):
    turtles = []
    spacingx = WIDHT // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDHT // 2+ (i +1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles     
 
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDHT, HEIGHT)
    screen.title("TurtleGame by A.Nodir")
    
racers = get_racer_number()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print('winner is: ', winner)
time.sleep(3)
'''racer = turtle.Turtle()
rand = random.randint(0, 10)
racer.speed(rand)'''
