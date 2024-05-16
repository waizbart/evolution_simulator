from random import randint
from data_structure.boundary import Boundary
import math    
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
    
    def get_nearby_organisms(self, quadtree, distance):
        nearby_organisms = []

        # Definir uma área de consulta com base na distância especificada
        query_boundary = Boundary(self.x - distance, self.y - distance, 2 * distance, 2 * distance)

        # Realizar consulta na Quadtree para obter organismos próximos
        nearby_organisms = quadtree.query_range(query_boundary)

        # Filtrar organismos para aqueles dentro da distância especificada
        nearby_organisms = [org for org in nearby_organisms if self.distance_to(org) <= distance]

        return nearby_organisms

    def distance_to(self, other_obj):
        # Calcular a distância euclidiana entre este organismo e outro organismo
        return math.sqrt((self.x - other_obj.x)**2 + (self.y - other_obj.y)**2)
    
    def get_nearby_food(self, ecosystem, distance):
        nearby_food = []

        # Filtrar alimentos para aqueles dentro da distância especificada
        nearby_food = [food for food in ecosystem.get_food() if self.distance_to(food) <= distance]

        return nearby_food