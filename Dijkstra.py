# 다익스트라 최단 경로 알고리즘 

# 매번 거리가 가장 짧은 노드를 선택하는 것을 반복 : 그리디 알고리즘 

from concurrent.futures import InvalidStateError
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)] # graph의 정보를 담는 N개 길이의 리스트 
visited = [False]*(n+1)
distance = [INF]*(n+1) # 거리 정보 

def get_smallest_node():
    min_value = INF
    index = 0 
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i 
        return index 

# -> 이 부분을 heapq를 쓸 수 도 있지 않나 ???

def dijkstra(start):
    distance[start] = 0 # 시작 노드 start -> start : 0 
    visited[start] = True 
    
    # 시작 노드의 인접 노드들에 대해 최단 거리 계산 
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    # 시작 노드 제외한 n-1 개의 다른 노드들을 처리 
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for next in graph[now]:
            cost = distance[now] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost 
        
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("도달할 수 X")
    else:
        print(distance[i])