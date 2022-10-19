#!/opt/python/stable/bin/python3
# John Ingram 2022
# Written for Mr. Sebastian's CS 330 class
# Assignment 2
from Behaviors import *

# Note that I am using the behavior nuber 11 for the path following behavior as specified in the assignment


class Main:
    def __init__(self):
        pass

    def run():
        # Create a path with the given points
        path = Path([Vector2(0, 90), Vector2(-20, 65), Vector2(20, 40), Vector2(-40, 15), Vector2(40, -10), Vector2(-60, -35), Vector2(60, -60), Vector2(0, -85)])
        
        # Create a character with the FollowPath behavior
        followCharacter = Character(2701, Movement(Vector2(20, 95), Vector2(0, 0), 0), SteeringOutput(), 4, 2, FollowPath(path, 0.04, 0))

        characters = [followCharacter]
        
        seconds = 125
        timestep = 0.5

        # loop through the characters and update their position
        with open("trajectories.txt", "w") as file:
            for i in range(int(seconds/timestep + 1)):
                elapsed = i * timestep
                for character in characters:
                    character.behavior.getSteering(character)
                    character.behavior.update(character, timestep)
                    file.write(f"{elapsed}, {character}, FALSE\n")
    

if __name__ == "__main__":
    Main.run()
