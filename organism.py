from data_structure.boundary import Boundary
from random import randint
import math    
class Organism:
    def __init__(self, color, size, speed):
        self.color = color
        self.size = size
        self.speed = speed
        self.x = None
        self.y = None
        self.vision = 100

    def move(self, ecosystem, max_x, max_y):
        vision = self.vision * self.size
        
        nearby_food = self.get_nearby_food(ecosystem, vision)
        nearby_organisms = self.get_nearby_organisms(ecosystem.organisms, vision)
        
        if len(nearby_food) == 0 and len(nearby_organisms) == 0:
            angle = randint(0, 360)
        else:
            best_goal = None
            
            for obj in [*nearby_food, *nearby_organisms]:
                if best_goal is None:
                    best_goal = obj
                    continue
                if self.distance_to(obj) < self.distance_to(best_goal):
                    if isinstance(obj, Organism):
                        if self.size > obj.size:
                            if obj.size > best_goal.size:
                                best_goal = obj
                    else:
                        if obj.size > best_goal.size:
                            best_goal = obj
                        
            angle = self.angle_to(best_goal)
        
        distance = self.speed
        new_x = self.x + distance * math.cos(math.radians(angle))
        new_y = self.y + distance * math.sin(math.radians(angle))
        self.x = max(self.size, min(new_x, max_x - self.size))
        self.y = max(self.size, min(new_y, max_y - self.size))
    
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