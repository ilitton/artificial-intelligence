# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def basic_search(problem, frontier):
  """Foundation for search algorithms
  
  Parameters
  ----------
  problem : SearchProblem obj
      Data structure with an initial state, goal state, successor states, and cost of actions
  
  frontier : container data object (Ex: stacks, queues, etc)
      The farthest path that has been explored. 
      State has a format of (location, action, parent)
  
  Returns
  -------
  : list of actions that reaches a goal
  """
  paths = {}
  # add initial state to frontier
  frontier.push((problem.getStartState(), None, None))
  first_flag = True
  
  while True:
      if frontier.isEmpty():
          return []
  
      node, action, parent = frontier.pop()
      
      if first_flag:
          paths[node] = []
          first_flag = False
      else:
          current_path = list(paths[parent])
          current_path.append(action)
          paths[node] = current_path
      
      if problem.isGoalState(node):
          return paths[node]
      
      successors = problem.getSuccessors(node)
      for successor, action, cost in successors:
          # check for not explored
          if successor not in paths:
              in_frontier = False
              # explore not in frontier
              for test_node, temp_1, temp_2 in frontier.list:
                  if successor == test_node:
                      in_frontier = True
              if not in_frontier:
                  frontier.push((successor, action, node))

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  Parameters
  ----------
  problem : SearchProblem obj
      Data structure with an initial state, goal state, successor states, and cost of actions
      State has the format (location, action, parent)
  
  Returns
  -------
  : list of actions that reaches a goal
  """
  frontier = util.Stack()
  return basic_search(problem, frontier)

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
    
  Parameters
  ----------
  problem : SearchProblem obj
        Data structure with an initial state, goal state, successor states, and cost of actions
        State has the format (location, action, parent)
  
  Returns
  -------
  : list of actions that reaches a goal
  """
  frontier = util.Queue()
  return basic_search(problem, frontier)
      
def uniformCostSearch(problem):
  """
  Search the node of least total cost first.
  
  Parameters
  ----------
  problem : SearchProblem obj
        Data structure with an initial state, goal state, successor states, and cost of actions
        State has the format (location, action, parent, step_cost)
  
  Returns
  -------
  : list of actions that reaches a goal
  """
  return aStarSearch(problem)

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  
  Parameters
  ----------
  state : 4-tuple
    (location, action, parent, step_cost)
    
  problem : SearchProblem obj
        Data structure with an initial state, goal state, successor states, and cost of actions
        State has the format (location, action, parent, step_cost)
    
  Returns
  -------
  : int
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  """Search the node that has the lowest combined cost and heuristic first.
  
  Parameters
  ----------
  problem : SearchProblem obj
      Data structure with an initial state, goal state, successor states, and cost of actions
      State has the format (location, action, parent, step_cost)
    
  heuristic : function
      Function to estimate cost from current state to goal
  
  Returns
  -------
  : list of actions that reaches a goal
  """
  paths = {}
  path_costs = {}
  
  frontier = util.PriorityQueue()
  # add initial state to frontier
  frontier.push((problem.getStartState(), None, None, 0), 0)
  first_flag = True
  
  # search first time path
  while True:
      if frontier.isEmpty():
          return []

      node, action, parent, step_cost = frontier.pop()
      if first_flag:
          paths[node] = []
          path_costs[node] = 0
          first_flag = False
      else:
          current_path = list(paths[parent])
          current_path.append(action)
          paths[node] = current_path
          path_costs[node] = path_costs[parent] + step_cost
      
      # check if goal is reached
      if problem.isGoalState(node):
          return paths[node]
      
      successors = problem.getSuccessors(node)
      for successor, action, cost in successors:
          # check for not explored
          if successor not in paths:
              # check if node is not in frontier and check cost - only keep lowest cost
              in_frontier = False
              for (index, (_, test_node)) in enumerate(frontier.heap):
                  if successor == test_node[0]:
                      in_frontier = True
                      # check if cost is lower
                      if path_costs[node] + cost < path_costs[test_node[2]] + test_node[3]:
                          del frontier.heap[index]
                          new_cost = path_costs[node] + cost + heuristic(successor, problem)
                          frontier.push((successor, action, node, step_cost), new_cost)
                               
              if not in_frontier: 
                  frontier.push((successor, action, node, cost),\
                      path_costs[node] + cost + heuristic(successor, problem))
        
          successors = problem.getSuccessors(node)
          for successor, action, cost in successors:
              if successor not in paths: #not explored
                  "check not in frontier, if is, check the cost, keep the lower cost"
                  isInFrontier = False
                  for (index, (priority, test_node)) in enumerate(frontier.heap):
                      if successor == test_node[0]:
                          isInFrontier = True
                          if path_costs[node] + cost < path_costs[test_node[2]] + test_node[3]:
                              del frontier.heap[index]
                              new_cost = path_costs[node] + cost + heuristic(successor, problem)
                              frontier.push((successor, action, node, step_cost), new_cost)
                            
                  if not isInFrontier:
                      new_cost = path_costs[node] + cost + heuristic(successor, problem)
                      frontier.push((successor, action, node, cost), new_cost)    
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
