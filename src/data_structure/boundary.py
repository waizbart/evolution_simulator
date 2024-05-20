class Boundary:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def contains_point(self, px, py):
        return (px >= self.x and px <= self.x + self.width and
                py >= self.y and py <= self.y + self.height)
    
    def intersects(self, other_boundary):
        return not (self.x + self.width < other_boundary.x or
                    other_boundary.x + other_boundary.width < self.x or
                    self.y + self.height < other_boundary.y or
                    other_boundary.y + other_boundary.height < self.y)