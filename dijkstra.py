"""Алгоритм Дейкстры по поиску кратчайшего пути во взвешенном графе.
   Работает только с положительными весами ребер."""

from collections import deque

def add_edge(G, a, b, weight):
    """ Добавляем в граф ребро a - b с весом weight
    """
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

def read_graph():
    """ Cчитываем граф в виде строк "a b вес ребра"
    """
    M = int(input('Количество ребер?'))
    G = {}
    for i in range(M):
        a, b, weight = input('Ребро?').split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)  # дополнительно, если граф неориентированный
    return G

def dijkstra(G, start):
    """ Возвращает словарь кратчайших расстояний от вершины start до остальных (в пределах компоненты связности)
    """
    Q = deque()
    s = {}
    for key in G:
        s[key] = 1000
    s[start] = 0
    Q.append(start)
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if s[v] + G[v][u] < s[u]:
                s[u] = s[v] + G[v][u]
                Q.append(u)

    return s

def restore_path(G, start, finish, s_d):
    """ Возвращает список кратчайшего пути от start до finish
    """
    result = []
    current = finish
    while current != start:
        for n, w in G[current].items():
            if s_d[current] == s_d[n] + G[current][n]:
                result.append(current)
                current = n
                break
    result.append(start)
    return result[::-1]


G = read_graph()
start = input('С какой вершины начать?')
shortest_distances = dijkstra(G, start)
finish = input('До какой вершины путь?')
shortest_path = restore_path(G, start, finish, shortest_distances)
print(shortest_distances[finish])
print(shortest_path)
