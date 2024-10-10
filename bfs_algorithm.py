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

def bfs(list, s, visited):
    queue = deque()

    visited[s] = True
    queue.append(s)

    while len(queue) != 0:
        current = queue.popleft()
        print(current, end=" ")
        for i in list.get(current, []):
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

    print("\nQueue: " + str(list))
    print("\nArray A: " + str(visited))

def bfs_graph(list):
    visited= {node: False for node in list}
    for i in list:
        if visited[i] == False:
            bfs(list, i, visited)

graph = create_graph(read_edges_from_file('bfs.txt'))
bfs_graph(graph)
