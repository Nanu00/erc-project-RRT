from obstacle import EndArea, Obsctacle
import tree, utils
import matplotlib.pyplot as plt

obs = [ Obsctacle((utils.Point(600, 700), utils.Point(700, 600), utils.Point(700, 700))) ]

end = EndArea((utils.Point(700, 700), utils.Point(750, 700), utils.Point(750, 750), utils.Point(700, 750)))

t = tree.Tree(utils.Point(500, 500), end, (utils.Point(0, 0), utils.Point(1000, 1000)), obs)

plt.ion()

for _ in range(1000):
    plt.cla()
    path = t.sample_iter(50)

    if path:
        plottable = t.get_plottable() + [o.get_plottable() for o in t.obstacles] + [t.end.get_plottable()] + [path.plottable_path()]
        for a in plottable:
            plt.plot(*a, marker='.', markersize=5)
        plt.show()
        plt.pause(100)
        break

    plottable = t.get_plottable() + [o.get_plottable() for o in t.obstacles] + [t.end.get_plottable()]

    for a in plottable:
        plt.plot(*a, marker='.', markersize=5)

    plt.show()
    plt.pause(0.0001)
