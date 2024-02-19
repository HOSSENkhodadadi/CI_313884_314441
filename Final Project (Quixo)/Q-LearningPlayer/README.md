# Reinforcement Learning Quixo Agent with Q-learning

Please Note: There is an expected issue with this code that may affect its usability. Please refer to the detailed arised issues provided in the report.


This repository contains a Python implementation of a Quixo playing agent trained using Q-learning, a reinforcement learning technique. The agent learns to play Quixo by interacting with the environment and updating its action-value function based on rewards obtained from its actions.

## How it Works

The agent learns to play Quixo through an iterative process. Here's a brief overview of the steps involved:

1. Initialization: Initialize Q-values for all possible state-action pairs.

2. Game Simulation: Play Quixo games iteratively.

3. Exploration and Exploitation: During each step of the game, the agent decides whether to explore new actions randomly or exploit its current knowledge.

4. Reward Calculation: Assign rewards based on game outcomes (win, lose, or draw).

5. Q-value Update: Update Q-values using the reward obtained and the maximum Q-value for the next state.

6. Training Loop: Repeat the above steps for a specified number of iterations.

