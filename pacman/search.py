# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Na busca em profundidade viajamos "de galho em galho", navegando até um nó folha antes de seguir para o proximo
    # Para isso usamos uma Fila (First in first out)
    no = util.Queue()

    nos_visitados = []
    # Faremos uma lista de ações para registrar a direção seguida
    lista_de_acoes = []
    # Place the starting point in the stack
    no.push((problem.getStartState(), lista_de_acoes))
    while no:
        no, direcao = no.pop()
        if not no in nos_visitados:
            nos_visitados.append(no)
            if problem.isGoalState(no):
                return direcao
            for successor in problem.getSuccessors(no):
                coordinate, direction, cost = successor
                nextActions = direcao + [direction]
                no.push((coordinate, nextActions))
    return []
    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    # Na busca em largura navegamos por todos os nós de um mesmo nível antes de seguir para o proximo
    # Raiz - direita - esquerda, ou seja, lendo a árvore em Pilha
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    no = util.Stack()

    nos_visitados = []
    # Faremos uma lista de ações para registrar a direção seguida
    lista_de_acoes = []
    # Place the starting point in the stack
    no.push((problem.getStartState(), lista_de_acoes))
    while no:
        no, direcao = no.pop()
        if not no in nos_visitados:
            nos_visitados.append(no)
            if problem.isGoalState(no):
                return direcao
            for successor in problem.getSuccessors(no):
                coordinate, direction, cost = successor
                nextActions = direcao + [direction]
                no.push((coordinate, nextActions))
    return []
    # util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Na busca por custo uniforme utilizamos a soma dos custos de veiagem até cada nó em nossa estimativa
    # Para isso utilizamos uma fila com prioridade e damos prioridade a quem tiver o menor custo
    no = util.PriorityQueue()
    nos_visitados = []
    lista_de_acoes = []
    no.push((problem.getStartState(), lista_de_acoes), problem)
    while no:
        node, acoes = no.pop()
        if not node in nos_visitados:
            nos_visitados.append(node)
            if problem.isGoalState(node):
                return acoes
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = acoes + [direction]
                nextCost = problem.getCostOfActions(nextActions)
                no.push((coordinate, nextActions), nextCost)
    return []
    # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Use a priority queue, so the cost of actions is calculated with a provided heuristic
    no = util.PriorityQueue()
    # Make an empty list of explored nodes
    nos_visitados = []
    # Make an empty list of actions
    lista_de_acoes = []
    # Place the starting point in the priority queue
    no.push((problem.getStartState(), lista_de_acoes),
            heuristic(problem.getStartState(), problem))
    while no:
        node, acoes = no.pop()
        if not node in nos_visitados:
            nos_visitados.append(node)
            if problem.isGoalState(node):
                return acoes
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = acoes + [direction]
                nextCost = problem.getCostOfActions(nextActions) + \
                    heuristic(coordinate, problem)
                no.push((coordinate, nextActions), nextCost)
    return []
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
