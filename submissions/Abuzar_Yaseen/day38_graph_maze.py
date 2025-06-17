def bfs(graph,start):
    visited = []
    to_visit = [start]
    while to_visit:
        current = to_visit.pop(0)
        if current not in visited:
            visited.append(current)
            for neighbour in graph[current] :
                if neighbour not in visited:
                    to_visit.append(neighbour) 
    return visited  

graph = {
    'A': ['B','C'],
    'B':[],
    'C':[]

}

result = bfs(graph,'A')
print(' '.join(result))