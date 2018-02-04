# Build a Game-playing Agent

### Demo:
<div style="text-align:center"><img src="./writeup/viz.gif" width="50%" height="50%"/></div> 

### Goal:

* Develop adversarial search agent to play the game [Isolation](#BackgroundInformation) with:
  * Minimax 
  * Alpha-beta pruning
  * iterative deepning search
  * Custom heuristics
* Outperform `ID_Improved` player in the tournament

### Repo Structure: 
* [`game_agent.py`](game_agent.py): heuristic functions to play the game
* [`agent_test`](agent_test.py): test cases for heuristic functions
* [`sample_players.py`](sample_players.py): provided [player classes](#TournamentOpponents) to play against agent
* [`tournament.py`](tournament.py): script to evaluate the effectiveness of custom heuristics. To learn more about the tournamet, please click [here](#Tournament).
* [`./isolation/`](./isolation/): directory for Python implementation of [Isolation](#BackgroundInformation)
* [`./iso_viz/`](./iso_viz/): contains a modified version of chessboard.js that can animate games played on a 7x7 board. To learn more, please click [here](#GameVisualization).
* [`./writeup/`](./writeup/): heuristic analysis and images for the writeup
* [`./research_review/`](./research_review/): Review of [Mastering the game of Go with deep neural networks and tree search](https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf)

### Dependencies

This project requires **Python 3**.

Recommended install: [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 

---

## <a name="BackgroundInformation"></a>Background Information

Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board.  Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game.  The first player with no remaining legal moves loses, and the opponent is declared the winner.  These rules are implemented in the `isolation.Board` class provided in the repository. 

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a rectangular grid (like a chess or checkerboard).  The agents can move to any open cell on the board that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. Movements are blocked at the edges of the board (the board does not wrap around), however, the player can "jump" blocked or occupied spaces (just like a knight in chess).

Additionally, agents will have a fixed time limit each turn to search for the best move and respond.  If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins. 

## <a name="Tournament"></a>Tournament

The `tournament.py` script is used to evaluate the effectiveness of my custom heuristics.  The script measures relative performance of my agent (named "Student" in the tournament) in a round-robin tournament against several other pre-defined agents.  The Student agent uses time-limited Iterative Deepening along with my custom heuristics.

The performance of time-limited iterative deepening search is hardware dependent (faster hardware is expected to search deeper than slower hardware in the same amount of time). The script controls for these effects by also measuring the baseline performance of an agent called "ID_Improved" that uses Iterative Deepening and the improved_score heuristic defined in `sample_players.py`.

#### <a name="TournamentOpponents"></a>Tournament Opponents

- Random: An agent that randomly chooses a move each turn.
- MM\_Open: MinimaxPlayer agent using the open\_move\_score heuristic with search depth 3
- MM\_Center: MinimaxPlayer agent using the center\_score heuristic with search depth 3
- MM\_Improved: MinimaxPlayer agent using the improved\_score heuristic with search depth 3
- AB\_Open: AlphaBetaPlayer using iterative deepening alpha-beta search and the open_move_score heuristic
- AB\_Center: AlphaBetaPlayer using iterative deepening alpha-beta search and the center_score heuristic
- AB\_Improved: AlphaBetaPlayer using iterative deepening alpha-beta search and the improved\_score heuristic

## <a name="GameVisualization"></a>Game Visualization

In order to use the board, you must run a local webserver by running `python -m http.server 8000` from your project directory (you can replace 8000 with another port number if that one is unavailable), then open your browser to `http://localhost:8000` and navigate to the `/isoviz/display.html` page.  Enter the move history of an isolation match (i.e., the array returned by the Board.play() method) into the text area and run the match.  Refresh the page to run a different game. 