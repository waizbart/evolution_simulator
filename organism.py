from random import randint
    
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