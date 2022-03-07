#from shapely.ops import polygonize
from shapely.geometry import Polygon
#from shapely.geometry import MultiPolygon
from shapely.geometry import Point
#from shapely.geometry import MultiLineString
#from anytree import NodeMixin, LevelOrderIter, PreOrderIter
import matplotlib.pyplot as plt

class PointNode(Point, NodeMixin):
    def __init__(self, x, y, parent=None, children=None):
        self.x = x
        self.y = y
        self.parent = parent
        if children:
            self.children = children

    def __repr__(self):
        return "PointNode(%f, %f)" % (self.x, self.y)

''' start transplant'''

class Obsctacle:
    '''Obsctacle
    Attributes:
        I. boundary points
        II. check if line segment passes through obsctacle
            1. use some lineat alg
            2. check what nanu00 sent
    '''

    def __init__(self, start, end, boundaries, obstacles=[]):
        '''Inits the class Tree with a start point and an end "obstacle"'''
        self.start = PointNode(start.x, start.y)
        self.end = end
        self.boundaries = boundaries
        self.obstacles = obstacles
        self.max_dist = min(abs(boundaries[0].x - boundaries[1].x), abs(boundaries[0].y - boundaries[1].y))

    def sample_iter(self, n):
        if n == 0:
            return

        for _ in range(n):
            new_point = Point.random_with_boundaries(self.boundaries)
            closest_node = self.start
            least_dist = self.start.dist(new_point)
            for p in PreOrderIter(self.start):
                if p.dist(new_point) < least_dist:
                    closest_node = p
                    least_dist = p.dist(new_point)
            if least_dist > self.max_dist:
                m = closest_node.slope(new_point)
                new_x = 1/((1 + m**2)**0.5) * self.max_dist
                new_y = 1/((1 + (1/m)**2)**0.5) * self.max_dist
                new_point = Point(new_x, new_y)

            PointNode(new_point.x, new_point.y, parent = closest_node)

    def get_plottable(self):
        plottable = []
        for n in reversed(list(LevelOrderIter(self.start))):
            if n.parent:
                plottable.append(([n.x, n.parent.x], [n.y, n.parent.y], 'b-'))
        return plottable
