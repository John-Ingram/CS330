#!/opt/python/stable/bin/python3
# John Ingram 2022
# Written for Mr. Sebastian's CS 330 class
# Assignment 1
from Behaviors import *

# Note that I am using the behavior nubers from the assignment, not the ones from the python plotter

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
        for i in range(int(seconds/timestep + 1)):
            elapsed = i * timestep
            for character in characters:
                character.behavior.getSteering(character)
                character.behavior.update(character, timestep)
                file.write(f"{elapsed}, {character}, FALSE\n")


    