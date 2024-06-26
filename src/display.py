import pygame
from .utils import is_circle_colliding, is_circle_inside_circle

FPS = 20

class Display:
    def __init__(self, window_size):
        pygame.init()
        pygame.display.set_caption("Ecosystem")
        self._screen = pygame.display.set_mode((window_size, window_size))
        self._running = True
        self._window_size = window_size

    def update(self, ecosystem):
        organisms = ecosystem.get_organisms()
        food = ecosystem.get_food()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
    
        self._screen.fill((0, 0, 0))
        
        self.draw_organisms(ecosystem)
        self.draw_food(food)
        self.verify_food_collision(food, organisms)
        self.verify_organisms_collision(ecosystem)
        self.draw_generation(ecosystem.generations)
        
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
            
        organisms_colors_in_ecosystem = set([organism.color for organism in ecosystem.get_organisms()])
        
        # Se só existe uma cor de organismo no ecossistema então cria uma nova geração utilizando o organismo vencedor como base
        if len(organisms_colors_in_ecosystem) == 1:
            organism = ecosystem.get_organisms()[0]
            print("All organisms are the same color")
            print("Winner: ", organism)
            print("New generation: ", ecosystem.generations)
            ecosystem.new_generation(organism)
            
            
    def draw_food(self, food):
        for f in food:
            pygame.draw.circle(self._screen, pygame.Color("white"), (f.x, f.y), f.size)
            
    def draw_organisms(self, ecosystem):
        organisms = ecosystem.get_organisms()
        for organism in organisms:
            organism.move(ecosystem, self._window_size, self._window_size)
            pygame.draw.circle(self._screen, pygame.Color(organism.color), (organism.x, organism.y), organism.size)
            if organism.size > 1:
                pygame.draw.circle(self._screen, pygame.Color("white"), (organism.x, organism.y), organism.size, 1)
        
    def verify_food_collision(self, food, organisms):
        for organism in organisms:
            for f in food:
                if is_circle_colliding((organism.x, organism.y, organism.size), (f.x, f.y, f.size)):
                    food.remove(f)
                    new_size = organism.size + f.size
                    organism.size = new_size
                    
    def verify_organisms_collision(self, ecosystem):
        for organism in ecosystem.get_organisms():
            for other_organism in ecosystem.get_organisms():
                if organism != other_organism and organism.color != other_organism.color:
                    if is_circle_inside_circle((organism.x, organism.y, organism.size), (other_organism.x, other_organism.y, other_organism.size)):
                        if organism.size > other_organism.size:
                            ecosystem.remove_organism(other_organism)
                            organism.size += other_organism.size
                        else:
                            ecosystem.remove_organism(organism)
                            other_organism.size += organism.size
                            
    def draw_generation(self, generation):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Generation: {generation}", True, pygame.Color("white"))
        self._screen.blit(text, (10, 10))
    
    def is_running(self):
        return self._running
    
    def close(self):
        pygame.quit()