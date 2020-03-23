from itertools import combinations
import math
import sys

def find(a):
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)
    parent[b]=a

N,M=map(int,sys.stdin.readline().rstrip().split())
L=[]
parent=[i for i in range(N)]
cost=0
nodeNum=0
for i in range(N):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    L.append([x,y])
for i in range(M):
    node1,node2=map(int,sys.stdin.readline().rstrip().split())
    union(node1-1,node2-1)
    nodeNum+=1
    x1,y1=L[node1-1]
    x2,y2=L[node2-1]

#그래프 만들기
edge=[]
com=list(combinations([i for i in range(N)],2))
for node1,node2 in com:
    x1,y1=L[node1]
    x2,y2=L[node2]
    edge.append([math.sqrt((x1-x2)**2+(y1-y2)**2),node1,node2])
edge.sort()

#크루스칼
for nowCost,node1,node2 in edge:
    if find(node1)!=find(node2):
        union(node1,node2)
        cost+=nowCost
        nodeNum+=1
        if nodeNum==N-1:
            break
print("%.2f"%(cost))
