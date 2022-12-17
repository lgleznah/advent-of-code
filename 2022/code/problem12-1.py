import copy
import queue

class Action:

    def __init__(self, move):
        self.move = move

class State:

    def __init__(self, pos):
        self.pos = pos

    def __eq__(self, state):
        return self.pos == state.pos

    def __hash__(self):
        return hash(self.pos)

    def applyAction(self, action):
        st = copy.deepcopy(self)
        
        if (action.move == "UP"):
            st.pos = (st.pos[0]-1,st.pos[1])
        elif (action.move == "DOWN"):
            st.pos = (st.pos[0]+1,st.pos[1])
        elif (action.move == "RIGHT"):
            st.pos = (st.pos[0],st.pos[1]+1)
        elif (action.move == "LEFT"):
            st.pos = (st.pos[0],st.pos[1]-1)
        
        return st

class Node:
    def __init__(self, state, parent, action):
        self.state = state # Must be State Class
        self.parent = parent # Must be Node Class
        self.action = action # Must be Action Class
        self.depth = 0
        self.gCost, self.hCost, self.fCost = 0.0, 0.0, 0.0

class Problem:

    actions = ["UP", "DOWN", "RIGHT", "LEFT"]

    def __init__(self, filename):

        with open(filename, 'r') as file:
            self.maze = [[ord(character) - 96 for character in line.strip()] for line in file.readlines()]
        
        self.list_lowest = []

        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                if self.maze[row][col] == -13:
                    self.initialState = State((row, col))
                    self.maze[row][col] = 1
                    self.list_lowest.append((row, col))
                elif self.maze[row][col] == -27:
                    self.goal = (row, col)
                    self.maze[row][col] = 26
                elif self.maze[row][col] == 1:
                    self.list_lowest.append((row, col))

        self.rows = len(self.maze)
        self.cols = len(self.maze[0])


    def getInitialState(self):
        return self.initialState

    def getActions(self):
        return self.actions

    def isGoal(self, st):
        '''
        check if the given state is final or not
        '''
        return st.pos == self.goal
    
    def computeHeuristic(self,st):
        '''
        Compute and return the heuristic cost from the state 'st' to the 'goal state'.
        @param st the state
        @param heuristic is the name of the heuristic to use, useful if more than one is implemented 
        '''
        st_pos = st.pos
        goal = self.goal

        return abs(st_pos[0] - goal[0]) + abs(st_pos[1] - goal[1])

class Search():

    def __init__(self,problem):
        self.problem = problem
        self.open = queue.PriorityQueue() # TODO: declare self.open as a priority queue
        self.closed = set()

        self.generatedNodes = 0
        self.expandedNodes = 0
        self.exploredMaxSize = 0
        self.openMaxSize = 0

    def insertNode(self, node):
        self.open.put((node.fCost, self.generatedNodes, node))

    def getSuccesors(self, node):

        suc = []
        
        actions = self.problem.getActions()

        rows = self.problem.rows
        cols = self.problem.cols
        pos = node.state.pos
        maze = self.problem.maze
        
        row = pos[0]
        col = pos[1]

        for a in range(len(actions)):
            act = None
            # Action UP
            if ((actions[a] == "UP") and (row > 0) and (maze[row-1][col] <= 1 + maze[row][col])):
                act = Action("UP")
            # Action DOWN
            if ((actions[a] == "DOWN") and (row < (rows-1)) and (maze[row+1][col] <= 1 + maze[row][col])):
                act = Action("DOWN")
            # Action RIGHT
            if ((actions[a] == "RIGHT") and (col < (cols-1)) and (maze[row][col+1] <= 1 + maze[row][col])):
                act = Action("RIGHT")
            # Action LEFT
            if ((actions[a] == "LEFT") and (col > 0) and (maze[row][col-1] <= 1 + maze[row][col])):
                act = Action("LEFT")
            if (act != None):
                # Create a new node
                newState = node.state.applyAction(act)
                newNode = Node(newState, node, act)
                newNode.depth = node.depth + 1
                newNode.gCost = node.gCost + 1
                newNode.hCost = self.problem.computeHeuristic(newNode.state)
                newNode.fCost = newNode.gCost + newNode.hCost
                 
                suc.append(newNode)

        if (len(suc) > 0):
            self.expandedNodes +=1
        
        return suc


    def doSearch(self, treeSearch=False):

        # Initial node
        initNode = Node(self.problem.getInitialState(), None, None)
        initNode.gCost = 0.0
        initNode.hCost = self.problem.computeHeuristic(self.problem.getInitialState())
        initNode.fCost = initNode.gCost + initNode.hCost
        self.insertNode(initNode)
        
        self.generatedNodes += 1
        
        finish = False
        
        while (not self.open.empty() and not finish):  
            current = self.open.get()[2]
        
            if (self.problem.isGoal(current.state)):
                finish = True
            
            elif not(current.state in self.closed):
                self.closed.add(current.state)
                # Generate successors
                children = self.getSuccesors(current)
                for node in children:
                    self.insertNode(node)
                    self.generatedNodes += 1
        
        if (finish):
            return current.depth

def main():
    problem = Problem("../inputs/input12")
    list_lowest = problem.list_lowest
    min_depth = 99999999999

    for num, lowest in enumerate(list_lowest):
        print(f"Running search {num} of {len(list_lowest)}", end='\r')
        problem.initialState = State(lowest)
        searcher = Search(problem)
        result_depth = searcher.doSearch()
        min_depth = min(min_depth, 99999999999 if result_depth is None else result_depth)

    print(f'\n{min_depth}')

if __name__ == "__main__":
    main()