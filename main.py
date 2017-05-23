from GeneticAlgorithm import *
from TrajectoryData import *
from Grapher import *
from Logging import *
from SystemSolver import *
from ScipyMinimazer import *
from ParameterVector import *
from matplotlib.pyplot import *
from AnalyticSolution import *
from numpy import *

def ReadData():
    TrajectoryData.ReadData("data\\innisfri time.txt", "data\\innisfri height.txt", "data\\innisfri speed.txt")
    TrajectoryData.NormalizeData()
    TrajectoryData.ToString()

def MainScipy():
    ReadData()
    minimizer = ScipyMinimizer()
    result = minimizer.Minimize()
    print(result)
    min = result.x
    solver = SystemSolver()
    vector = Individual(min[0], min[1], min[2])
    solver.InitSystemParams(vector)
    traj = solver.SolveSystem()
    time = TrajectoryData.normTime
    plot(time, TrajectoryData.normHeight, "go")
    plot(time, traj[2], "r-")
    xlabel("Время")
    ylabel("Высота")
    legend(("Точки наблюдений", "Рассчитанная траектория"))
    show()
    plot(time, TrajectoryData.normSpeed, "go")
    plot(time, traj[0], "r-")
    xlabel("Время")
    ylabel("Скорость")
    legend(("Точки наблюдений", "Рассчитанная траектория"))
    show()
    solver.timePoints = linspace(0, 50.8, num = 1000)
    traj = solver.SolveSystem()
    plot(solver.timePoints, traj[0], 'r')
    ylabel("Speed")
    xlabel("Time")
    show()
    plot(solver.timePoints, traj[2], 'r')
    xlabel("Время")
    ylabel("Высота")
    show()
    plot(solver.timePoints, traj[3], 'r')
    xlabel("Time")
    ylabel("Mass")
    show()
    analyticPlot = GetHeightPoints()
    for i in range(0, len(traj[0])):
        traj[0][i] *= TrajectoryData.originalSpeed[0]
        traj[2][i] *= TrajectoryData.originalHeight[0]
    for i in range(0, len(analyticPlot[0])):
        analyticPlot[0][i] *= TrajectoryData.originalSpeed[0]
        analyticPlot[1][i] *= 7.160
    plot(traj[0], traj[2], 'r')
    plot(analyticPlot[0], analyticPlot[1], 'b')
    plot(TrajectoryData.originalSpeed, TrajectoryData.originalHeight, 'go')
    legend(("Численное решение", "Аналитическое решение", "Точки наблюдения"))
    xlabel("Скорость")
    ylabel("Высота")
    show()
    return

MainScipy()
# MainGA()
