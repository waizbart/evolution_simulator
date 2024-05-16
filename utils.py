import math
from random import randint

def is_circle_colliding(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    return distance <= r1 + r2

def is_circle_inside_circle(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    return distance + r1 <= r2 or distance + r2 <= r1

def generate_food(ecosystem, amount, width, height):
    for _ in range(amount):
        x = randint(0, width)
        y = randint(0, height)
        
        ecosystem.add_food((x, y))