from organism import Organism
from random import randint, choice
from ecosystem import Ecosystem
from utils import generate_food
from display import Display

FOOD_AMOUNT = 50
ORGANISM_AMOUNT = 100
WINDOW_SIZE = 800
VELOCITY = 50

ecosystem = Ecosystem(WINDOW_SIZE)
generate_food(ecosystem, FOOD_AMOUNT, WINDOW_SIZE, WINDOW_SIZE)

colors = ["red", "blue", "yellow", "purple", "orange", "green", "pink", "brown", "gray", "cyan"]

for i in range(ORGANISM_AMOUNT):
    color = choice(colors)
    size = 1
    speed = randint(1, 10)
    organism = Organism(color, size, speed)
    
    organism.x = randint(0, WINDOW_SIZE)
    organism.y = randint(0, WINDOW_SIZE)

    ecosystem.add_organism(organism)

display = Display(WINDOW_SIZE)

while display.is_running:
    display.update(ecosystem)