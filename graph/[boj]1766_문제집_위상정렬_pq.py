import heapq
N,M=map(int,input().split())

fromNode={}
toNode={}
for i in range(1,N+1):
    fromNode[i]=[]
    toNode[i]=[]

for _ in range(M):
    a,b=map(int,input().split())
    fromNode[b].append(a)
    toNode[a].append(b)

pq=[]
for i in range(1,N+1):
    if not fromNode[i]:
        heapq.heappush(pq,i)

ans=[]
while(pq):
    nowNode=heapq.heappop(pq)
    ans.append(nowNode)
    for conNode in toNode[nowNode]:
        # 이전노드 삭제
        fromNode[conNode].remove(nowNode)
        # 비어있으면
        if not fromNode[conNode]:
            heapq.heappush(pq,conNode)

print(*ans)