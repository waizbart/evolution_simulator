from random import randint

class Organism:
    def __init__(self, color, size, speed):
        self.color = color
        self.size = size
        self.speed = speed
        self.x = 0
        self.y = 0
    
    def move(self, max_x, max_y):
        new_x = self.x + randint(-self.speed, self.speed)
        new_y = self.y + randint(-self.speed, self.speed)
        
        organism_size = self.size
        
        if new_x < organism_size:
            new_x = organism_size
        elif new_x > max_x - organism_size:
            new_x = max_x - organism_size
        
        if new_y < organism_size:
            new_y = organism_size
        elif new_y > max_y - organism_size:
            new_y = max_y - organism_size
        
        self.x = new_x
        self.y = new_y
        
        return self.x, self.y
    
class Organism:
    def __init__(self, color, size, speed):
        self.color = color
        self.size = size
        self.speed = speed
        self.x = None
        self.y = None

    def move(self, max_x, max_y):
        self.x += randint(-self.speed, self.speed)
        self.y += randint(-self.speed, self.speed)
        
        self.x = max(self.size, min(self.x, max_x - self.size))
        self.y = max(self.size, min(self.y, max_y - self.size))
        
        return self.x, self.y