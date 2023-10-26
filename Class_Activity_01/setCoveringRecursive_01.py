from random import random
import numpy as np
from collections import namedtuple

# Global variable to keep track of the nodes explored
node_counter = 0

def find_min_set_cover(universe, subsets, state, subset_indices):
    global node_counter
    node_counter += 1

    if not universe:
        return state

    if not subsets:
        return None

    chosen_subset = subsets[0]
    chosen_subset_index = subset_indices[0]

    state_with_chosen = find_min_set_cover(universe - chosen_subset, subsets[1:], state + [chosen_subset_index], subset_indices[1:])
    state_without_chosen = find_min_set_cover(universe, subsets[1:], state, subset_indices[1:])

    if state_with_chosen and state_without_chosen:
        if len(state_with_chosen) < len(state_without_chosen):
            return state_with_chosen
        else:
            return state_without_chosen
    elif state_with_chosen:
        return state_with_chosen
    else:
        return state_without_chosen

PROBLEM_SIZE = 10
NUM_SETS = 8
SETS = tuple(
    np.array([random() < 0.3 for _ in range(PROBLEM_SIZE)])
    for _ in range(NUM_SETS)
)
subset_indices = list(range(NUM_SETS))

# Generate the universe and subsets
universe = set(range(PROBLEM_SIZE))
subsets = [set([index for index, value in enumerate(s) if value]) for s in SETS]

result = find_min_set_cover(universe, subsets, [], subset_indices)

if result is not None:
    print("Minimum set covering:", result , "("+ str(len(result))+ " subsets selected)")
else:
    print("No valid set cover found.")

print("Nodes explored:", node_counter)
