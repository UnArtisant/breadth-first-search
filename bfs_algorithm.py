from collections import deque
import re

def read_edges_from_file(filename):
    edges = []
    with open(filename, 'r') as file:
        content = file.read()
        matches = re.findall(r'\((\d+),(\d+)\)', content)
        for match in matches:
            u, v = map(int, match) 
            edges.append((u, v))
    return edges

def create_graph(edges):
    graph = {}
    for edge in edges:
        u, v = edge
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    return graph

def bfs(graph, s, visited, L):
    queue = deque()
    visited[s] = True
    queue.append(s)

    print(f"Starting BFS from node: {s}")
    while queue:
        current = queue.popleft()
        L.append(current)
        print(f"Visited node: {current}")
        
        for i in graph.get(current, []):
            if not visited[i]:
                visited[i] = True
                queue.append(i)
        print(f"Current queue: {list(queue)}")
        print("\nVisited array after BFS traversal:", visited)

def bfs_graph(graph):
    visited = {node: False for node in graph}
    L = []

    for i in graph:
        if not visited[i]:
            bfs(graph, i, visited, L)
    return L

graph = create_graph(read_edges_from_file('bfs.txt'))
bfs_order = bfs_graph(graph)
print("BFS Traversal Order:", bfs_order)

