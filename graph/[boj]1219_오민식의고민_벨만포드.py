from collections import deque
maxNum=9999999999999999

def bellman():
    nodeCost=[maxNum for i in range(N)]
    nodeCost[A]=-money[A]
    #벨만포드
    for i in range(N-1):
        for n1,n2,cost in edge:
            if nodeCost[n1]==maxNum:
                continue
            nowCost=nodeCost[n1]+cost
            if nowCost<nodeCost[n2]:
                nodeCost[n2]=nowCost

    isUpdate=False
    isPossible=False
    #싸이클있는지 확인(N번째 반복)
    for n1,n2,cost in edge:
        #시작부분과 연결되었고, 음의 사이클이 존재할때
        if nodeCost[n1]!=maxNum and nodeCost[n1]+cost<nodeCost[n2]:
            #print(n1,n2,"사이클확인시작")
            isUpdate=True
            #싸이클에서 목적지 갈 수 잇는지 확인
            visited=[-1 for i in range(N)]
            q=deque([n1])
            visited[n1]=1
            while(q):
                temp=q.popleft()
                if temp==B:
                    isPossible=True
                    break
                for node in graph[temp]:
                    if visited[node]==-1:
                        visited[node]=1
                        q.append(node)
            if isPossible:
                break
    #print(isUpdate,isPossible)
    #print(nodeCost)
    #도달여부확인
    if nodeCost[B]==maxNum:
        print("gg")
    else:
        if isUpdate and isPossible:
            print("Gee")
        else:
            print(-nodeCost[B])


N,A,B,M=map(int,input().split())
edge=[]
graph={}
for i in range(N):
    graph[i]=[]
for m in range(M):
    temp=list(map(int,input().split()))
    edge.append(temp)
    graph[temp[0]].append(temp[1])
money=list(map(int,input().split()))
#방문했을때 버는 돈 추가
for m in range(M):
    edge[m][2]-=money[edge[m][1]]
bellman()