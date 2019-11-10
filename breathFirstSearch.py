#BreadthFirstSearch

from collections import deque
def breadthFirstSearch(graph, start):

    visited = []
    queue = deque()
    queue.appendleft(start)
    while queue:
        currentNode = queue.popleft()
        if currentNode not in visited:
            visited.append(currentNode)
            neighbours = graph[currentNode]
            for neighboursNode in neighbours:
                queue.append(neighboursNode)
    return visited

graph = {1: [4],
         2: [3],
         3: [],
         4: [5],
         5: [],
         6: []}

print breadthFirstSearch(graph,1)
