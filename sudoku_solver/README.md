# Diagonal Sudoku Solver Project

### Demo:
<div style="text-align:center"><img src="./output/solve.gif" width="50%" height="50%"/></div> 

### Goal:

* Develop Sudoku-solving agent to solve *diagonal* Sudoku puzzles and the *naked twin* problem

### Repo Structure: 
* [`utils.py`](utils.py): utility functions to create sudoku board
* [`solution.py`](solution.py): functions to solve a game
* [`PySudoku.py`](PySudoku.py): code for visualizing solution
* [`visualize.py`](visualize.py): code for visualizing solution
* [`./objects/`](./objects/): necessary classes to create sudoku board
* [`./output/`](./output/): directory containing images for writeup
* [`./tests/`](./tests/): testcases
 * `./tests/test_solution.py` - Test solution by running `python -m unittest`

### Dependencies

This project requires **Python 3**.

Recommended install: [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 

##### Optional: Pygame

Please see how to download pygame [here](http://www.pygame.org/download.shtml).

---

## Terminology

![Alt text](./output/peers.png "Figure 1. Terminology Example")
**Figure 1. Example Sudoku Boards**

* **Boxes**: individual squares (81 in total)
 * Ex: 'A1', 'A2', etc. 
* **Units**: Complete rows, columns, and 3x3 squares. Each unit is a set of 9 boxes. (27 in total)
 * Ex: Each blue highlighted boxes in Figure 1
* **Peers**: All other boxes that belong to the same row, column, 3x3 square as a certain box. Each box will have 20 total peers.
 * Ex: Each board in Figure 1 shows a different peer for 'E3' 

## Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Constrain propagation was used as followed:

<img src="./output/naked-twins.png" alt="Overview" width="50%" height="50%">

**Figure 2. Example of Naked Twins Board**

* Find all boxes in the same unit with the same two possible values
 * In Figure 1, this means identifying that 'F3' and 'I3' are naked twins because they both have '23' as their values and are within the same unit
* If these boxes share the same two values, all the other boxes in their unit cannot have this value as a possible solution
 * This means 'D3' and 'E3' cannot have '23' in their values 
* The identical values can be eliminated from the other boxes in the naken twin units.
 * Remove '23' from 'D3' and '3' from 'E3' 

Eliminating the twin values reduces the search space which creates a board closer to the solution.

## Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The diagonals are added as units and follow the same rules applied to the other units (rows, columns, 3x3 squares) - the digits 1-9 can only appear once in every box within the unit. Therefore, the strategies (ex: eliminate, only choice, naked twins) will not change but will have two more constraints to follow. 