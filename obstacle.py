#from shapely.ops import polygonize
from shapely.geometry import Polygon, LineString
import matplotlib.pyplot as plt

''' start transplant'''

class Obsctacle:
    '''Obsctacle
    Attributes:
        I. boundary points
        II. check if line segment passes through obsctacle
    '''

    def __init__(self, defintions):
        '''Inits the class Tree with a start point and an end "obstacle"'''
        self.defintions = defintions
        self.pol = Polygon(self.defintions)

    def get_plottable(self):
        x,y = self.pol.exterior.coords.xy
        return (x, y, 'r-') 

    def checkint(self, p1, p2):
        """Check for intersections between a line defined by 2 points and the obstacle itself.
        """
        l = LineString([p1, p2])
        return self.pol.intersects(l)
