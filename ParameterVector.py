class Individual:
    a1 = None
    a2 = None
    initGamma = None
    costFunction = None
    costFunctionSpeed = None
    selectionProbability = None
    correspondingSolution = None

    def __init__(self, a1 = 0, a2 = 0, initGamma = 0, costFunction = 0):
        self.a1 = a1
        self.a2 = a2
        self.initGamma = initGamma
        self.costFunction = costFunction
    def ToString(self):
        result = "a1: " + str(self.a1) + "\n"
        result += "a2: " + str(self.a2) + "\n"
        result += "inital gamma: " + str(self.initGamma) + "\n"
        result += "cost function: " + str(self.costFunction) + "\n"
        return result
