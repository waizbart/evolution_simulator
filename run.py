from organism import Organism
from random import randint, choice
from ecosystem import Ecosystem
from utils import is_circle_colliding, is_circle_inside_circle, generate_food
import pygame

FOOD_SIZE = 2
FOOD_AMOUNT = 50
ORGANISM_AMOUNT = 100
WINDOW_SIZE = 800
VELOCITY = 10

ecosystem = Ecosystem()

colors = ["red", "blue", "yellow", "purple", "orange", "green", "pink", "brown", "gray", "cyan"]

for i in range(ORGANISM_AMOUNT):
    color = choice(colors)
    size = 1
    speed = randint(1, 10)
    
    organism = Organism(color, size, speed)
    
    ecosystem.add_organism(organism)
    
pygame.init()
pygame.display.set_caption("Ecosystem")
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# posição inicial dos organismos
for organism in ecosystem.get_organisms():
    organism.x = randint(0, WINDOW_SIZE)
    organism.y = randint(0, WINDOW_SIZE)
    
# criação de comida aleatória
food = generate_food(FOOD_AMOUNT, WINDOW_SIZE, WINDOW_SIZE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    
    # desenha a comida
    for f in food:
        pygame.draw.circle(screen, pygame.Color("white"), f, FOOD_SIZE)
    
    # desenha os organismos
    for organism in ecosystem.get_organisms():
        new_x, new_y = organism.move(WINDOW_SIZE, WINDOW_SIZE)
        pygame.draw.circle(screen, pygame.Color(organism.color), (organism.x, organism.y), organism.size)
        if organism.size > 1:
            pygame.draw.circle(screen, pygame.Color("white"), (organism.x, organism.y), organism.size, 1)
            
    # colisão dos organismos com a comida
    for organism in ecosystem.get_organisms():
        for f in food:
            if is_circle_colliding((organism.x, organism.y, organism.size), (f[0], f[1], FOOD_SIZE)):
                food.remove(f)
                new_size = organism.size + FOOD_SIZE
                organism.size = new_size
                
    # colisão dos organismos com os outros organismos
    for organism in ecosystem.get_organisms():
        for other_organism in ecosystem.get_organisms():
            if organism != other_organism:
                if is_circle_inside_circle((organism.x, organism.y, organism.size), (other_organism.x, other_organism.y, other_organism.size)):
                    if organism.size > other_organism.size:
                        ecosystem.remove_organism(other_organism)
                        organism.size += other_organism.size
                    else:
                        ecosystem.remove_organism(organism)
                        other_organism.size += organism.size
            
    pygame.display.flip()
    pygame.time.Clock().tick(VELOCITY)
    
    if len(ecosystem.get_organisms()) == 1:
        running = False
