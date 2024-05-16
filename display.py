import pygame
from utils import is_circle_colliding, is_circle_inside_circle

FOOD_SIZE = 2
VELOCITY = 50

class Display:
    def __init__(self, window_size):
        pygame.init()
        pygame.display.set_caption("Ecosystem")
        self._screen = pygame.display.set_mode((window_size, window_size))
        self._running = True
        self._clock = pygame.time.Clock().tick(VELOCITY)
        self._window_size = window_size

    def update(self, ecosystem):
        organisms = ecosystem.get_organisms()
        food = ecosystem.get_food()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
    
        self._screen.fill((0, 0, 0))
        
        self.draw_organisms(organisms)
        self.draw_food(food)
        self.verify_food_collision(food, organisms)
        self.verify_organisms_collision(ecosystem)
        
        pygame.display.flip()
        pygame.time.Clock().tick(VELOCITY)
        
        if len(ecosystem.get_organisms()) == 1:
            self.is_running = False
        
    def draw_food(self, food):
        for f in food:
            pygame.draw.circle(self._screen, pygame.Color("white"), f, FOOD_SIZE)
            
    def draw_organisms(self, organisms):
        for organism in organisms:
            organism.move(self._window_size, self._window_size)
            pygame.draw.circle(self._screen, pygame.Color(organism.color), (organism.x, organism.y), organism.size)
            if organism.size > 1:
                pygame.draw.circle(self._screen, pygame.Color("white"), (organism.x, organism.y), organism.size, 1)
        
    def verify_food_collision(self, food, organisms):
        for organism in organisms:
            for f in food:
                if is_circle_colliding((organism.x, organism.y, organism.size), (f[0], f[1], FOOD_SIZE)):
                    food.remove(f)
                    new_size = organism.size + FOOD_SIZE
                    organism.size = new_size
                    
    def verify_organisms_collision(self, ecosystem):
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
    
    def is_running(self):
        return self._running
    
    def close(self):
        pygame.quit()