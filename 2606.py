# 2602 바이러스 
from collections import deque 

n = int(input()) # 컴퓨터의 수 
e = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 인접 노드를 그래프로 표시하기 
    graph[b].append(a) # 그래프는 양방향 그래프!! 

result = 0 

def bfs(start):
    global result 
    queue = deque() # 덱으로 풀기 !! 
    queue.append(start)

    while queue:
        now = queue.pop()
        visited[now] = True 

        for i in graph[now]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                result += 1
bfs(1)
print(result)
            


