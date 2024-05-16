from data_structure.quadtree import Quadtree
from data_structure.boundary import Boundary

class Ecosystem:
    def __init__(self, window_size):
        self.organisms = Quadtree(Boundary(0, 0, window_size, window_size), 4)
        self.food = []
    
    def add_organism(self, organism):
        self.organisms.insert(organism)
        
    def remove_organism(self, organism):
        self.organisms.remove(organism)
    
    def get_organisms(self):
        return self.organisms.query_all_organisms()
    
    def get_food(self):
        return self.food
    
    def add_food(self, food):
        self.food.append(food)