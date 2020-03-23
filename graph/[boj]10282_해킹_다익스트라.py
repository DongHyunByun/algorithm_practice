import heapq
import sys
INF=9876543210

T=int(input())
for t in range(T):
    n,d,c=map(int,sys.stdin.readline().rstrip().split())
    graph={}
    for i in range(1,n+1):
        graph[i]=[]
    for _ in range(d):
        a,b,s=map(int,sys.stdin.readline().rstrip().split())
        graph[b].append([a,s])

    #다익스트라시작
    nodeDist=[INF for i in range(n+1)]
    dij=[[0,c]]
    nodeDist[c]=0
    nodeNum=0
    time=0
    while(dij):
        nowCost,nowNode=heapq.heappop(dij)
        if nodeDist[nowNode]<nowCost:
            continue
        nodeNum+=1
        time=nowCost
        for conNode,added in graph[nowNode]:
            temp=nowCost+added
            if temp<nodeDist[conNode]:
                nodeDist[conNode]=temp
                heapq.heappush(dij,[temp,conNode])
    print(nodeNum,time)