import heapq,sys

INF=9876543210
alter = [1,0]

N,M = map(int,input().split())
graph={i:[] for i in range(1,N+1)}

for i in range(M):
    a,b,d = map(int,sys.stdin.readline().rstrip().split())

    graph[a].append((b,d))
    graph[b].append((a,d))

def dij_fox():
    dist = [INF for i in range(N + 1)]
    pq = []

    dist[1] = 0
    heapq.heappush(pq, (0, 1))

    while(pq):
        t,node = heapq.heappop(pq)
        # print(t,node)
        if dist[node] < t:
            continue

        for to_node,added_t in graph[node]:
            next_t = t+added_t
            if next_t < dist[to_node]:
                heapq.heappush(pq,(next_t,to_node))
                dist[to_node] = next_t

    return dist

def dij_wolf():
    dist = [[INF for j in range(N+1)] for i in range(N + 1)] #dist[i][j] : i그루터기를 j번째 방문했을때 최소거리
    pq = []

    dist[1][0] = 0
    heapq.heappush(pq, (0, 1, 0))

    while(pq):
        t,node,cnt = heapq.heappop(pq)
        # print(t,node)
        if cnt==N or dist[node][cnt] < t:
            continue

        for to_node,added_t in graph[node]:
            if cnt%2==0: #두배
                next_t = t+added_t/2
            else: #1/2배
                next_t = t+added_t*2
            if next_t < dist[to_node][cnt+1]:
                heapq.heappush(pq,(next_t,to_node,cnt+1))
                dist[to_node][cnt+1] = next_t

    return dist

def dij_wolf_v2():
    dist = [[INF for j in range(2)] for i in range(N + 1)] #dist[i][0]:i그루터기를 느리게도착, dist[i][1]:i그루터기를 빠르게도착
    pq = []

    dist[1][0] = 0
    heapq.heappush(pq, (0, 1, 0))

    while(pq):
        t,node,speed = heapq.heappop(pq)
        # print(t,node)
        if dist[node][speed] < t:
            continue

        for to_node,added_t in graph[node]:
            if speed==0: # 느리게도착(다음은 빠르게감)
                next_t = t+added_t/2
            else: # 빠르게도착(다음은 느리게감)
                next_t = t+added_t*2
            if next_t < dist[to_node][alter[speed]]:
                heapq.heappush(pq,(next_t,to_node,alter[speed]))
                dist[to_node][alter[speed]] = next_t

    return dist

dist_fox = dij_fox()
# print(dist_fox)

dist_wolf = dij_wolf_v2()
# for i in dist_wolf:
#     print(i)

ans=0
for i in range(1,N+1):
    if dist_fox[i]<min(dist_wolf[i]):
        ans+=1
print(ans)