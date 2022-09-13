from Character import Character
from Utilities import *

# Abstract behavior class
# All behaviors should inherit from this class
# contains the getSteering function which will be implemented in the child classes
# contains the update function which will update the character's position based on velocity and orientation
class Behavior:
    def getSteering(self, character):
        pass
    
    def update(self, character, timestep):
        # update position
        character.movement.position += character.movement.velocity * timestep

        # update velocity and orientation
        character.movement.velocity += character.steering.linear * timestep
        character.movement.orientation += character.steering.angular * timestep

        #check if the character is moving faster than the max speed and clip if needed
        if character.movement.velocity.magnitude() > character.maxSpeed:
            character.movement.velocity.normalize()
            character.movement.velocity *= character.maxSpeed
    
    def __str__(self):
        return "0"

# Seek behavior class
# inherits from the behavior class
# match character position to target character's position
class Seek(Behavior):
    def __init__(self, target):
        self.target = target

    # returns a steering output
    def getSteering(self, character): #
        # create a steering output
        steering = SteeringOutput()

        # get the direction to the target
        steering.linear = self.target.movement.position - character.movement.position

        #accelerate at max acceleration
        steering.linear.normalize()
        steering.linear *= character.maxAcceleration

        # give the character the new steering output
        character.steering = steering
    
    def __str__(self):
        return "6"

# Arrive behavior class
# inherits from the behavior class
# like seek but slows down as it gets closer to the target
class Arrive(Behavior):
    def __init__(self, target, slowRadius, targetRadius, timeToTarget):
        self.target = target
        self.slowRadius = slowRadius
        self.targetRadius = targetRadius
        self.timeToTarget = timeToTarget
    
    def getSteering(self, character):
        # create a steering output
        steering = SteeringOutput()

        # get the direction to the target
        direction = self.target.movement.position - character.movement.position

        # get the distance to the target
        distance = direction.magnitude()

        # if we are inside the target radius, return no steering
        if distance < self.targetRadius:
            return steering

        # check if we are inside the slow radius
        if distance < self.slowRadius:
            # calculate the target speed
            targetSpeed = character.maxSpeed * (distance / self.slowRadius)
        else:
            targetSpeed = character.maxSpeed

        # calculate the target velocity
        targetVelocity = direction.normalized() * targetSpeed

        # calculate the linear acceleration
        steering.linear = targetVelocity - character.movement.velocity
        steering.linear /= self.timeToTarget

        # check if the acceleration is too fast
        if steering.linear.magnitude() > character.maxAcceleration:
            steering.linear.normalize()
            steering.linear *= character.maxAcceleration

        # give the character the new steering output
        character.steering = steering

    
    
    def __str__(self):
        return "8"

# Flee behavior class
# inherits from the behavior class
# negate character position to target character's position
class Flee(Behavior):
    def __init__(self, target):
        self.target = target

    # returns a steering output
    def getSteering(self, character): #
        # create a steering output
        steering = SteeringOutput()

        # get the direction to the target
        steering.linear = character.movement.position - self.target.movement.position

        #accelerate at max acceleration
        steering.linear.normalize()
        steering.linear *= character.maxAcceleration

        # give the character the new steering output
        character.steering = steering

    def __str__(self):
        return "7"

# Continue behavior
# Changes nothing about the character's movement variable
class Continue(Behavior):
    def __init__(self):
        pass

    def getSteering(self, character):
        pass
    
    def __str__(self):
        return "1"
