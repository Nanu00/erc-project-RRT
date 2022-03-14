#from shapely.ops import polygonize
from shapely.geometry import Polygon
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
        x,y = self.exterior.coords.xy
        return (x, y, 'r-') 

    def checkint(self, tree): # how do you give input from external stuff?
        return tree.intersects(self.pol)
