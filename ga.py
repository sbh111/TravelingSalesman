import math
import numpy as np
import random as rd


class GeneticAlgo:

    def __init__(self, cities, popSize=100):
        self.cities = cities
        self.popSize = popSize
        self.it = 0

        bestRoute = self.cities
        self.bestRoute = np.append(bestRoute, [bestRoute[0]], axis=0)
        self.bestDist = self.totDist(self.bestRoute)

        order = list(range(0, len(self.cities)))
        self.population = [rd.sample(order, len(order)) for i in range(popSize)]
        self.fitness, _, _ = self.calcFitness(self.population)

    def calcFitness(self, pop):
        currRecord = math.inf
        currBestRoute = None
        fitness = []
        sumFitness = 0

        for route in pop:
            route = self.cities[route]
            _route = np.append(route, [route[0]], axis=0)
            dist = self.totDist(_route)
            if dist < currRecord:
                currRecord = dist
                currBestRoute = _route
            fit = 1 / (dist ** 8 + 1)
            sumFitness += fit
            fitness.append(fit)

        # normalize fitness
        fitness = [float(i) / sumFitness for i in fitness]

        return fitness, currBestRoute, currRecord

    def update(self):
        retval = None

        # calculate fitness of curr population
        fitness, currBestRoute, currBestDist = self.calcFitness(self.population)
        if currBestDist < self.bestDist:
            self.bestDist = currBestDist
            self.bestRoute = currBestRoute

        newPop = []
        for i in self.population:
            orderA = rd.choices(self.population, fitness, k=1)[0]
            orderB = rd.choices(self.population, fitness, k=1)[0]

            crossOrder = self.crossover(orderA, orderB)
            self.mutate(crossOrder, 1)
            newPop.append(crossOrder)

        self.population = newPop
        retval = currBestRoute
        self.it += 1
        return retval

    @staticmethod
    def mutate(order, mutationRate=0.01):
        for i in range(len(order)):
            if rd.random() < mutationRate:
                idxA = rd.randint(0, len(order) - 1)
                idxB = (idxA + 1) % len(order)
                order[idxA], order[idxB] = order[idxB], order[idxA]

    @staticmethod
    def crossover(orderA, orderB):
        # cross over some genes from orderA and orderB
        start = rd.randint(0, len(orderA) - 1)
        end = rd.randint(start + 1, len(orderA))
        newOrder = orderA[start:end]

        for i in orderB:
            if i not in newOrder:
                newOrder.append(i)
        return newOrder

    def getBestRoute(self):
        return self.bestRoute

    def getBestDist(self):
        return self.bestDist

    @staticmethod
    def euclidDist(x1, y1, z1, x2, y2, z2):
        return (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2

    def totDist(self, points):
        total = 0
        for i in range(0, len(points) - 1):
            currP = points[i]
            nextP = points[i + 1]
            total += self.euclidDist(
                currP[0], currP[1], currP[2],
                nextP[0], nextP[1], nextP[2]
            )
        return total
