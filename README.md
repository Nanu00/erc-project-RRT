# ERC Mini-project: RRT
This is an implementation of the RRT algorithm for ERC's path planning mini-project

# Overview
- Designing a basic implementation of RRT
- Visualising it

All the visualising is done using [matplotlib](https://matplotlib.org/)

Tree operations are done using the [anytree](https://pypi.org/project/anytree/) library

Geometry and collision detection is handled by [shapely](https://pypi.org/project/Shapely/)

Dependencies are listed in [requirements.txt](./requirements.txt)

## Classes

### Point
- A simple wrapper around `shapely.geometry.Point`
- #### Methods:
    - Distance from another point
    - New random point within boundaries

### Tree
- Made out of nodes who hold their sub-nodes
- #### Methods:
    - Sample next iteration
    - Check for collisions
    - Check if solution reached

### PointNode
- The nodes in the tree
- A wrapper around the `Point` class
- Uses `anytree.NodeMixin` for tree operations
- #### Methods:
    - Plot the path leading to it from the top of the whole tree

### Obstacles
- Made out of a list of border points
- #### Methods:
    - Check for collisions
    - Plot itself

### EndArea
- Simply the `Obstacle` class, except plots itself in green instead of red

## Objectives

- [x] Implement the basic tree and obstacle classes
- [x] Implement visualisation using matplotlib
- [x] Implement logic for sampling
- [x] Implement collision detection
