from collections import deque
import sys

T=int(input())
for t in range(T):
    #입력
    N,K=map(int,input().split())
    build=list(map(int,sys.stdin.readline().rstrip().split()))
    parent={} #부모노드
    graph={} #자식노드
    for i in range(1,N+1):
        parent[i]=[]
        graph[i]=[]
    for i in range(K):
        x,y=map(int,sys.stdin.readline().rstrip().split())
        graph[x].append(y)
        parent[y].append(x)
    w=int(sys.stdin.readline().rstrip())
    q=deque([])
    time=list(build)

    #위상정렬
    #시작노드넣기(부모노드없는것)
    for i in range(1,N+1):
        if not parent[i]:
            q.append(i)

    while(q):
        nowNode=q.popleft()
        if nowNode==w:
            print(time[w-1])
            break
        for conNode in graph[nowNode]:
            temp=time[nowNode-1]+build[conNode-1]
            if time[conNode-1]<temp:
                time[conNode-1]=temp
            parent[conNode].remove(nowNode)
            #부모노드가 없으면 큐에넣기
            if not parent[conNode]:
                q.append(conNode)

