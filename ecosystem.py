class Ecosystem:
    def __init__(self):
        self.organisms = []
        self.food = []
    
    def add_organism(self, organism):
        self.organisms.append(organism)
        
    def remove_organism(self, organism):
        self.organisms.remove(organism)
        
    def get_organism(self, index):
        return self.organisms[index]
    
    def get_organisms(self):
        return self.organisms
    
    def get_food(self):
        return self.food
    
    def add_food(self, food):
        self.food.append(food)