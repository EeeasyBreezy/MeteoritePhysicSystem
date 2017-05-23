from math import *

class TrajectoryData:
    TICKS_NUMBER = 17
    TICKS_NUMBER_USED = 17

    originalHeight = []
    originalSpeed = []
    originalTime = []
    normHeight = []
    normSpeed = []
    normTime = []
    origInitHeight = None
    origInitSpeed = None
    origInitTime = 0

    @staticmethod
    def ReadData(timeFilename, heightFilename, speedFilename):
        timeFile = open(timeFilename, "r")
        heightFile = open(heightFilename, "r")
        speedFile = open(speedFilename, "r")
        for i in range(0, TrajectoryData.TICKS_NUMBER):
            TrajectoryData.originalTime.append(float(timeFile.readline()))
            TrajectoryData.originalHeight.append(float(heightFile.readline()))
            TrajectoryData.originalSpeed.append(float(speedFile.readline()))
        TrajectoryData.origInitHeight = TrajectoryData.originalHeight[0]
        TrajectoryData.origInitSpeed = TrajectoryData.originalSpeed[0]
        TrajectoryData.origInitTime = TrajectoryData.originalTime[0]
    @staticmethod
    def NormalizeData():
        TrajectoryData.normTime = []
        TrajectoryData.normHeight = []
        TrajectoryData.normSpeed = []
        for i in range(0, TrajectoryData.TICKS_NUMBER_USED):
            TrajectoryData.normHeight.append(TrajectoryData.originalHeight[i] / TrajectoryData.origInitHeight)
            TrajectoryData.normSpeed.append(TrajectoryData.originalSpeed[i] / TrajectoryData.origInitSpeed)
            normTimeCoeff = TrajectoryData.originalSpeed[0] / TrajectoryData.originalHeight[0]
            TrajectoryData.normTime.append(TrajectoryData.originalTime[i] * normTimeCoeff)
        return
    @staticmethod
    def CalculateSpeedDifference(customSpeed):
        norm = 0
        for i in range(0, TrajectoryData.TICKS_NUMBER_USED):
            norm += (TrajectoryData.normSpeed[i] - customSpeed[i]) ** 2
        norm /= len(TrajectoryData.normSpeed)
        return sqrt(norm)
    @staticmethod
    def CalculateTrajectoryDifference(customTrajectory):
        norm = 0
        for i in range(0, TrajectoryData.TICKS_NUMBER_USED):
            norm += (TrajectoryData.normHeight[i] - customTrajectory[i]) ** 2
        norm /= len(TrajectoryData.normHeight)
        return sqrt(norm)
    @staticmethod
    def ToString():
        print("Original time")
        print(TrajectoryData.originalTime)
        print("Original height")
        print(TrajectoryData.originalHeight)
        print("Original Speed")
        print(TrajectoryData.originalSpeed)
        print("------------------------------------------------")
        print("Normalized time")
        print(TrajectoryData.normTime)
        print("Normalized height")
        print(TrajectoryData.normHeight)
        print("Normalized speed")
        print(TrajectoryData.normSpeed)
        # for i in range(0, TrajectoryData.TICKS_NUMBER):
        #     print(TrajectoryData.originalTime[i])
