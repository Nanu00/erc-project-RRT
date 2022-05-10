from obstacle import Obsctacle
import tree, utils
import matplotlib.pyplot as plt

# Define all the obstables
obstacle_list = [
[(40, 0), (40, 40), (50, 50), (60, 40), (50, 40)],
[(10, 10), (20, 20), (10, 30), (0, 20)],
[(50, 60), (70, 80), (60, 100), (40, 80), (45, 100)],
[(70, 20), (90, 20), (80, 40)] ]

obs = [ Obsctacle(tuple(o)) for o in obstacle_list ]

# Define the end area
end = utils.Point(100, 1)

# Make the tree by putting in the starting point and boundaries
t = tree.Tree(utils.Point(1, 1), end, (utils.Point(0, 0), utils.Point(100, 100)), obs)

plt.ion()

# Plot the obstacles and the end area
# Outside the loop because they only need to be plotted once
plottable = [o.get_plottable() for o in t.obstacles] + [(t.end.x, t.end.y, "g")]

for a in plottable:
    plt.plot(*a, marker='.', markersize=5)

# Fail if solution isn't found in 1000 iterations
for _ in range(1000):
    # Sample points for the current iteration and plot them
    path = t.sample_iter(50, plt)

    # Check if solution was found, plot it and break if yes
    if path:
        plottable = path.plottable_path()
        plt.plot(*plottable, marker='.', markersize=1, linewidth=1)
        plt.show()
        plt.pause(100)
        break

    # Show the plot for the current iteration
    plt.show()
    plt.pause(0.0001)
