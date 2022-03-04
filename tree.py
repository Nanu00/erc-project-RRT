from utils import Point
from anytree import NodeMixin, LevelOrderIter, PreOrderIter
import matplotlib.pyplot as pyplot

class PointNode(Point, NodeMixin):
    def __init__(self, x, y, parent=None, children=None):
        self.x = x
        self.y = y
        self.parent = parent
        if children:
            self.children = children

    def __repr__(self):
        return "PointNode(%f, %f)" % (self.x, self.y)

class Tree:
    '''Tree
    Attributes:
        start: The start node, top of the tree
        end: The end area
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

        self.max_dist /= 1.3

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

    def show_on_plot(self, plot: pyplot):
        for n in reversed(list(LevelOrderIter(self.start))):
            if n.parent:
                plot.plot([n.x, n.parent.x], [n.y, n.parent.y], 'bo-')

        plot_boundaries = []

        if self.boundaries[0].x > self.boundaries[1].x:
            plot_boundaries += [self.boundaries[1].x, self.boundaries[0].x]
        else:
            plot_boundaries += [self.boundaries[0].x, self.boundaries[1].x]

        if self.boundaries[0].y > self.boundaries[1].y:
            plot_boundaries += [self.boundaries[1].y, self.boundaries[0].y]
        else:
            plot_boundaries += [self.boundaries[0].y, self.boundaries[1].y]

        plot.autoscale()
