# 11779 복습
import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())    
    graph[a].append((b, cost))
    
start, end = map(int, input().split())

INF = int(1e9)
distance = [INF]*(n+1)
path = [[] for _ in range(n+1)]
path[start].append(start)

queue = [(0, start)]
heapq.heapify(queue) # 우선순위 큐


while queue:
    now_cost, now = heapq.heappop(queue)
    if now_cost > distance[now]:
        continue
    if now == start:
        distance[now] = 0 # start -> start : distance 0 
        
    for next, next_cost in graph[now]:
        path_cost = next_cost + now_cost
        if path_cost < distance[next]:
            distance[next] = path_cost # 새로운 비용으로 갱신한다. 
            heapq.heappush(queue, (path_cost, next))
            path[next] = []
            for i in path[now]:
                path[next].append(i)
            path[next].append(next)

print(distance[end])
print(len(path[end]))
print(' '.join(map(str, path[end])))
            