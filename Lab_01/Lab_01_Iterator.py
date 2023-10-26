from Lab_01_setCoveringAStar import optimizer, goal_check, State, NUM_SETS, SETS
parameter_values = []
for _ in range(100):
    try:
        assert goal_check(State(set(range(NUM_SETS)), set())), "Problem not solvable"
        parameter_value = optimizer()
        parameter_values.append(parameter_value)
        is_problem_solvable = True  # Reset the flag
    except AssertionError as e:
        # Handle the AssertionError (problem not solvable)
        print(f"Assertion Error: {e}")
        is_problem_solvable = False

# Calculate the average of the parameter values
average_parameter = sum(parameter_values) / len(parameter_values)

# Print the average
print(f'Average Parameter Value: {average_parameter}')