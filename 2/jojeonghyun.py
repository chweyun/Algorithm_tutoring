from collections import deque
n, m, v = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def bfs(v):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        
        for i in range(len(matrix[x])):
            if matrix[x][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True
                
    
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    
    for i in range(len(matrix[v])):
        if visited[i] == False and matrix[v][i] == 1:
            dfs(i)

dfs(v)
visited = [False] * (n+1) # DFS를 한 번 실행하고 나면 visited가 모두 True로 바뀌기 때문에 수정해줌
print()
bfs(v)
