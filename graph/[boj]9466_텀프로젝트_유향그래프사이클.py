from collections import deque
import sys
sys.setrecursionlimit(1000000)

def dfs(node):
    global cnt
    visited[node]=1
    next=graph[node]
    # 다음노드가 방문이 안되었으면 방문해
    if not visited[next]:
        dfs(next)
    # 다음노드가 방문이 되었는데 끝나진앖았으면 사이클
    elif not fin[next]:
        tempNode=next
        while(1):
            cnt+=1
            tempNode=graph[tempNode]
            if tempNode==next:
                break
    fin[node]=1

T=int(input())
for t in range(T):
    n=int(input())
    L=[0]+list(map(int,input().split()))
    cnt=0

    # 그래프만들기
    graph={}
    for i in range(1,n+1):
        graph[i]=L[i]

    #싸이클확인
    visited=[0 for _ in range(n+1)]
    fin=[0 for _ in range(n+1)]

    for i in range(1,n+1):
        if visited[i]==0:
            dfs(i)
    print(n-cnt)
