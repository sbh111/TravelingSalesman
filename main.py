import numpy as np
import random as rd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


def main(numCities=10):
    rd.seed()
    cities = [[100 * rd.random(), 100 * rd.random(), 100 * rd.random()] for i in range(numCities)]
    cities = np.array(cities)

    fig = plt.figure()
    ax = p3.Axes3D(fig)

    # draw cities
    ax.scatter(cities[:, 0], cities[:, 1], cities[:, 2], c = 'b', s = 50)

    # draw routes
    ax.plot(cities[:, 0], cities[:, 1], cities[:, 2], color='red', linestyle='dashed')
    plt.show()


main(10)
