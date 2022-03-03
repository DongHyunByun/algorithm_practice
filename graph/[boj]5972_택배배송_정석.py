import heapq

N,M = map(int,input().split())

inf = 9876543210
dist = [inf for i in range(N+1)]

graph={i:[] for i in range(1,N+1)}

for i in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

pq = [(0,1)]

while(pq):
    now_cost, now_node = heapq.heappop(pq)

    if dist[now_node]<now_cost:
        continue

    if now_node==N:
        print(now_cost)
        break

    for to_node in graph[now_node]:
        next_node = to_node[0]
        add_cost = to_node[1]

        if now_cost+add_cost<dist[next_node]:
            dist[next_node] = now_cost+add_cost
            heapq.heappush(pq,(now_cost+add_cost,next_node))


