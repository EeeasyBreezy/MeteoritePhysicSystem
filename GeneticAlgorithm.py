# Import section: required modules are imported here
from RandomGenerator import *
from ParameterVector import *

# Class GeneticAlgorithm
# Implements a geneting algorithm for searching parameters of
# differential equation system
class GeneticAlgorithm:
    SET_SIZE = 150
    CROSSOVER_PROB = 0.6
    MUTATION_PROB = 0.4
    ITERATIONS = 10000
    offspringsNumber = 5
    argSet = None
    C_S = 0.075
    LOW_BORDER_A1 = 0
    TOP_BORDER_A1 = 5000
    LOW_BORDER_A2 = 0
    TOP_BORDER_A2 = 0.1

    # Construtor
    def __init__(self):
        self.argSet = []
        self.offsprings = []
        return
    # Generating initial set of individuals
    def GenerateInitSet(self):
        for i in range(0, self.SET_SIZE):
            a1 = RandomGenerator.GetRandomFloat(self.LOW_BORDER_A1, self.TOP_BORDER_A1)
            a2 = RandomGenerator.GetRandomFloat(self.LOW_BORDER_A2, self.TOP_BORDER_A2)
            gamma = RandomGenerator.GetRandomFloat(0, 90)
            newIndividual = Individual(a1, a2, gamma)
            self.argSet.append(newIndividual)
        return
    # Sort set by increase of cost function
    def SortSetByCostFunction(self):
        # Key for sort function
        def SortKey(individual):
            return individual.costFunction
        self.argSet.sort(key = SortKey)
        return
    # Distribute probabilities in sorted set of individuals
    def DistributeProbabilities(self):
        for i in range(0, self.SET_SIZE):
            self.argSet[i].selectionProbability = self.C_S * (1 - self.C_S) ** (i - 1)
        return
    # Select parent number for crossover
    def SelectParent(self):
        c = RandomGenerator.GetRandomFloat(0, 1)
        r = 0
        for i in range(0, self.SET_SIZE):
            r += self.argSet[i].selectionProbability
            if r >= c:
                return i
        return (self.SET_SIZE - 1)
    # Make crossover
    def MakeHeuristicCrossover(self):
        self.SortSetByCostFunction()
        self.DistributeProbabilities()
        self.offsprings = []
        for i in range(0, self.offspringsNumber):
            newOffspring = Individual()
            parentOne = self.SelectParent()
            parentTwo = self.SelectParent()
            parentOneA1 = self.argSet[parentOne].a1
            parentTwoA1 = self.argSet[parentTwo].a1
            parentOneA2 = self.argSet[parentOne].a2
            parentTwoA2 = self.argSet[parentTwo].a2
            parentOneGamma = self.argSet[parentOne].initGamma
            parentTwoGamma = self.argSet[parentTwo].initGamma
            w = RandomGenerator.GetRandomFloat(0, 1)
            if parentOneA1 < parentTwoA1:
                newOffspring.a1 = parentOneA1 + w * (parentTwoA1 - parentOneA1)
            else:
                newOffspring.a1 = parentTwoA1 + w * (parentOneA1 - parentTwoA1)
            w = RandomGenerator.GetRandomFloat(0, 1)
            if parentOneA2 < parentTwoA2:
                newOffspring.a2 = parentOneA2 + w * (parentTwoA2 - parentOneA2)
            else:
                newOffspring.a2 = parentTwoA2 + w * (parentOneA2 - parentTwoA2)
            w = RandomGenerator.GetRandomFloat(0, 1)
            if parentOneGamma < parentTwoGamma:
                newOffspring.initGamma = parentOneGamma + w * (parentTwoGamma - parentOneGamma)
            else:
                newOffspring.initGamma = parentTwoGamma + w * (parentOneGamma - parentTwoGamma)
            newOffspring.selectionProbability = 0
            newOffspring.costFunction = 0
            self.offsprings.append(newOffspring)
        j = 0
        for i in range(self.SET_SIZE - 1, self.SET_SIZE - 1 - len(self.offsprings) , -1):
            self.argSet[i] = self.offsprings[j]
            j += 1
        return
    # Mutate individual
    def MakeMutation(self):
        indivNum = RandomGenerator.GetRandomInt(0, self.SET_SIZE)
        a1 = RandomGenerator.GetRandomFloat(self.LOW_BORDER_A1, self.TOP_BORDER_A1)
        a2 = RandomGenerator.GetRandomFloat(self.LOW_BORDER_A2, self.TOP_BORDER_A2)
        gamma = RandomGenerator.GetRandomFloat(0, 90)
        mutant = Individual(a1 = a1, a2 = a2, initGamma = gamma)
        self.argSet[indivNum] = mutant
        return
    def GetAverageCostFunction(self):
        averageCostFunction = 0
        for i in range(0, self.SET_SIZE):
            averageCostFunction += self.argSet[i].costFunction
        averageCostFunction /= self.SET_SIZE
        return averageCostFunction
    # Print set to console
    def PrintSet(self):
        for i in range(0, self.SET_SIZE):
            print("(" + str(self.argSet[i].a1) + ", " + str(self.argSet[i].a2) + \
                  ", " + str(self.argSet[i].costFunction) + "," + \
                  str(self.argSet[i].selectionProbability) +  ")")
        return