import heapq
maxNum=9876543210

T=int(input())
for _ in range(T):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    graph={}
    for i in range(1,n+1):
        graph[i]=[]
    for i in range(m):
        a,b,d=map(int,input().split())
        graph[a].append([b,d])
        graph[b].append([a,d])
    dest=[]
    for i in range(t):
        dest.append(int(input()))
    dest.sort()

    isConnected=[0 for i in range(n+1)] #g-h 간선을 지났으면 1
    dij=[[0,s,0]]
    nodeDist=[maxNum for i in range(n+1)]
    nodeDist[s]=0
    while(dij):
        nowDist,nowNode,isCon=heapq.heappop(dij)
        if nodeDist[nowNode]<nowDist:
            continue
        if isCon:
            isConnected[nowNode]=1
        for toNode,cost in graph[nowNode]:
            addedDist=nowDist+cost
            if addedDist<=nodeDist[toNode]:
                nodeDist[toNode]=addedDist
                if isCon or [nowNode,toNode] in [[g,h],[h,g]]:
                    heapq.heappush(dij,[addedDist,toNode,1])
                else:
                    heapq.heappush(dij,[addedDist,toNode,0])

    #print(nodeDist)
    #print(isConnected)
    ans=[]
    for i in dest:
        if isConnected[i]:
            ans.append(i)
    print(*ans)