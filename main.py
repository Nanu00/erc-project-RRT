from obstacle import EndArea, Obsctacle
import tree, utils
import matplotlib.pyplot as plt

# Define all the obstables
obs = [ Obsctacle((utils.Point(600, 700), utils.Point(700, 600), utils.Point(700, 700))) ]

# Define the end area
end = EndArea((utils.Point(700, 700), utils.Point(750, 700), utils.Point(750, 750), utils.Point(700, 750)))

# Make the tree by putting in the starting point and boundaries
t = tree.Tree(utils.Point(500, 500), end, (utils.Point(0, 0), utils.Point(1000, 1000)), obs)

plt.ion()

# Plot the obstacles and the end area
# Outside the loop because they only need to be plotted once
plottable = [o.get_plottable() for o in t.obstacles] + [t.end.get_plottable()]

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
