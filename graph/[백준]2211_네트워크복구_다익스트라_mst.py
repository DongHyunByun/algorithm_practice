import heapq

inf=9876543210

N,M=map(int,input().split())
graph={}
for i in range(1,N+1):
    graph[i]=[]

for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

# nodeDist[i]=[a,b] => a: 1에서 i노드까지의 거리, b: i노드의 이전노드
nodeDist=[[inf,i] for i in range(N+1)]
dij=[[0,1]]
nodeDist[1][0]=0

ans=[]

while(dij):
    cost,nowNode=heapq.heappop(dij)
    if cost>nodeDist[nowNode][0]:
        continue
    ans.append([nowNode,nodeDist[nowNode][1]])
    for toNode,toCost in graph[nowNode]:
        addedCost=cost+toCost
        if addedCost<nodeDist[toNode][0]:
            nodeDist[toNode][0]=addedCost
            nodeDist[toNode][1]=nowNode
            heapq.heappush(dij,[addedCost,toNode])

print(N-1)
for i in range(1,N):
    print(*ans[i])
