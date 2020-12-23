import heapq
INF=9876543210

N,M=map(int,input().split())

graph={}
for i in range(1,N+1):
    graph[i]=[]

for i in range(N-1):
    a,b,cost=map(int,input().split())
    graph[a].append([b,cost])
    graph[b].append([a,cost])

def dijstra(start,fin):
    dist=[INF for i in range(N+1)]
    dist[start]=0
    dij=[[0,start]]

    while(dij):
        nowCost,nowNode=heapq.heappop(dij)
        if nowNode==fin:
            return nowCost
        if dist[nowNode]<nowCost:
            continue

        for toNode,addedCost in graph[nowNode]:
            newCost=nowCost+addedCost
            if newCost<dist[toNode]:
                dist[toNode]=newCost
                heapq.heappush(dij,[newCost,toNode])


for i in range(M):
    a,b=map(int,input().split())
    print(dijstra(a,b))
