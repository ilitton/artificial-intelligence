# artificial-intelligence

This repository contains all my code for the
**[Udacity Artificial Intelligence Nanodegree](https://www.udacity.com/course/artificial-intelligence-nanodegree--nd889)** projects.

## Projects

<table style="width:105%">
  <tr>
    <th width="50%" height="50%">
      <p align="center">
           <a href="./sudoku_solver"><img src="./sudoku_solver/output/solve.gif" alt="Overview" width="75%" height="75%"></a>
           <br>Sudoku Solver</br>
      </p>
    </th>
    <th width="50%" height="50%">
      <p align="center">
           <a href="./isolation_agent"><img src="./isolation_agent/writeup/viz.gif" alt="Overview" width="95%" height="95%"></a>
           <br>Isolation Agent</br>
      </p>
   </th>
  </tr>
  <tr>
  	<th width="50%" height="50%">
  		<p align="center">
          <a href="./domain_independent_planner"><img src="./domain_independent_planner/writeup/images/viz.gif" alt="Overview" width="125% height="125%"></a>
          <br>Domain Independent Planner</br>
      </p>
    </th>
    <th width="50%" height="50%">
    	<p align="center">
          <a href="./sign_language_recognizer"><img src="./sign_language_recognizer/viz.gif" alt="Overview" width="125%" height="125%"></a>
          <br>Sign Language Recognizer</br>
      </p>
    </th>
  </tr>
</table>

## Labs

<table style="width:105%">
  <tr>
    <th width="33%" height="33%">
      <p align="center">
           <a href="./pacman_search"><img src="./pacman_search/pacman.gif" alt="Overview" width="200%" height="200%"></a>
           <br>Pac-Man Search</br>
      </p>
    </th>
    <th><p align="center">
           <a href="./simulated_annealing"><img src="./simulated_annealing/SA_animation.gif" alt="Overview" width="250%" height="250%"></a>
           <br>Simulated Annealing</br>
        </p>
   </th>
   <th><p align="center">
           <a href="./constraint_satisfaction"><img src="./constraint_satisfaction/EightQueens.gif" alt="Overview" width="200%" height="200%"></a>
           <br>Constraint Satisfaction</br>
        </p>
   </th>
  </tr>
</table>

## Table of Contents
### Projects:
#### [Sudoku Solver](./sudoku_solver)
 - **Summary:** Create a Sudoku-solving agent that can also solve a diagonal sudoku and the naked twins problem
 - **Keywords:** Constraint Propagation

#### [Isolation Agent](./isolation_agent)
 - **Summary:** Develop adversarial search agent to play the game "Isolation"
- **Keywords:** Adversarial Search, Minimax, Alpha Beta Pruning, Iterative Deepening Search

#### [Domain Independent Planner](./domain_independent_planner)
 - **Summary:** Build a planning search agent that solves deterministic logistics planning problems for an Air Cargo transport system
- **Keywords:** Planning Domain Definition Language (PDDL), Planning Graph Heuristics, A* Search

#### [Sign Language Recognizer](./sign_language_recognizer)
 - **Summary:** Build a system that can recognize words communicated using the American Sign Language (ASL)
- **Keywords:** Hidden Markov Models (HMMs)

### Labs:

#### [Pac-Man Search](./pacman_search)
 - **Summary:** Use BFS, DFS, and A* to teach Pac-Man to navigate his world in the most efficient way possible
- **Keywords:** Breadth First Search (BFS), Depth First Search (DFS), A* Search

#### [Simulated Annealing](./simulated_annealing)
 - **Summary:** Implement simulated annealing algorithm to solve the Traveling Salesman Problem (TSP) between US state capitals
- **Keywords:** Simulated Annealing

#### [Constraint Satisfaction](./constraint_satisfaction)
 - **Summary:** Solve the N-Queens constraint satisfaction problem using symbolic constraints and Backtracking-Search
- **Keywords:** Symbolic Constraints, Backtracking-Search

## Configure Environment

**Mac OS X**

1. `conda env create -f aind-environment-osx.yml` to create the environment.
then source activate aind to enter the environment.
2. Install the development version of hmmlearn 0.2.1 with a source build: `pip install git+https://github.com/hmmlearn/hmmlearn.git`

### Install PyGame
**Mac OS X**

1. Install [homebrew](https://brew.sh)
2. `brew install sdl sdl_image sdl_mixer sdl_ttf portmidi mercurial`
3. `source activate aind`
4. `pip install pygame`

Some users have reported that pygame is not properly initialized on OSX until you also run python -m pygame.tests.

---
Major thanks to [Andrea Palazzi](https://github.com/ndrplz) for letting me use his awesome README format! :)
