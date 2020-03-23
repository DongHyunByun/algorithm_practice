from collections import deque

minNum=-9876543210
n,m=map(int,input().split())
edge=[]
graph={}
for i in range(1,n+1):
    graph[i]=[]
for i in range(m):
    a,b,c=map(int,input().split())
    edge.append([a,b,c])
    graph[a].append(b)

# [이전노드, ost]
nodeDist=[[i,minNum] for i in range(n+1)]
nodeDist[1][1]=0
def ans():
    ans = []
    now = n
    while (now != 1):
        ans.append(now)
        now = nodeDist[now][0]
    ans.append(now)
    print(*list(reversed(ans)))


def bellman():
    for i in range(n-1):
        for nowNode,toNode,cost in edge:
            if nodeDist[nowNode][1]==minNum:
                continue
            nowDist=nodeDist[nowNode][1] + cost
            if nowDist>nodeDist[toNode][1]:
                nodeDist[toNode][1]=nowDist
                nodeDist[toNode][0]=nowNode

    #싸이클이 있고, 싸이클이 도착지와 연결되는가?
    connectCycle=False
    isUpdate=False
    for nowNode,toNode,cost in edge:
        #출발지와 연결된 싸이클만
        if nodeDist[nowNode][1]==minNum:
            continue
        else:
            nowDist=nodeDist[nowNode][1]+cost
            if nowDist>nodeDist[toNode][1]:
                isUpdate=True
                q=deque([nowNode])
                visited=[-1 for i in range(n+1)]
                visited[nowNode]=1
                while(q):
                    temp=q.popleft()
                    #싸이클이 목적지와 붙어있다
                    if temp==n:
                        connectCycle=True
                        break
                    for conNode in graph[temp]:
                        if visited[conNode]==-1:
                            visited[conNode]=1
                            q.append(conNode)
    #(출발지와 붙은)싸이클있다
    if isUpdate:
        #도착지와도 붙어있다
        if connectCycle:
            print(-1)
        else:
            ans()
    else:
        #도달불가능
        if nodeDist[n][1]==minNum:
            print(-1)
        #도달가능
        else:
            ans()

bellman()
