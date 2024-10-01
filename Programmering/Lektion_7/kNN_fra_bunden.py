#Make a class to contain a data point. The class must be able to contain an x-y-position of the data point, a class label, and a color.
class DataPoint:
    def __init__(self, x,y, label, color):
        self.x = x
        self.y = y
        self.label = label
        self.color = color