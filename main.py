"""
Author: Saad Bhatti
Desc:
The Travelling Salesman Problem is a famous problem in CS. The premise is simple, given a
list of 'cities' find the best tour/route that visits all of them. It is in the NP-Complete
Class of problems, meaning there is no polynomial exact solution. The best we can do is
find optimizations instead of exact solutions. This project explores 2 algorithms to find
a tour. The first algorithm is the naive/brute force algorithm. It first finds all the permutations
of the routes and tries them all to find the most optimal one. This algorithm has O(N!) complexity, which
is not ideal. The second algorithm is a Genetic Algorithm. As the name suggests, it takes inspiration
from genetics in biology. First the algorithm selects a few tours from a 'population' of tours. It then performs
'mutations' on those few tours and creates a new population descendant from the mutations.
This algorithm arrives at an near optimal tour much faster than the brute force, especially if the
number of cities is large
"""

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

from brute import Brute
from ga import GeneticAlgo


def update(frame, ax, cities, Algo):
    # get cycles
    currRoute = Algo.update()
    bestRoute = Algo.getBestRoute()
    bestDist = Algo.getBestDist()

    ax.clear()
    ax.view_init(azim=frame * 2)

    name = None
    if type(Algo) == GeneticAlgo:
        name = "Genetic Algorithm"
    elif type(Algo) == Brute:
        name = "Brute Force Algorithm"

    ax.set_title("{0}\nBest Squared Distance So Far: {1}".format(name, round(bestDist)))

    ax.scatter(cities[:, 0], cities[:, 1], cities[:, 2], c='r', s=50)
    if currRoute is not None:
        ax.plot(currRoute[:, 0], currRoute[:, 1], currRoute[:, 2], color='salmon', linestyle='dashed')
        pass
    ax.plot(bestRoute[:, 0], bestRoute[:, 1], bestRoute[:, 2], color='blue', linestyle='solid', linewidth=2)


def main(maxDist=100):
    rd.seed()
    numCities = 0
    while True:
        inp1 = int(input("\nEnter the number of cities:"))

        if inp1 <= 3:
            print("Number of cities has to be more than 3.")
            continue
        numCities = inp1
        break

    cities = [[maxDist * rd.random(), maxDist * rd.random(), maxDist * rd.random()] for i in range(numCities)]
    cities = np.array(cities)

    algo = None

    prompt = "Select an Algoritm:\n" \
             "0: Brute Force\n" \
             "1: Genetic Algorithm\n"

    while True:
        inp2 = input(prompt)

        if inp2 is '0':

            if numCities > 10:
                inp3 = input("It's going to take a while to calculate {} permutations.\n"
                             "Are you sure you want to do Brute Force Algorithm? (y/n).\n".format(numCities))
                if inp3 is not 'y' or inp2 is not 'Y':
                    continue
            print("Generating permutations, may take a while.\n")
            algo = Brute(cities)
            break
        elif inp2 is '1':
            algo = GeneticAlgo(cities, 200)
            break
        else:
            continue

    fig = plt.figure(figsize=(8, 6))
    ax = p3.Axes3D(fig)

    ani = animation.FuncAnimation(fig, update, fargs=(ax, cities, algo), interval=1)
    plt.show()


main(10)
