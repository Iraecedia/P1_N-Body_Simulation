##File containing constants for equations and inital conditions##
import numpy as np

class physicsConstants:
    G = 6.67 * (10**-11)
    N = 10
    scalableFactor = 1

class initialConditions:
    massDist = np.random.normal(loc=4, scale=2, size=physicsConstants.N)
    posDist = np.random.exponential(scale=4, size=physicsConstants.N)
    velDist = np.random.exponential(scale=1, size=physicsConstants.N)
