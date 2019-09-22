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
    ax.view_init(azim=frame*2)
    ax.set_title("Best Squared Distance So Far: {}".format(bestDist))

    ax.scatter(cities[:, 0], cities[:, 1], cities[:, 2], c='r', s=50)
    if currRoute is not None:
        ax.plot(currRoute[:, 0], currRoute[:, 1], currRoute[:, 2], color='salmon', linestyle='dashed')
        pass
    ax.plot(bestRoute[:, 0], bestRoute[:, 1], bestRoute[:, 2], color='blue', linestyle='solid', linewidth=2)


def main(numCities=10, maxDist=100):
    rd.seed()
    cities = [[maxDist * rd.random(), maxDist * rd.random(), maxDist * rd.random()] for i in range(numCities)]
    cities = np.array(cities)
    #brute = Brute(cities)
    genetic = GeneticAlgo(cities, 200)

    fig = plt.figure(figsize=(8, 6))
    ax = p3.Axes3D(fig)

    ani = animation.FuncAnimation(fig, update, fargs=(ax, cities, genetic), interval=1)
    plt.show()


main(15, 10)
