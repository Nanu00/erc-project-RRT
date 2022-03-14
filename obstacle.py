#from shapely.ops import polygonize
from shapely.geometry import Polygon
#from shapely.geometry import MultiPolygon
from shapely.geometry import Point
from shapely.geometry import MultiLineString
#from anytree import NodeMixin, LevelOrderIter, PreOrderIter
import matplotlib.pyplot as plt

''' start transplant'''

class Obsctacle:
    '''Obsctacle
    Attributes:
        I. boundary points
        II. check if line segment passes through obsctacle
            1. use some lineat alg
            2. check what nanu00 sent
    '''

    def __init__(self, boundaries, defintions=[]):
        '''Inits the class Tree with a start point and an end "obstacle"'''
        self.boundaries = boundaries
        self.defintions = defintions

    def get_plottable(self):
        x,y = self.exterior.coords.xy
       # plt.plot(x,y)

    def checkint(self, tree): # how do you give input from external stuff?
        tree.crosses(self)
        if True:
            redo tree?
        else 
            continue

