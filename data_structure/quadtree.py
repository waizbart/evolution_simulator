from .boundary import Boundary

class Quadtree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary  
        self.capacity = capacity  
        self.organisms = []       
        self.divided = False      
    
    def insert(self, organism):
        if not self.boundary.contains_point(organism.x, organism.y):
            return False  
        
        if len(self.organisms) < self.capacity:
            self.organisms.append(organism)
            return True
        else:
            if not self.divided:
                self.divide()  
                self.divided = True
            
            if self.northeast.insert(organism):
                return True
            elif self.northwest.insert(organism):
                return True
            elif self.southeast.insert(organism):
                return True
            elif self.southwest.insert(organism):
                return True
            else:
                return False
    
    def divide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.width
        h = self.boundary.height
        
        ne_boundary = Boundary(x + w/2, y, w/2, h/2)
        nw_boundary = Boundary(x, y, w/2, h/2)
        se_boundary = Boundary(x + w/2, y + h/2, w/2, h/2)
        sw_boundary = Boundary(x, y + h/2, w/2, h/2)
        
        self.northeast = Quadtree(ne_boundary, self.capacity)
        self.northwest = Quadtree(nw_boundary, self.capacity)
        self.southeast = Quadtree(se_boundary, self.capacity)
        self.southwest = Quadtree(sw_boundary, self.capacity)
        
        
        for organism in self.organisms:
            if self.northeast.insert(organism):
                continue
            elif self.northwest.insert(organism):
                continue
            elif self.southeast.insert(organism):
                continue
            elif self.southwest.insert(organism):
                continue
    
    def query_range(self, range_boundary, found=[]):
        if found is None:
            found = []  

        if not self.boundary.intersects(range_boundary):
            return found

        if self.divided:
            found = self.northeast.query_range(range_boundary, found.copy())
            found = self.northwest.query_range(range_boundary, found.copy())
            found = self.southeast.query_range(range_boundary, found.copy())
            found = self.southwest.query_range(range_boundary, found.copy())
        else:
            
            for organism in self.organisms:
                if range_boundary.contains_point(organism.x, organism.y):
                    found.append(organism)

        return found
        
    
    def query_all_organisms(self):
        all_organisms = []
        
        if self.divided:
            all_organisms.extend(self.northeast.query_all_organisms())
            all_organisms.extend(self.northwest.query_all_organisms())
            all_organisms.extend(self.southeast.query_all_organisms())
            all_organisms.extend(self.southwest.query_all_organisms())
        else:
            all_organisms.extend(self.organisms)
        
        return all_organisms
    
    def remove(self, organism):
        if organism in self.organisms:
            self.organisms.remove(organism)
            return True
        elif self.divided:
            if self.northeast.remove(organism):
                return True
            elif self.northwest.remove(organism):
                return True
            elif self.southeast.remove(organism):
                return True
            elif self.southwest.remove(organism):
                return True
        return False