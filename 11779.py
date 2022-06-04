# 최소 비용 구하기 
import heapq

n = int(input()) # 도시의 개수 (node)
m = int(input()) # 버스의 개수 (edge)

INF = int(1e9)
graph = [[] for _ in range(n+1)]    
distance = [INF] * (n+1) # 최단 거리 저장
path = [[] for _ in range(n+1)] # 경로를 담을 배열 

for _ in range(m): # 버스의 정보 
    a, b, cost = map(int, input().split()) # a : 출발도시 -> b : 도착도시, cost
    graph[a].append((b, cost))
start, end = map(int, input().split()) # 출발도시 , 도착도시 
queue = [(0, start)] # (cost, 출발도시)
queue = heapq.heapify(queue) # 우선순위 큐 

distance[start] = 0 

while queue:
    now_cost, now = heapq.heappop(queue)
    if now_cost > distance[now]:
        continue
    
    for next, next_cost in graph[now]:
        temp_cost = next_cost + now_cost
        if temp_cost < distance[next]:
            distance[next] = temp_cost
            heapq.heappush(queue, (temp_cost, next))
            # path 가 갱신되었을 때 현재까지의 경로를 넣어준다. 
            path[next] = []
            for i in path[now]:
                path[next].append(i)
            path[next].append(next)
            
    
print(distance[start]) # 최소비용
print(len(path[end])) # 경로에 포함된 도시의 수 
print(' '.join(map(str, path[end]))) # 경로 출력하기 
