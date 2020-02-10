import heapq

N=int(input())
M=int(input())
graph={}
for i in range(N):
    graph[i+1]=[]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
start,end=map(int,input().split())

maxNum=9876543210
nodeDist=[maxNum for i in range(N+1)]
dij=[[0,start]]
heapq.heapify(dij)
while(dij):

    temp=heapq.heappop(dij)
    nowCost=temp[0]
    nowNode=temp[1]

    if nowNode==end:
        print(nowCost)
        break

    if nodeDist[nowNode]<nowCost:
        continue
    for toNode,toCost in graph[nowNode]:
        w=nowCost+toCost
        if nodeDist[toNode]>w:
            nodeDist[toNode]=w
            heapq.heappush(dij,[w,toNode])