
import math
import numpy as np
from itertools import permutations
import random as rd


class Brute:
    def __init__(self, cities):
        self.cities = cities
        self.it = 0

        bestRoute = cities
        self.bestRoute = np.append(bestRoute, [bestRoute[0]], axis=0)
        self.bestDist = self.totDist(self.bestRoute)

        _permutations = list(permutations(range(0, len(cities))))
        rd.shuffle(_permutations)
        self.permutations = [list(p) for p in _permutations]
        pass

    def update(self):
        retVal = None
        if self.it < len(self.permutations):
            # get the current permutation
            currPerm = self.permutations[self.it]

            # get the route associated with perm, and append the beginning to make it a cycle
            currRoute = self.cities[currPerm]
            currRoute = np.append(currRoute, [currRoute[0]], axis=0)

            # if currRoute is better, then update best route
            currDist = self.totDist(currRoute)
            if currDist < self.bestDist:
                self.bestRoute = currRoute
                self.bestDist = currDist

            retVal = currRoute

        self.it += 1
        return retVal

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
