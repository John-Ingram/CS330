# John Ingram
# Programming Assignment 4
# This program will implement a simple hard coded state machine
from enum import Enum
import random

# Global Variables to keep track of iterations, how many times a state was entered and how many times states were changed in total
g_follow = 0
g_pullOut = 0
g_accelerate = 0
g_pullInAhead = 0
g_pullInBehind = 0
g_decelerate = 0
g_done = 0
g_path = []

# array with all 9 possible transitions. 
# Each transition has a touple with two probabilities one for 
# each scenario
transitionProbabilites = [
    [0.8, 0.9],
    [0.4, 0.6],
    [0.3, 0.3],
    [0.4, 0.2],
    [0.3, 0.2],
    [0.3, 0.4],
    [0.8, 0.7],
    [0.8, 0.9],
    [0.8, 0.7],
]

# Enum class to keep track of states.
# Each state has a list of possible transitions
class State(Enum):
    FOLLOW = [0]
    PULL_OUT = [1, 3]
    ACCELERATE = [4, 5, 2]
    PULL_IN_AHEAD = [8]
    PULL_IN_BEHIND = [6]
    DECELERATE = [7]
    DONE = []


# Stub functions for each state
# each function will increment the number of times that state was entered
# if the scenario is 1 it will also add the state to the path
def follow(scenario):
    global g_follow
    global g_path
    g_follow += 1
    if scenario == 1:
        g_path[-1].append("state= 1 Follow")

def pullOut(scenario):
    global g_pullOut
    global g_path
    g_pullOut += 1
    if scenario == 1:
        g_path[-1].append("state= 2 Pull Out")

def accelerate(scenario):
    global g_accelerate
    global g_path
    g_accelerate += 1
    if scenario == 1:
        g_path[-1].append("state= 3 Accelerate")

def pull_in_ahead(scenario):
    global g_pullInAhead
    global g_path
    g_pullInAhead += 1
    if scenario == 1:
        g_path[-1].append("state= 4 Pull In Ahead")

def pull_in_behind(scenario):
    global g_pullInBehind
    global g_path
    g_pullInBehind += 1
    if scenario == 1:
        g_path[-1].append("state= 5 Pull In Behind")

def decelerate(scenario):
    global g_decelerate
    global g_path
    g_decelerate += 1
    if scenario == 1:
        g_path[-1].append("state= 6 Decelerate")

def done(scenario):
    global g_done
    global g_path
    g_done += 1
    if scenario == 1:
        g_path[-1].append("state= 7 Done")


def run(iterations, scenario):
    # Global variables
    global g_follow
    global g_pullOut
    global g_accelerate
    global g_pullInAhead
    global g_pullInBehind
    global g_decelerate
    global g_done
    global g_path

    # list of times each transition was taken
    transitionCounters = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    
    # Loop through the number of iterations
    for i in range(iterations):
        state = State.FOLLOW
        g_path.append([])
        # If statements to run through the state machine
        while True:
          
            # Generata a random number between 0 and 1
            rand = random.uniform(0, 1)
            # Check to see what transition to take
            if state == State.FOLLOW:
                follow(scenario)
                # check to see if we transition to pull out
                if rand < [0.8, 0.9][scenario - 1]:
                    state = state.PULL_OUT
                    pullOut(scenario)
                    transitionCounters[0] += 1
                else:
                    continue
            elif state == State.PULL_OUT:
                # check to see if we transition to accelerate
                if rand < [0.4, 0.6][scenario - 1]:
                    state = state.ACCELERATE
                    accelerate(scenario)
                    transitionCounters[1] += 1
                # check to see if we transition to pull in behind
                elif rand < [0.8, 0.8][scenario - 1]:
                    state = state.PULL_IN_BEHIND
                    pull_in_behind(scenario)
                    transitionCounters[3] += 1
                else:
                    continue
            elif state == State.ACCELERATE:
                if rand < [0.3, 0.3][scenario - 1]:
                    state = state.PULL_IN_AHEAD
                    pull_in_ahead(scenario)
                    transitionCounters[2] += 1
                elif rand < [0.6, 0.7][scenario - 1]:
                    state = state.DECELERATE
                    decelerate(scenario)
                    transitionCounters[5] += 1
                elif rand < [0.9, 0.9][scenario - 1]:
                    state = state.PULL_IN_BEHIND
                    pull_in_behind(scenario)
                    transitionCounters[4] += 1
                else:
                    continue
            elif state == State.PULL_IN_BEHIND:
                if rand < [0.8, 0.7][scenario - 1]:
                    state = state.FOLLOW
                    follow(scenario)
                    transitionCounters[6] += 1
                else:
                    continue
            elif state == State.DECELERATE:
                if rand < [0.8, 0.9][scenario - 1]:
                    state = state.PULL_IN_BEHIND
                    pull_in_behind(scenario)
                    transitionCounters[7] += 1
                else:
                    continue
            elif state == State.PULL_IN_AHEAD:
                if rand < [0.8, 0.7][scenario - 1]:
                    state = state.DONE
                    done(scenario)
                    transitionCounters[8] += 1
                    break
                else:
                    continue

    # List of global state counters
    stateCounters = [g_follow, g_pullOut, g_accelerate, g_pullInAhead, g_pullInBehind, g_decelerate, g_done]

    # Print out the number of times each state was entered
    print(f"\nscenario \t\t\t= {scenario}")
    print(f"trace \t\t\t\t= {bool(g_path)}")
    print(f"iterations \t\t\t= {iterations}")
    # print the transition probabilities used 
    print("transition probabilities \t=", end = "")  
    for probability in transitionProbabilites:
        print(f" {probability[scenario -1]}", end = "")
    #print the number of times each state was entered
    print("\nsate counts \t\t\t=", end = "")
    for stateCounter in stateCounters:
        print(f" {stateCounter}", end = "")
    # print the state frequencies
    print("\nstate frequencies \t\t=", end = "")
    for stateCounter in stateCounters:
        print(f" {round(stateCounter / sum(stateCounters), 3)}", end = "")
    # print the number of times each transition was taken
    print("\ntransition counts \t\t=", end = "")
    for transition in transitionCounters:
        print(f" {transition}", end = "")
    # print the transition frequencies
    print("\ntransition frequencies \t\t=", end = "")
    for transition in transitionCounters:
        print(f" {round(transition / sum(transitionCounters), 3)}", end = "")

    # print the path taken
    if g_path and scenario == 1:
        for iteration in g_path:
            print(f"iteration= {g_path.index(iteration)}")
            for state in iteration:
                print(f"{state}")

    # reset the global variables
    g_follow = 0
    g_pullOut = 0
    g_accelerate = 0
    g_pullInAhead = 0
    g_pullInBehind = 0
    g_decelerate = 0
    g_done = 0
    g_path = []



# Run the state machine
run(100, 1)
run(1000000, 2)
    