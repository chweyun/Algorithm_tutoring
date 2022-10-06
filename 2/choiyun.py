from collections import deque
import sys

input = sys.stdin.readline
node_num, edge_num, start_node = map(int,input().split())
graph = [[] for _ in range(node_num+1)]

for _ in range(edge_num):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for gra in graph:
    gra.sort()

dfs_visited = [False]*(node_num+1)
bfs_visited = [False]*(node_num+1)

def dfs(graph, start_node):
    dfs_visited[start_node] = True
    print(start_node, end=' ')
    for i in graph[start_node]:
        if not dfs_visited[i]:
            dfs(graph, i)


def bfs(graph, start_node):
    queue = deque([start_node])
    bfs_visited[start_node]=True
    while queue:
        next_node = queue.popleft()
        print(next_node, end=' ')
        for i in graph[next_node]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i]=True

dfs(graph, start_node)
print()
bfs(graph, start_node)