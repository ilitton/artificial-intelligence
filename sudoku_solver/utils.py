def cross(A, B):
    """
    Cross product of elements in A and elements in B

    Parameters
    ----------
    A, B: : list of strs

    Returns
    -------
    : list
    """
    return [s+t for s in A for t in B]

def display(values):
    """
    Display the values as a 2-D grid.

    Parameters
    ----------
    values : dict where key: str, value: str
        Dict representing board where key is a row/column index identifying box
         and value is the possible number(s)
        Ex: {'A1': '123', 'A2': '456', etc}
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF':
            print(line)
    return

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
diagonal_units = [[x+y for x, y in zip(rows, cols)], [x+y for x, y in zip(rows, cols[::-1])]]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], []))-set([s])) for s in boxes)
