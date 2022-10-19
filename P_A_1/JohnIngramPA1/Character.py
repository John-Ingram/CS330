# John Ingram 2022
# Written for Mr. Sebastian's CS 330 class
# Assignment 1
class Character:
    def __init__(self, cid, movement, steering, maxSpeed, maxAcceleration, behavior): # id is cid because id is a function in python
        self.cid = cid
        self.movement = movement
        self.steering = steering
        self.maxSpeed = maxSpeed
        self.maxAcceleration = maxAcceleration
        self.behavior = behavior

    # output the character's data as cid, name, movement, steering
    def __str__(self):
        return f"{self.cid}, {self.movement.position}, {self.movement.velocity}, {self.steering.linear}, {self.movement.orientation}, {self.behavior}"
