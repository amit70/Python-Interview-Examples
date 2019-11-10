#breathFirstSearchShortestPath

def breathFirstSearchShortestPath(graph, start, end):
    # if start == end:
    #     return

    visited = []
    queue = [[start]]

    while queue:
        currentNode = queue.pop(0)
        node = currentNode[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbourNode in neighbours:
                new_path = list(currentNode)
                new_path.append(neighbourNode)
                queue.append(new_path)

                if neighbourNode == end:
                    print visited
                    return new_path

            visited.append(node)

    return "So sorry, but a connecting path doesn't exist :("


graph = {1: [4,2,3],
         2: [3],
         3: [],
         4: [5],
         5: [6],
         6: [5,1]}

print breathFirstSearchShortestPath(graph,1,6)
