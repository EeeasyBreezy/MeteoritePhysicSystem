from scipy.integrate import *
from numpy import *
from TrajectoryData import *

class SystemSolver:

    AIR_MOLAR_MASS = 0.029
    GAS_CONSTANT = 8.314
    NORMAL_TEMPERATURE = 273.15
    NORMAL_PRESSURE = 101325
    NORMAL_DENSITY = 1.225
    GRAV_ACCELERATION = 9.834
    EARTH_RADIUS = 6400000
    K = 1.209
    DRAG_COEFF = 2.0
    GAMMA = 1
    a1 = None
    a2 = None
    density = None
    initSpeed = 1
    initHeight = 1
    initMass = 1
    initGamma = None
    timePoints = None
    timeStep = None


    def __init__(self):
        self.timePoints = linspace(0, TrajectoryData.normTime[len(TrajectoryData.originalTime) - 1], TrajectoryData.TICKS_NUMBER_USED)
        self.timeStep = self.timePoints[1]
        return

    def InitSystemParams(self, paramVector):
        self.a1 = paramVector.a1
        self.a2 = paramVector.a2
        self.initGamma = paramVector.initGamma
        self.density = 0
    def SetInitialConditions(self, initSpeed, initGamma, initHeight, initMass):
        self.initSpeed = initSpeed
        self.initMass = initMass
        self.initHeight = initHeight
        self.initGamma = initGamma
    def GetDensityOnHeight(self, height):
        height *= TrajectoryData.origInitHeight * 1000
        pressure = self.NORMAL_PRESSURE * \
                     exp(- self.AIR_MOLAR_MASS * self.GRAV_ACCELERATION * height \
                         / (self.GAS_CONSTANT * self.NORMAL_TEMPERATURE))
        density = pressure * self.AIR_MOLAR_MASS \
                     / (self.GAS_CONSTANT * self.NORMAL_TEMPERATURE)
        density /= self.NORMAL_DENSITY
        return density
        #todo: function to calculate atmosphere density on given height barometric formulas
    def System(self, f, t):
        v = f[0]
        gamma = f[1]
        y = f[2]
        m = f[3]
        rightPartV = - self.K / 2 * self.DRAG_COEFF * self.density * self.a1 * (v ** 2) * m ** (-1 / 3) + \
                        self.GRAV_ACCELERATION * TrajectoryData.origInitHeight / (1000 * TrajectoryData.origInitSpeed ** 2)
        rightPartGamma = self.GRAV_ACCELERATION * cos(gamma) / (v * TrajectoryData.originalSpeed[0]) - \
                         (v * TrajectoryData.originalSpeed[0]) / self.EARTH_RADIUS
        rightPartY = - v * sin(gamma)
        rightPartM = - self.K / 2 * self.a2 * self.a1 * self.density * (v ** 3) * (m ** (2 / 3))
        return [rightPartV, rightPartGamma, rightPartY, rightPartM]
    def SolveSystem(self):
        speed = []
        height = []
        mass = []
        gamma = []
        self.SetInitialConditions(1, self.initGamma, 1, 1)
        speed.append(1)
        height.append(1)
        mass.append(1)
        gamma.append(self.initGamma)
        self.density = self.GetDensityOnHeight(self.initHeight)
        for i in range(0, len(self.timePoints) - 1):
            self.density = self.GetDensityOnHeight(height[i])
            init = [speed[i], gamma[i], height[i], mass[i]]
            t = [self.timePoints[i], self.timePoints[i + 1]]
            result = odeint(self.System, init, t)
            speed.append(result[1][0])
            gamma.append(result[0][1])
            height.append(result[1][2])
            mass.append(result[1][3])
        return [speed, gamma, height, mass]
        #todo: system solution
        # 1. Calculate atmosphere density on current height
        # 2. Set up init conditions - new on every time step
        # 3. Solve system with ode int
