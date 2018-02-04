from itertools import combinations
from utils import *

assignments = []

def assign_value(values, box, value):
    """
    Assigns a value to a given box

    Parameters
    ----------
    values : dict where key: str, value: str
        Dict representing board where key is a row/column index identifying box and value is the
            possible number(s)
        Ex: {'A1': '123', 'A2': '456', etc}

    box : str
        Row/column index identifying box on a board
        Ex: 'A1', 'A2', etc

    value : str
        Possible number for box

    Returns
    -------
    values : dict where key: str, value: str
        Dict representing sudoku board with some values replaced
    """
    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def find_twin_units(possible_twins):
    """Find units of naked twin boxes

    Parameters
    ----------
    possible_twins : set of strs
        Set of boxes that are possible naked twins (have two possible numbers)

    Returns
    -------
    twin_units : list of str
        List of boxes from the same units as the naked twin boxes
    """
    # Create all pair combinations from list of potential twins
    pairs = combinations(possible_twins, 2)
    twin_units = list()

    for pair in pairs:
        # Find all units corresponding to one box of the pair
        pair_units = units[pair[1]]
        # Add unit to list if the pair belong to the same unit
        twin_units.append([box for unit in pair_units for box in unit if pair[0] in unit])

    # Remove any duplicate boxes
    twin_units = list(set([box for unit in twin_units for box in unit]))
    return twin_units

def naked_twins(values):
    """
    Eliminate values using the naked twins strategy.

    Parameters
    ----------
    values : dict where key: str, value: str
        Dict representing board where key is a row/column index identifying box and value is the
            possible number(s)
        Ex: {'A1': '123', 'A2': '456', etc}

    Returns
    -------
    values : dict where key: str, value: str
        Dict representing resulting sudoku board with the naked twins eliminated from peers
    """
    no_more_twins = False
    # while loop is used because new twins might be uncovered when possible values are removed
        # from peers
    while not no_more_twins:
        board_before = values
        # Iterate through all units until no more twins are found
        for units in unitlist:
            # Create dict where key is digits and value is units related to twin box
            possible_twins_dict = dict()
            for box in units:
                # If length of digits is 2 add units to dict of possible twins
                if len(values[box]) == 2:
                    if values[box] not in possible_twins_dict:
                        possible_twins_dict[values[box]] = list()
                    possible_twins_dict[values[box]].append(units)

                    # If length of list of units is 2, a twin set is found
                    if len(possible_twins_dict[values[box]]) == 2:
                        # Remove any duplicate units
                        possible_twins_dict[values[box]] = [list(x) for x in set(tuple(x)\
                                                            for x in\
                                                            possible_twins_dict[values[box]])]
                        # Iterate through all units of twins
                        for twin_units in possible_twins_dict[values[box]]:
                            for peer in twin_units:
                                # For each box in the unit which is not one of the two twins
                                    # remove the possible values
                                if box != peer:
                                    if values[peer] != values[box]:
                                        assign_value(values, peer,\
                                            values[peer].replace(values[box][0], ''))
                                        assign_value(values, peer,\
                                            values[peer].replace(values[box][1], ''))

        board_after = values
        # if boards before and after naked twin detection are the same then there are no more
            # twins thus we end the while loop
        if board_before == board_after:
            no_more_twins = True
    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.

    Parameters
    ----------
    grid: str
        A grid in string form.

    Returns
    --------
    : dict where key: str, value: str
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value
                will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from
        the values of all its peers.

    Parameters
    ----------
    values : dict where key: str, value: str
        Dict representing board where key is a row/column index identifying box and value is the
            possible number(s)
        Ex: {'A1': '123', 'A2': '456', etc}

    Returns
    -------
    values : dict where key: str, value: str
        Dict representing sudoku board with some values eliminated
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            assign_value(values, peer, values[peer].replace(digit, ''))
    return values

def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box,
    assign the value to this box.

    Parameters
    ----------
    values : dict where key: str, value: str
        Dict representing board where key is a row/column index identifying box and value is the
            possible number(s)
        Ex: {'A1': '123', 'A2': '456', etc}

    Returns
    --------
    values : dict where key: str, value: str
        Dict representing resulting sudoku board with only choice values assigned
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available
        values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.

    Parameters
    ----------
    values : dict where key: str, value: str
        Dict representing board where key is a row/column index identifying box and value is the
            possible number(s)
        Ex: {'A1': '123', 'A2': '456', etc}

    Returns
    -------
    values : dict where key: str, value: str
        Dict representing sudoku board with as much as the puzzle solved with eliminate and
            only_choice strategies
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    """
    Using depth-first search and propagation, create a search tree and solve the sudoku.

    Parameters
    ----------
    values : dict where key: str, value: str
        Dict representing board where key is a row/column index identifying box and value is the
            possible number(s)
        Ex: {'A1': '123', 'A2': '456', etc}

    Returns
    -------
    values : dict where key: str, value: str
        Dict representing attempted sudoku board
    """
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    unfilled_squares = {k:v for k, v in values.items() if len(v) > 1}
    root = min(unfilled_squares.items(), key=lambda x: len(x[1]))[0]
    # Now use recurrence to solve each one of the resulting sudokus
    for value in values[root]:
        new_sudoku = values.copy()
        new_sudoku[root] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.

    Parameters
    ----------
    grid : str
        String representing a sudoku grid
        Ex: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
    solved: dict
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))

if __name__ == '__main__':
    diag_sudoku_grid =\
        '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    print('\n')
    test = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
    display(solve(test))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
