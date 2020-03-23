import heapq

maxNum=9876543210
N,K,M=map(int,input().split())
graph={}
for i in range(1,N+M+1):
    graph[i]=[]
for i in range(M):
    temp=list(map(int,input().split()))
    for k in range(K):
        graph[N + i + 1].append([0, temp[k]])
        graph[temp[k]].append([1, N + i + 1])

nodeDist=[maxNum for i in range(N+M+1)]
nodeDist[1]=1
dij=[[1,1]]
ans=-1
while(dij):
    nowCost,nowNode=heapq.heappop(dij)
    if nowNode==N:
        ans=nowCost
        break
    if nodeDist[nowNode]<nowCost:
        continue
    for addedCost,toNode in graph[nowNode]:
        toCost=addedCost+nowCost
        if toCost<nodeDist[toNode]:
            nodeDist[toNode]=toCost
            heapq.heappush(dij,[toCost,toNode])
print(ans)