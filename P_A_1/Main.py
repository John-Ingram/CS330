import math

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

class Movement:
    def __init__(self, position, velocity, orientation):
        self.position = position
        self.velocity = velocity
        self.orientation = orientation

    # output the movement's data as position, velocity, orientation
    def __str__(self):
        return f"{position}, {velocity}, {orientation}"

# Steering output class
# contains liner acceleration (2d vector), and angular acceleration (float)
class SteeringOutput:
    def __init__(self):
        self.linear = Vector2(0, 0)
        self.angular = 0

# Vector2 class
# This class is used to represent a 2D vector, which can be used to represent position, velocity, and more.
class Vector2:
    def __init__(self, x, z):
        self.x = x
        self.z = z
    
    # Returns the magnitude of the vector
    def magnitude(self):
        return math.sqrt(self.x**2 + self.z**2)

    # Returns the normalized vector
    def normalized(self):
        magnitude = self.magnitude()
        return Vector2(self.x / magnitude, self.z / magnitude)

    # Normalize this vector
    def normalize(self):
        magnitude = self.magnitude()
        self.x /= magnitude
        self.z /= magnitude

    # additon operator
    def __add__(self, other):
        return Vector2(self.x + other.x, self.z + other.z)

    # subtraction operator
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.z - other.z)
    
    # multiplication operator
    def __mul__(self, other):
        return Vector2(self.x * other, self.z * other) 

    # division operator
    def __truediv__(self, other):
        return Vector2(self.x / other, self.z / other)
    
    #output the vector's data as x, z
    def __str__(self):
        return f"{self.x}, {self.z}"
        

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

if __name__ == "__main__":
    # Create a character with all zeros at position (0, 0)
    continueCharacter = Character(2601, Movement(Vector2(0, 0), Vector2(0, 0), 0), SteeringOutput(), 0, 0, Continue())
    # Create a character with the seek behavior at position (-50, 40) initial velocity: (0, 8) initial orientation: 3pi/2 max velocity: 8 max acceleration: 2 target: continueCharacter
    seekCharacter = Character(2602, Movement(Vector2(-50, 40), Vector2(0, 8), (3*math.pi/2)), SteeringOutput(), 8, 2, Seek(continueCharacter))
    # Create a character with the flee behavior at position (-30, -50) initial velocity: (2, 7) initial orientation: (pi/4) max velocity: 8 max acceleration: 1.5 target: continueCharacter
    fleeCharacter = Character(2603, Movement(Vector2(-30, -50), Vector2(2, 7), (math.pi/4)), SteeringOutput(), 8, 1.5, Flee(continueCharacter))
    # Create a character with the arrive behavior. position: (50, 75) initial velocity: (-9, 4) initial orientation: pi max velocity: 8 max acceleration: 2 target: continueCharacter slow radius: 32 target radius: 4 time to target: 1
    arriveCharacter = Character(2604, Movement(Vector2(50, 75), Vector2(-9, 4), math.pi), SteeringOutput(), 8, 2, Arrive(continueCharacter, 32, 4, 1))
    characters = [continueCharacter, seekCharacter, fleeCharacter, arriveCharacter]
    seconds = 50
    timestep = 0.5

    # loop through the characters and update their position
    with open("output.txt", "w") as file:
        for i in range(int(seconds/timestep)):
            elapsed = i * timestep
            for character in characters:
                character.behavior.getSteering(character)
                character.behavior.update(character, timestep)
                file.write(f"{elapsed}, {character}, FALSE\n")


    