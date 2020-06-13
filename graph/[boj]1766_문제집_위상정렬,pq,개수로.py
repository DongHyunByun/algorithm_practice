import heapq
N,M=map(int,input().split())

toNode={}
cntParent=[0 for i in range(N+1)]
for i in range(1,N+1):
    toNode[i]=[]

for _ in range(M):
    a,b=map(int,input().split())
    toNode[a].append(b)
    cntParent[b]+=1

pq=[]
for i in range(1,N+1):
    if cntParent[i]==0:
        heapq.heappush(pq,i)

ans=[]
while(pq):
    nowNode=heapq.heappop(pq)
    ans.append(nowNode)
    for conNode in toNode[nowNode]:
        cntParent[conNode]-=1
        if cntParent[conNode]==0:
            heapq.heappush(pq,conNode)

print(*ans)