from collections import deque
N=int(input())
time=[0 for i in range(N+1)]
ans=[0 for i in range(N+1)]
parent={}
graph={}
q=deque([])
for i in range(1,N+1):
    parent[i]=[]
    graph[i]=[]
for i in range(1,N+1):
    temp=list(map(int,input().split()))
    time[i]=temp.pop(0)
    temp.pop()
    size=len(temp)
    if size==0:
        q.append(i)
        ans[i]=time[i]
    for j in range(size):
        fromNode=temp[j]
        graph[fromNode].append(i)
        parent[i].append(fromNode)

while(q):
    nowNode=q.popleft()
    for toNode in graph[nowNode]:
        parent[toNode].remove(nowNode) #끊기
        temp=ans[nowNode]+time[toNode]
        if temp>ans[toNode]:
            ans[toNode]=temp
        if not parent[toNode]:
            q.append(toNode)


for i in range(1,N+1):
    print(ans[i])