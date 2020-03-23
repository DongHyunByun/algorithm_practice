import heapq

#input
N,M,X=map(int,input().split())
graph={}
graphR={}
for i in range(1,N+1):
    graph[i]=[]
    graphR[i]=[]
for i in range(M):
    a,b,cost=map(int,input().split())
    graph[a].append([b,cost])
    graphR[b].append([a,cost])
maxNum=10000000
nodeDist=[maxNum for node in range(N+1)]
nodeDistR=[maxNum for node in range(N+1)]

def dijkstra(nodeDist,graph):
    dij=[[0,X]]
    nodeDist[X]=0
    heapq.heapify(dij)
    while(dij):
        temp=heapq.heappop(dij)
        nowCost=temp[0]
        nowNode=temp[1]
        # 이미방문되었으면 통과해(첫방문이 최솟값임이 보장됨)
        if nodeDist[nowNode]!=nowCost:
            continue
        for toNode,toCost in graph[nowNode]:
            if nowCost+toCost<nodeDist[toNode]:
                nodeDist[toNode]=nowCost+toCost
                heapq.heappush(dij,[nodeDist[toNode],toNode])

#역방향(각 마을에서 X까지의 최단거리)
dijkstra(nodeDistR,graphR)
#순방향(4에서 각최단거리)
dijkstra(nodeDist,graph)
#합
dist=[nodeDistR[i]+nodeDist[i] for i in range(1,N+1)]
print(max(dist))