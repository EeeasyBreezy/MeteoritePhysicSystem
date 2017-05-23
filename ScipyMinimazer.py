from scipy.optimize import *
from SystemSolver import *
from TrajectoryData import *
from RandomGenerator import *
from ParameterVector import *
import numpy as np

class ScipyMinimizer:
    solver = None
    LOW_BORDER_A1 = 0
    TOP_BORDER_A1 = 5000
    LOW_BORDER_A2 = 0
    TOP_BORDER_A2 = 0.1
    iteration = None

    def __init__(self):
        self.solver = SystemSolver()
        self.iteration = 0

    def TargetFunction(self, v):
        vector = Individual(v[0], v[1], v[2])
        self.solver.InitSystemParams(vector)
        solution = self.solver.SolveSystem()
        trajectory = solution[2]
        speed = solution[0]
        # norm = TrajectoryData.CalculateTrajectoryDifference(trajectory)
        norm = TrajectoryData.CalculateTrajectoryDifference(trajectory) + \
               TrajectoryData.CalculateSpeedDifference(speed)
        self.iteration += 1
        print("Iteration " + str(self.iteration) + ": " + str(norm))
        return norm
    def Minimize(self):
        initA1 = RandomGenerator.GetRandomFloat(self.LOW_BORDER_A1, self.TOP_BORDER_A1)
        initA2 = RandomGenerator.GetRandomFloat(self.LOW_BORDER_A2, self.TOP_BORDER_A2)
        initGamma = RandomGenerator.GetRandomFloat(0, 90)
        init = np.array([initA1, initA2, initGamma])
        opt =\
            {
                'disp': True,
                'maxiter': 10000,
                'xatol': 10 ** (-6),
                'fatol': 10 ** (-6),
            }
        result = minimize(self.TargetFunction, init, method = 'nelder-mead', options = opt)
        return result