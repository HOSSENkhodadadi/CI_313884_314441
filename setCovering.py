# recursive solution for set covering problem

def solve_set_cover(universe, subsets):
    if not universe:
        return []
    if not subsets:
        return None

    # Choose the subset that covers the most elements
    best_subset = max(subsets, key=lambda subset: len(universe & subset))

    if not (universe & best_subset):
        return None

    remaining_universe = universe - best_subset
    remaining_subsets = [subset for subset in subsets if subset != best_subset]

    # Recursive call without the best subset
    solution = solve_set_cover(remaining_universe, remaining_subsets)
    if solution is not None:
        return [best_subset] + solution

    return None


# Example usage
universe = {1, 2, 3, 4, 5, 6}
subsets = [{1, 3}, {1, 2, 5}, {4, 6, 2, 5}]

result = solve_set_cover(universe, subsets)
print("Set Cover Solution:", result)