"""
Tec de Monterrey

Proyecto: Snake
Materia: Herramientas computacionales: El arte de la progrmación
Autores: Yerik Escobar Asprón y Diego Lemus Mejía

Descripcion:
Videojuego Snake desarrollado con Python y Turtle.
Basado en el codigo original de Grant Jenks.

Modificaciones:
- Movimiento aleatorio de comida.
- Colores aleatorios distintos para serpiente y comida."""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
food_steps = 0

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    #Modificación
    global food_steps

    food_steps += 1

    if food_steps % 5 == 0:
        directions =[
            vector(10, 0),
            vector(-10, 0),
            vector(0, 10),
            vector(0, -10)
        ]
     
        direction = directions [randrange(4)]
        nueva_comida = food.copy()
        nueva_comida.move(direction)

        if inside(nueva_comida) and nueva_comida not in snake:
            food.x = nueva_comida.x
            food.y = nueva_comida.y

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
