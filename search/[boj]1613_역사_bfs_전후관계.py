import sys
from collections import deque

def bfs(event):
    q=deque([event])
    visited=[0 for i in range(n+1)]
    visited[event]=1
    while(q):
        nowEvent=q.popleft()
        for nextEvent in graph[nowEvent]:
            if visited[nextEvent]==0:
                visited[nextEvent]=1
                q.append(nextEvent)
                after[event].add(nextEvent)

n,k=map(int,input().split())
graph={}
for i in range(1,n+1):
    graph[i]=[]
for i in range(k):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)

after=[set([]) for i in range(n+1)] #after[i] : i사건의 이후에 일어난 모든 사건

for i in range(1,n+1):
    bfs(i)
'''
for i in range(1,n+1):
    print(i,"사건의 후")
    print(after[i])
'''

s=int(input())
for i in range(s):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    if b in after[a]:
        print(-1)
    elif a in after[b]:
        print(1)
    else:
        print(0)