from .data_structure.quadtree import Quadtree
from .data_structure.boundary import Boundary
from .organism import Organism
from .food import Food
from random import randint, choice

FOOD_AMOUNT = 50
class Ecosystem:
    def __init__(self, window_size, organism_colors):
        self.organisms = Quadtree(Boundary(0, 0, window_size, window_size), 4)
        self.food = []
        self.organism_colors = organism_colors
        self.window_size = window_size
        self.generations = 0
        
        self.new_generation()
    
    def add_organism(self, organism):
        self.organisms.insert(organism)
        
    def remove_organism(self, organism):
        self.organisms.remove(organism)
    
    def get_organisms(self):
        return self.organisms.query_all_organisms()
    
    def generate_organisms(self, default_organism=None):
        for color in self.organism_colors:
            if default_organism:
                organism = default_organism.reproduce()
                organism.color = color
                organism.size = 1
            else:
                organism = Organism(color=color)
            
            organism.x = randint(0, self.window_size)
            organism.y = randint(0, self.window_size)

            self.add_organism(organism)
    
    def get_food(self):
        return self.food
    
    def add_food(self, food):
        self.food.append(food)
        
    def generate_food(self):
        for _ in range(FOOD_AMOUNT):
            x = randint(0, self.window_size)
            y = randint(0, self.window_size)
            size = choice([1, 1, 1, 1, 2, 2, 3])
            
            food = Food(size, x, y)

            self.add_food(food)
        
    def reproduce_all(self):
        print("Reproducing all organisms")
        for organism in self.get_organisms():
            if organism.size >= 2:
                new_organism = organism.reproduce()
                self.add_organism(new_organism)
                
    def get_total_initial_organisms(self):
        return len(self.organism_colors)
    
    def clear(self):
        self.clear_food()
        self.clear_organisms()
        
    def clear_food(self):
        self.food = []
        
    def clear_organisms(self):
        self.organisms = Quadtree(Boundary(0, 0, self.window_size, self.window_size), 4)
        
    def new_generation(self, default_organism=None):
        self.clear()
        self.generate_food()
        self.generate_organisms(default_organism)
        self.generations += 1
        
    def get_generations(self):
        return self.generations