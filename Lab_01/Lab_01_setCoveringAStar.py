from random import random
from functools import reduce
import numpy as np
from queue import PriorityQueue
from collections import namedtuple

PROBLEM_SIZE = 15
NUM_SETS = 15
SETS = tuple(
    np.array([random() < 0.3 for _ in range(PROBLEM_SIZE)])
    for _ in range(NUM_SETS)
)

State = namedtuple('State', ['taken', 'not_taken'])


def goal_check(state):
    return np.all(reduce(
        np.logical_or,
        [SETS[i] for i in state.taken],
        np.array([False for _ in range(PROBLEM_SIZE)]),
    ))


def distance(state):
    return PROBLEM_SIZE - sum(
        reduce(
            np.logical_or,
            [SETS[i] for i in state.taken],
            np.array([False for _ in range(PROBLEM_SIZE)]),
        )
    )


def g_function(state):
    return len(state.taken)


def h_function(state):
    return distance(state)


def costFunction(state):
    return g_function(state) + h_function(state)


assert goal_check(
    State(set(range(NUM_SETS)), set())
), "Problem not solvable"

def optimizer():
    frontier = PriorityQueue()
    start_state = State(set(), set(range(NUM_SETS)))
    frontier.put((costFunction(start_state), start_state))
    visited_states = set()


    counter=0
    while not frontier.empty():
        counter += 1
        _, current_state = frontier.get()

        # Convert the current_state to a frozenset before adding it to visited_states
        current_state_frozen = (frozenset(current_state.taken), frozenset(current_state.not_taken))

        if current_state_frozen not in visited_states:
            visited_states.add(current_state_frozen)

            if goal_check(current_state):
                break

            for action in current_state.not_taken:
                new_state = State(
                    current_state.taken | {action},
                    current_state.not_taken - {action},
                )

                # Convert the new_state to a frozenset before checking for membership
                new_state_frozen = (frozenset(new_state.taken), frozenset(new_state.not_taken))
                if new_state_frozen not in visited_states:
                    frontier.put((costFunction(new_state), new_state))
    return counter

counter = optimizer()
print(counter)
#print(f"Solved in {counter:,} steps ({len(current_state.taken)} sets selected)")
#print("Selected sets:", current_state.taken)
