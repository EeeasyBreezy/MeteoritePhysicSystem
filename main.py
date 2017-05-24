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

    # searching solution with c_d = 2.0
    minimizer = ScipyMinimizer()
    result = minimizer.Minimize()
    print(result)
    minC2 = result['fun']
    min = result.x
    solver = SystemSolver()
    vector = Individual(min[0], min[1], min[2])
    solver.InitSystemParams(vector)
    traj = solver.SolveSystem()
    trajC2 = traj[2]
    speedC2 = traj[0]
    time = TrajectoryData.normTime
    solver.timePoints = linspace(0, 50.8, num = 1000)
    traj = solver.SolveSystem()
    trajC2Continued = traj[2]

    # searching solution with c_d = 0.5
    minimizer = ScipyMinimizer()
    minimizer.solver.DRAG_COEFF = 0.5
    result = minimizer.Minimize()
    print(result)
    minC05 = result['fun']
    print(minC2)
    print(minC05)
    min = result.x
    vector = Individual(min[0], min[1], min[2])
    solver.InitSystemParams(vector)
    solver.timePoints = TrajectoryData.normTime
    solver.DRAG_COEFF = 0.5
    traj = solver.SolveSystem()
    trajC05 = traj[2]
    speedC05 = traj[0]
    solver.timePoints = linspace(0, 50.8, num = 1000)
    traj = solver.SolveSystem()
    traj05Continued  = traj[2]
    # plotting
    plot(time, TrajectoryData.normHeight, "go")
    plot(time, trajC2, "r-")
    plot(time, trajC05, "b--", linewidth = 2.0)
    xlabel("t")
    ylabel("y")
    show()
    plot(time, TrajectoryData.normSpeed, "go")
    plot(time, speedC2, "r-")
    plot(time, speedC05, "b--", linewidth = 2.0)
    xlabel("t")
    ylabel("v")
    show()

    plot(solver.timePoints, trajC2Continued, 'r')
    plot(solver.timePoints, traj05Continued, 'b--', linewidth = 2.0)
    xlabel("t")
    ylabel("y")
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
    xlabel("V")
    ylabel("H")
    show()
    return

MainScipy()
# MainGA()
