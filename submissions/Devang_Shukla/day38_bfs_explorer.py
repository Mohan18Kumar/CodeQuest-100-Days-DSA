from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

def main():
    graph = {}
    n = int(input("Enter number of edges: "))
    print("Enter edges (format: node1 node2):")
    for _ in range(n):
        u, v = input().split()
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)  

    start_node = input("Enter starting node for BFS: ")
    bfs(graph, start_node)

if __name__ == "_main_":
    main()