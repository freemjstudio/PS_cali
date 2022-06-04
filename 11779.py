# 최소 비용 구하기 
# 다익스트라 최단 경로 알고리즘 

n = int(input()) # 도시의 개수 (node)
m = int(input()) # 버스의 개수 (edge)

INF = int(1e9)
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) # 방문 여부 표시 
distance = [INF] * (n+1) # 최단 거리 저장
for _ in range(m): # 버스의 정보 
    a, b, cost = map(int, input().split()) # a : 출발도시 -> b : 도착도시, cost
    graph[a].append((b, cost))
    
start, end = map(int, input().split()) # 출발도시 , 도착도시 

    