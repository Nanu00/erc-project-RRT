class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, pt):
        return ( ( self.x - pt.x )**2 + ( self.y - pt.y )**2 )**0.5

    # def show_on_plot(plot)
