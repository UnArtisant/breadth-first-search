from collections import deque

def read_edges_from_file(filename):
    edges = []
    with open(filename, 'r') as file:
        for line in file:
            u, v = map(int, line.strip().split(','))
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

def bfs(list, s, visited):
    queue = deque()

    visited[s] = True
    queue.append(s)

    while len(queue) != 0:
        current = queue.popleft()
        print(current, end=" ")
        for i in list[current]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

def bfs_graph(list):
    visited= [False] * len(list)
    for i in range(len(list)):
        if visited[i] == False:
            bfs(list, i, visited)

graph = create_graph(read_edges_from_file('bfs.txt'))
bfs_graph(graph)
