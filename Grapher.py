from matplotlib.pyplot import *

class Grapher:
    originalTrajectory = None
    calculatedTrajectory = None
    time = None
    custonTime = None

    def __init__(self, originalTrajectory = None, calculatedTrajectory = None, time = None):
        self.originalTrajectory = originalTrajectory
        self.calculatedTrajectory = calculatedTrajectory
        self.time = time

    def Plot(self, yLabel):
        plot(self.time, self.originalTrajectory)
        plot(self.time, self.calculatedTrajectory, 'r--')
        xlabel("Time")
        ylabel(yLabel)
        show()
