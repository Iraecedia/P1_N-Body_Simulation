##File containing step function and simulation class

import math
from typing import Self
from constants import initialConditions, physicsConstants

class BodyVector:
    """stores a single 3D vector"""
    x: float
    y: float
    z: float

    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z


    def __repr__(self) -> str:
        return f"BodyVector({self.x}, {self.y}, {self.z})"


    def __str__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BodyVector):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)


    def __add__(self, other: Self) -> Self:
        return BodyVector(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other: Self) -> Self:
        return BodyVector(self.x - other.x, self.y - other.y, self.z - other.z)


    def scale(self, s: float) -> Self:
        """scales a BodyVector by a constant"""
        return BodyVector(self.x * s, self.y * s, self.z * s)


    def magnitude(self) -> float:
        """returns the magnitude of a BodyVector"""
        return math.sqrt((self.x)**2 + (self.y)**2 + (self.z)**2)




class Body:
    """stores all relevant information for a single Body."""
    mass:    float        ## kg
    pos:     BodyVector   ## m
    vel:     BodyVector   ## m/s
    accel:   BodyVector   ## m/s^2
    prevPos: BodyVector   ## m

    def __init__(self, mass=0, pos=None, vel=None, accel=None, prevPos=None) -> None:
        self.mass    = mass
        self.pos     = pos if pos is not None else BodyVector()
        self.vel     = vel if vel is not None else BodyVector()
        self.accel   = accel if accel is not None else BodyVector()
        self.prevPos = prevPos if prevPos is not None else BodyVector()


    def __repr__(self) -> str:
        return f"Body({self.mass}, {self.pos}, {self.vel}, {self.accel}, {self.prevPos})"


    def __str__(self) -> str:
        return f"""
Mass:              {self.mass}
Position:          {self.pos}
Velocity:          {self.vel}
Acceleration:      {self.accel}
Previous Position: {self.prevPos}
"""


    def getPosition(self) -> BodyVector:
        """returns position of Body"""
        return self.pos


    def getVelocity(self) -> BodyVector:
        """returns velocity of Body"""
        return self.vel


    def setAcceleration(self, a: BodyVector) -> None:
        """takes a BodyVector; gives it to the Body"""
        self.accel = a



## list of N bodies, where N is physicsConstants.N
bodies = [Body(initialConditions.massDist,
               BodyVector(initialConditions.posDist,
                          initialConditions.posDist,
                          initialConditions.posDist),
               BodyVector(initialConditions.velDist,
                          initialConditions.velDist,
                          initialConditions.velDist))
          for _ in range(physicsConstants.N)]


print(bodies)
