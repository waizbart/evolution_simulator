from organism import Organism
from random import randint, choice
from ecosystem import Ecosystem
from utils import generate_food
from display import Display

FOOD_AMOUNT = 50
WINDOW_SIZE = 800
VELOCITY = 50

ecosystem = Ecosystem(WINDOW_SIZE)
generate_food(ecosystem, FOOD_AMOUNT, WINDOW_SIZE, WINDOW_SIZE)

organism_colors = ["red", "blue", "yellow", "purple", "orange", "green", "pink", "brown", "gray", "cyan", "fuchsia", "lime", "maroon", "navy", "olive", "teal", "aqua", "silver"]

INITIAL_ORGANISMS_TOTAL = len(organism_colors)

for color in organism_colors:
    organism = Organism(color)
    
    organism.x = randint(0, WINDOW_SIZE)
    organism.y = randint(0, WINDOW_SIZE)

    ecosystem.add_organism(organism)

display = Display(WINDOW_SIZE)

while display.is_running:
    display.update(ecosystem, INITIAL_ORGANISMS_TOTAL)