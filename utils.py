import random
import shapely.geometry

def random_with_boundaries(boundaries):
    new_x = random.random()*abs(boundaries[0].x - boundaries[1].x) + min(boundaries[0].x, boundaries[1].x)
    new_y = random.random()*abs(boundaries[0].y - boundaries[1].y) + min(boundaries[0].y, boundaries[1].y)
    return Point(new_x, new_y)

class Point(shapely.geometry.Point):
    def __init__(self, x: float, y: float):
        shapely.geometry.Point.__init__(self, x, y)

    def dist(self, pt):
        return ( ( self.x - pt.x )**2 + ( self.y - pt.y )**2 )**0.5

    def slope(self, pt):
        return (pt.y - self.y)/( pt.x - self.x )

    # def show_on_plot(plot)

    @classmethod
    def random_with_boundaries(cls, boundaries):
        new_x = random.random()*abs(boundaries[0].x - boundaries[1].x) + min(boundaries[0].x, boundaries[1].x)
        new_y = random.random()*abs(boundaries[0].y - boundaries[1].y) + min(boundaries[0].y, boundaries[1].y)
        return cls(new_x, new_y)
