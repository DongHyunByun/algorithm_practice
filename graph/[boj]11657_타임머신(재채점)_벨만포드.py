INF=9876543210

N,M=map(int,input().split())
edge=[]

for i in range(M):
    A,B,C=map(int,input().split())
    edge.append([A,B,C])

isUpdate=False
nodeDist=[INF for i in range(N+1)]
nodeDist[1]=0
for i in range(N):
    isUpdated=False
    for fromNode,toNode,addedCost in edge:
        if nodeDist[fromNode]==INF:
            continue
        newCost=nodeDist[fromNode]+addedCost
        if nodeDist[toNode]>newCost:
            nodeDist[toNode]=newCost
            isUpdated=True

if isUpdated:
    print(-1)
else:
    for i in range(2,N+1):
        if nodeDist[i]==INF:
            print(-1)
        else:
            print(nodeDist[i])