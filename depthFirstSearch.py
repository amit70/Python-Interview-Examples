#DepthFirstSearch

def depthFirstSearch(graph,start):
    visited = []
    stack = [start]
    visited.append(start)

    while stack:
        currentnode = stack[-1]
        neighbours = graph[currentnode]
        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.append(neighbour)
                break
        else:
            stack.pop()
    return visited

graph = {1: [4],
         2: [3],
         3: [],
         4: [5],
         5: [],
         6: []}

print depthFirstSearch(graph,1)
