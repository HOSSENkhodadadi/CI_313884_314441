# Quixo MinMax Strategy README
Please read the Usage section.
## Overview
This repository contains a Python implementation of a MinMax strategy for playing the game of Quixo. Quixo is a two-player abstract strategy board game where players take turns making moves to align five of their pieces either horizontally, vertically, or diagonally, or force their opponent to make an illegal move.

## Features
- MinMax algorithm with alpha-beta pruning for decision making.
- Adjustable depth parameter to control search depth.
- Customizable game evaluation function to assess the game state.
- Compatible with Python 3.x.

## Getting Started
### Prerequisites
- Python 3.x
- Basic understanding of Quixo game rules

### Installation
1. Clone or download the repository to your local machine.
2. Ensure you have Python 3.x installed.

### Usage
1. Integrate the `MinMaxPlayer` class into your Quixo game implementation.
2. Instantiate `MinMaxPlayer` with appropriate parameters (player ID and depth).
3. Set minmaxID = 0 if minimax_player is the first player put minmaxID = 0 otherwise minmaxID = 1
4. minimax_player = MinMaxPlayer(minmaxID, 3)
5. random_player = RandomPlayer()
5. Call the `make_move()` method of the `MinMaxPlayer` instance when it's the AI player's turn.

### Customization
- Adjust the depth parameter in the `MinMaxPlayer` constructor to control the depth of the MinMax search.
- Customize the game evaluation function according to your game dynamics.

## Implementation Details
- **`__init__(self, player_id, depth=3)`:** Initializes a MinMaxPlayer instance with the player ID and search depth.
- **`game_evaluation(self, game: Game)`:** Evaluates the current game state and assigns a score based on the outcome.
- **`get_possible_moves(self, game: Game, player_id: int)`:** Generates all possible moves for the current player.
- **`min_max(self, game, depth, alpha, beta, maximizing_player)`:** Implements the MinMax algorithm with alpha-beta pruning to find the best move.
- **`make_move(self, game: Game)`:** Invokes the MinMax algorithm to determine the best move for the AI player.

## Notes
- Ensure your Quixo game implementation provides necessary functionalities such as move validation, game state management, and winner determination.
- Adjust the MinMax parameters and game evaluation function according to your game dynamics for optimal performance.

## Contribution
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This implementation was inspired by the Quixo game and the MinMax algorithm.
