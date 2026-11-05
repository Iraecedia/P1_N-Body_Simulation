import numpy as np
import math
import constants
import simulation

''' After a quick google I realized you might want a helper function'''

class ForceCalculator: 
    def gravitationalForces(self, a : Body, b : Body) -> BodyVector:
        r_vec = a.pos - b.pos
        r_mag = r_vec.magnitude()
        
        if r_mag == 0:
            return simulation.BodyVector(0, 0, 0)  
        
        f_mag = (constants.physicsConstants.G * a.mass * b.mass) / (r_mag ** 2)
        f_vec = r_vec.scale(f_mag / r_mag) 
        
        return f_vec
    
    def computeForces(self, bodies: list[Body]) -> None:
        for body in bodies:
            body.accel = simulation.BodyVector(0, 0, 0)
            
        for i in range(len(bodies)):
            for j in range(i + 1, len(bodies)):
                bodies[i].accel += self.gravitationalForces(bodies[i], bodies[j]).scale(1 / bodies[i].mass)
                bodies[j].accel -= self.gravitationalForces(bodies[i], bodies[j]).scale(1 / bodies[j].mass)