# Depth-first search

def dfs(v, g: dict):
    used.add(v)
    for neighbour in g[v]:
        if neighbour not in used:
            dfs(neighbour, g)


graph = {'A': {'B', 'C'}, 'B': {'A', 'D'}, 'C': {'A'}, 'D': {'B'}}
used = set()
counter_of_components = 0
for vertex in graph:
    if vertex not in used:
        dfs(vertex, graph)
        counter_of_components += 1
print(counter_of_components)
