import math

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player based on the limit_opp_moves tactic.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return limit_opp_moves_heuristic(game, player)

def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player based on the defensive/move away tactic.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return defensive_heuristic(game, player)

def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player based on the offensive/move towards tactic.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return offensive_heuristic(game, player)

def custom_score_4(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player based on the manhattan distance heuristic.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return manhattan_dist_heuristic(game, player)

def custom_score_5(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player based on the euclidean distance heuristic.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return euclidean_dist_heuristic(game, player)

def limit_opp_moves_heuristic(game, player):
    """
    This heuristic prioritizes limiting the opponent's future moves. The
    evaluation function assigns a higher weight when the number of future
    moves for the opponent is low and assigns a lower weight otherwise.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_legal_moves = game.get_legal_moves(player)
    player_total_moves = len(player_legal_moves)

    for move in player_legal_moves:
        player_board = game.forecast_move(move)
        player_total_moves += len(player_board.get_legal_moves())

    opp_legal_moves = game.get_legal_moves(game.get_opponent(player))
    opp_total_moves = len(opp_legal_moves)

    for move in opp_legal_moves:
        opp_board = game.forecast_move(move)
        opp_total_moves += len(opp_board.get_legal_moves())

    # Multiply opp_total_moves by 2 to penalize when opp has more moves
    return float(player_total_moves - 2 * opp_total_moves)

def dist_heuristic_helper(game, player):
    '''
    This helper function calculates the difference between the number of moves
    and gets each of the players' location.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    move_diff : int
        Difference between each player's number of moves

    player_pos, opp_pos : (int, int)
        Board coordinates corresponding to a legal position
    '''
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    num_player_moves = len(game.get_legal_moves(player))
    num_opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    # calculate difference between number of moves and penalize by wt of 2 when
        # opp has more moves
    move_diff = num_player_moves - 2 * num_opp_moves

    # get player locations
    player_pos = game.get_player_location(player)
    opp_pos = game.get_player_location(game.get_opponent(player))

    return(move_diff, player_pos, opp_pos)

def manhattan_dist_heuristic(game, player):
    '''
    This heuristic focuses on the difference between the number of moves
    between the players normalized by their manhattan distance.

    The heuristic assigns a lower score when:
     * the number of future moves for the opponent is high
     * the distance between the players is large because it's harder to block
        the opponent's moves when they're far apart.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    '''
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    move_diff, player_pos, opp_pos = dist_heuristic_helper(game, player)

    manhattan_dist = abs(player_pos[0] - opp_pos[0]) + abs(player_pos[1] - opp_pos[1])

    try:
        heuristic_val = (float(move_diff/float(manhattan_dist)))
    except ZeroDivisionError:
        heuristic_val = 0
    return heuristic_val

def euclidean_dist_heuristic(game, player):
    '''
    This heuristic focuses on the difference between the number of moves between the players
    normalized by their euclidean distance.

    The heuristic assigns a lower score when:
     * the number of future moves for the opponent is high
     * the distance between the players is large because it's harder to block the opponent's moves
        when they're far apart.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    '''
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    move_diff, player_pos, opp_pos = dist_heuristic_helper(game, player)

    x_dist = (player_pos[0] - opp_pos[0])**2
    y_dist = (player_pos[1] - opp_pos[1])**2
    dist = math.sqrt(x_dist + y_dist)

    try:
        heuristic_val = float(move_diff)/float(dist)
    except ZeroDivisionError:
        heuristic_val = 0

    return heuristic_val

def defensive_heuristic(game, player):
    """
    Run away from opponent by maximizing the distance from the opponent. The
    heuristic assigns a larger score for larger differences.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_pos = game.get_player_location(player)
    opp_pos = game.get_player_location(game.get_opponent(player))

    return float(abs(sum(opp_pos) - sum(player_pos)))

def offensive_heuristic(game, player):
    """
    Move towards opponent by minimizing the distance from the opponent. The
    heuristic assigns a larger score for smaller differences.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_pos = game.get_player_location(player)
    opp_pos = game.get_player_location(game.get_opponent(player))

    return float(-abs(sum(opp_pos) - sum(player_pos)))

class IsolationPlayer:
    """
    Base class for minimax and alphabeta agents

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=4, score_fn=custom_score, timeout=20.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

class MinimaxPlayer(IsolationPlayer):
    """
    Game-playing agent that chooses a move using depth-limited minimax
    search
    """
    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left
        # Initialize the best move so that function returns something in case
            # the search fails
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()

        if not legal_moves:
            return best_move

        try:
            return self.minimax(game, self.search_depth)
        except SearchTimeout:
            # Return best move found so far when time runs out
            return best_move

    def terminal_test(self, game):
        """
        Return True if the game is over for the active player
        and False otherwise.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        Returns
        -------
         : boolean
            Flag for whether the game is over
        """
        return not bool(game.get_legal_moves())

    def check_time(self):
        """
        Check if time left is less than TIMER_THRESHOLD
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

    def min_value(self, game, depth):
        """
        Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            The list of coordinate pairs (row, column) of all legal moves
            for the player constrained by the current game state.

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        best_score : int
            Score assigned to the best move found in the current search
        """
        if self.terminal_test(game):
            return game.utility(self)

        if depth == 0:
            return self.score(game, self)

        best_score = float("inf")
        legal_moves = game.get_legal_moves()

        for m in legal_moves:
            self.check_time()
            new_game = game.forecast_move(m)
            current_score = self.max_value(new_game, depth-1)
            if current_score < best_score:
                best_score = current_score

        return best_score

    def max_value(self, game, depth):
        """
        Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            The list of coordinate pairs (row, column) of all legal moves
            for the player constrained by the current game state.

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        best_score : int
            Score assigned to the best move found in the current search
        """
        if self.terminal_test(game):
            return game.utility(self)

        if depth == 0:
            return self.score(game, self)

        best_score = float("-inf")
        legal_moves = game.get_legal_moves()

        for m in legal_moves:
            self.check_time()
            new_game = game.forecast_move(m)
            current_score = self.min_value(new_game, depth-1)
            if current_score > best_score:
                best_score = current_score

        return best_score

    def minimax(self, game, depth):
        """Depth-limited minimax search algorithm based on the
        MINIMAX-DECISION from AIMA
        (https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md)

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        self.best_move : (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        """
        self.check_time()

        legal_moves = game.get_legal_moves()

        if not legal_moves:
            return (-1, -1)

        best_score = float("-inf")
        self.best_move = legal_moves[0]

        for m in legal_moves:
            self.check_time()
            new_game = game.forecast_move(m)
            current_score = self.min_value(new_game, depth-1)
            if current_score > best_score:
                best_score = current_score
                self.best_move = m

        return self.best_move

class AlphaBetaPlayer(IsolationPlayer):
    """
    Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning.
    """
    def get_move(self, game, time_left):
        """
        Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        best_move : (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # initialize the best move to return something in case the search fails or times out
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()

        if not legal_moves:
            return best_move

        try:
            current_depth = 1
            while True:
                current_move = self.alphabeta(game, current_depth)

                if current_move != (-1, -1):
                    best_move = current_move

                current_depth += 1
                if self.time_left() < self.TIMER_THRESHOLD:
                    return best_move
        except SearchTimeout:
            # return best move found so far when time runs out
            return best_move

    def check_time(self):
        """
        Check if time left is less than TIMER_THRESHOLD
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

    def terminal_test(self, game):
        """
        Return True if the game is over for the active player
        and False otherwise.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        Returns
        -------
         : boolean
            Flag for whether the game is over
        """
        return not bool(game.get_legal_moves())

    def alphabeta_max_value(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """
        Alphabeta maximizer player. Returns the highest score/move tuple found
        in game. Prunes the search tree when possible.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        alpha : float
            Alpha limits the lower bound of search on minimizing layers
        """
        if depth == 0:
            return self.score(game, self)

        if self.terminal_test(game):
            return game.utility(self)

        legal_moves = game.get_legal_moves()
        legal_moves.sort()

        for m in legal_moves:
            self.check_time()
            new_game = game.forecast_move(m)
            current_score = self.alphabeta_min_value(new_game, depth-1, alpha, beta)
            if current_score > alpha:
                alpha = current_score
                if alpha >= beta:
                    break
        return alpha

    def alphabeta_min_value(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """
        Alphabeta minimizer player. Returns the lowest score/move tuple found
        in game. Prunes the search tree when possible.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        beta : float
            Beta limits the upper bound of search on maximizing layers
        """
        if depth == 0:
            return self.score(game, self)

        if self.terminal_test(game):
            return game.utility(self)

        legal_moves = game.get_legal_moves()
        legal_moves.sort()

        for m in legal_moves:
            self.check_time()
            new_game = game.forecast_move(m)
            current_score = self.alphabeta_max_value(new_game, depth-1, alpha, beta)
            if current_score < beta:
                beta = current_score
                if beta <= alpha:
                    break

        return beta

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """
        Depth-limited minimax search with alpha-beta pruning based on
        ALPHA-BETA-SEARCH from AIMA
        (https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md)

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        best_move : (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        """
        self.check_time()

        legal_moves = game.get_legal_moves()
        legal_moves.sort()

        if not legal_moves:
            return (-1, -1)

        best_move = legal_moves[0]

        for m in legal_moves:
            self.check_time()
            new_game = game.forecast_move(m)
            current_score = self.alphabeta_min_value(new_game, depth-1, alpha, beta)
            if current_score > alpha:
                alpha = current_score
                best_move = m
        return best_move
