from data_structure.boundary import Boundary
from random import randint, random, uniform
import math    
class Organism:
    def __init__(
        self, 
        color, 
        size=None, 
        speed=None, 
        hunger=None, 
        fear=None, 
        aggression=None,
        randomness=None,
    ):
        self.color = color
        self.size = size if size is not None else 1
        self.speed = speed if speed is not None else randint(1, 10)
        self.x = None
        self.y = None
        self.vision = 100
        self.hunger = hunger if hunger is not None else random()
        self.fear = fear if fear is not None else random()
        self.aggression = aggression if aggression is not None else random()
        self.randomness = randomness if randomness is not None else random()

    def move(self, ecosystem, max_x, max_y):
        angle = self.get_angle(ecosystem)
        distance = self.speed
        new_x = self.x + distance * math.cos(math.radians(angle))
        new_y = self.y + distance * math.sin(math.radians(angle))
        self.x = max(self.size, min(new_x, max_x - self.size))
        self.y = max(self.size, min(new_y, max_y - self.size))
        
    def get_angle(self, ecosystem):
        vision = self.vision * self.size
        
        nearby_food = self.get_nearby_food(ecosystem, vision)
        nearby_organisms = self.get_nearby_organisms(ecosystem.organisms, vision)
        
        best_goal = None
        best_score = float('-inf')
        
        for food in nearby_food:
            distance = self.distance_to(food)
            
            if distance == 0:
                distance = 1e-9
            
            score = self.hunger * (1 / distance)
            if score > best_score:
                best_score = score
                best_goal = food
        
        for organism in nearby_organisms:
            
            if organism == self or organism.color == self.color:
                continue
            
            distance = self.distance_to(organism)
            
            if distance == 0:
                distance = 1e-9
            
            if self.size > organism.size:
                score = self.aggression * (1 / distance)
            else:
                score = -self.fear * (1 / distance)
                
            if score > best_score:
                best_score = score
                best_goal = organism
        
        if best_goal is None or random() < self.randomness:
            angle = randint(0, 360)
        else:
            angle = self.angle_to(best_goal)
            
        return angle
    
    def get_nearby_organisms(self, quadtree, distance):
        nearby_organisms = []
        query_boundary = Boundary(self.x - distance, self.y - distance, 2 * distance, 2 * distance)
        nearby_organisms = quadtree.query_range(query_boundary)
        nearby_organisms = [org for org in nearby_organisms if self.distance_to(org) <= distance]
        return nearby_organisms

    def distance_to(self, other_obj):
        return math.sqrt((self.x - other_obj.x)**2 + (self.y - other_obj.y)**2)
    
    def angle_to(self, other_obj):
        return math.degrees(math.atan2(other_obj.y - self.y, other_obj.x - self.x))
    
    def get_nearby_food(self, ecosystem, distance):
        nearby_food = []
        nearby_food = [food for food in ecosystem.get_food() if self.distance_to(food) <= distance]
        return nearby_food
    
    def reproduce(self, mutation_rate=0.5):
        new_color = self.color
        new_size = self.size // 2
        self.size = self.size - new_size

        new_speed = self.speed * (1 + uniform(-mutation_rate, mutation_rate))
        new_hunger = self.hunger * (1 + uniform(-mutation_rate, mutation_rate))
        new_fear = self.fear * (1 + uniform(-mutation_rate, mutation_rate))
        new_aggression = self.aggression * (1 + uniform(-mutation_rate, mutation_rate))
        new_randomness = self.randomness * (1 + uniform(-mutation_rate, mutation_rate))
        
        offspring = Organism(
            color=new_color,
            size=new_size,
            speed=new_speed,
            hunger=new_hunger,
            fear=new_fear,
            aggression=new_aggression,
            randomness=new_randomness,
        )
        
        offspring.x = self.x
        offspring.y = self.y
        
        return offspring
    
    def __str__(self):
        return f"Organism(color={self.color}, size={self.size}, speed={self.speed}, hunger={self.hunger}, fear={self.fear}, aggression={self.aggression}, randomness={self.randomness})"