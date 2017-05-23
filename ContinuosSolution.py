from SystemSolver import *
from TrajectoryData import *
from numpy import *
from matplotlib.pyplot import *
from ParameterVector import *
from AnalyticSolution import *


def ReadData():
    TrajectoryData.ReadData("data\\innisfri time.txt", "data\\innisfri height.txt", "data\\innisfri speed.txt")
    TrajectoryData.NormalizeData()
    TrajectoryData.ToString()

def Error(analyticHeight, numHeight):
    err = 0
    for i in range(1, len(analyticHeight)):
        err += ((analyticHeight[i] - numHeight[i]) ** 2)
    err /= len(analyticHeight)
    print(err)

def Main():
    T = 10
    A1 = 35.19
    A2 = 21.75
    gamma = 64.01
    ReadData()
    solver = SystemSolver()
    solver.timePoints = linspace(0, T, num = 500)
    vector = Individual(A1, A2, gamma)
    solver.InitSystemParams(vector)
    traj = solver.SolveSystem()
    # plot(solver.timePoints, trajectory[2], "r-")
    # xlabel("Время")
    # ylabel("Высота")
    # show()
    analyticPlot = GetHeightPoints()
    aHeight = []
    for i in range(0, len(traj[0])):
        aHeight.append(GetHeight(traj[0][i], 7.24, 1.99))
        traj[2][i] *= TrajectoryData.origInitHeight
        traj[2][i] /= 7.160
    Error(aHeight, traj[2])
    for i in range(0, len(traj[0])):
        traj[0][i] *= TrajectoryData.originalSpeed[0]
        traj[2][i] /= 7.160
        traj[2][i] *= TrajectoryData.originalHeight[0]
    for i in range(0, len(analyticPlot[0])):
        analyticPlot[0][i] *= TrajectoryData.originalSpeed[0]
        analyticPlot[1][i] *= 7.160
        aHeight[i] *= 7.160
    plot(TrajectoryData.originalSpeed, TrajectoryData.originalHeight, 'go')
    plot(traj[0], traj[2], 'r^')
    plot(analyticPlot[0], analyticPlot[1], 'b')
    legend(( "Точки наблюдений", "Численное решение", "Аналитическое решение"))
    xlabel("Скорость")
    ylabel("Высота")
    show()
    plot(traj[0], traj[2], 'r^')
    plot(traj[0], aHeight, 'b')
    show()
    return

Main()