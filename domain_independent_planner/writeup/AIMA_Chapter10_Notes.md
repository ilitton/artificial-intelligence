# Artificial Intelligence A Modern Approach (3rd Edition)
## Chapter 10: Classical Planning

* **Planning**: Devising a plan of action to achieve one's goals

* **Factored representation**: state of the world is represented by a collection of variables 

* **PDDL (Planning Domain Definition Language)**: language to express all 4*Tn*<sup>2</sup> actions with one action schema
	* Describes the four things needed to define a search problem:
		1. Initial state
		2. Actions that are available in a state 
		3. Result of applying an action
		4. Goal test 

* **Fluent**: aspect of the world that changes; synonymous for "state variable"
* **State**: conjunction of fluents that are ground, functionless atoms
* **Dabase semantics**: 
	* Closed world assumptions means that any fluents not mentioned are false
	* Unique names assumption means distinct states
* Fluents are _not_ allowed in a state:
	 * Non-grounded
	 * Negations
	 * Use a function
* **Actions**: Described by a set of action schemas that implicitly define the ACTIONS(_s_) and RESULT(_s, a_) functions
* A description of the action should:
	* Needs to say what changes and what stays the same as a result of the action
	* Should only mention \delta
	* Should specify the result of the action in terms of what changes
	* Should not mention all the objects that stay in place

* **Action schema**: representation of a set of ground (variable-free) actions and consists of
	* action name
	* list of all variables used in the schema
	* precondition
		*  defines the state in which the action can be executed
	* effect
		* defines the result of executing the action
	* any variable in effect must also appear in the precondition 

* **Applicable**: action _a_ is **applicable** in state _s_ if the precondition is satisfied by _s_
* **Prepositionalize**: Replace each action schema with a set of ground actions and then use a prepositional solver to find a solution
* **Result**: state _s'_ is the **result** of executing an action _a_ in state _s_ 
	* Represented by the set of fluents formed by starting with _s_:
		* Removing the fluents that appear as negative literals in the action's effects (**Delete list**)
		* Adding the fluents that are positive literals in the action's effects (**Add list**)

* **Initial state**: conjunction of ground atoms 
* **Goal**: precondition - conjunction of literals (pos or neg) that may contain variables 

* Defined planning as a search problem:
	* Initial state
	* ACTIONS function
	* RESULT function
	* Goal test