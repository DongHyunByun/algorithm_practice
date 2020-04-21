import heapq
import sys
INF=9876543210
n,m,k=map(int,input().split())
graph={}
for i in range(n+1):
    graph[i]=[]
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().rstrip().split())
    graph[a].append([b,c])

kDist=[[] for i in range(n+1)]
kDist[1].append(0)
nodeDist=[INF for i in range(n+1)]
dij=[[0,1]]
while(dij):
    nowCost,nowNode=heapq.heappop(dij)
    for toNode,addedCost in graph[nowNode]:
        toCost=nowCost+addedCost
        if len(kDist[toNode])<k:
            heapq.heappush(kDist[toNode],-toCost)
            heapq.heappush(dij,[toCost,toNode])
        elif kDist[toNode][0]<-toCost:
            heapq.heappop(kDist[toNode])
            heapq.heappush(kDist[toNode],-toCost)
            heapq.heappush(dij,[toCost,toNode])

for i in range(1,n+1):
    if len(kDist[i])!=k:
        print(-1)
    else:
        print(-kDist[i][0])