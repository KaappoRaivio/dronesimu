import numpy as np

from src.vector import Vector3D, PositionalVector3D

from scipy.spatial.transform import Rotation as R

MAX_THRUST_PER_MOTOR = 2.5 # N
AIRCRAFT_MASS = 0.7 # kg

class Drone:
    def __init__(self):
        self.position = Vector3D(0, 0, 25)
        self.velocity = Vector3D(0, 0, 0)
        self.acceleration = Vector3D(0, 0, 0)

        self.orientation = Vector3D(10, 0, 0)
        self.angular_velocity = Vector3D(0, 0, 0)
        self.angular_acceleration = Vector3D(0, 0, 0)

        self.throttle = 0.50


    def tick(self, delta_time, gravity):
        self.angular_velocity += self.angular_acceleration * delta_time
        self.orientation += self.angular_velocity * delta_time


        aircraft_weight = Vector3D(0, 0, gravity * Vector3D(0, 0, 1) * AIRCRAFT_MASS)
        aircraft_thrust = self.orientation.bad_euler_to_sphere_coords() * self.throttle * MAX_THRUST_PER_MOTOR * 4


        self.acceleration = (aircraft_thrust + aircraft_weight) / AIRCRAFT_MASS
        self.velocity += self.acceleration * delta_time
        self.position += self.velocity * delta_time

        print(self.position, self.acceleration, self.orientation.bad_euler_to_sphere_coords())


    def getPlottable(self):
        if (self.position.k < 0):
            return PositionalVector3D(Vector3D(0, 0, 0), Vector3D(100000000, 100000000, 10000000))
        else:
            return PositionalVector3D(self.orientation.bad_euler_to_sphere_coords(), self.position)


# print(Drone().tick(None))