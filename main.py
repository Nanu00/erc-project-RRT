from obstacle import Obsctacle
import tree, utils
import matplotlib.pyplot as plt

obs = [ Obsctacle((utils.Point(600, 600), utils.Point(700, 700), utils.Point(600, 700))) ]

t = tree.Tree(utils.Point(500, 500), utils.Point(900, 325), (utils.Point(0, 0), utils.Point(1000, 1000)), obs)

plt.ion()

for _ in range(1000):
    plt.cla()
    t.sample_iter(10)
    plottable = t.get_plottable() + [o.get_plottable() for o in t.obstacles]
    for a in plottable:
        plt.plot(*a, marker='.', markersize=5)
    plt.show()
    plt.pause(0.0001)
