from itertools import combinations
import math

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

n=int(input())
L=[]
#L[i]= i의 x좌표,i의 y좌표 (i는 0~n-1)
for i in range(n):
    x,y=map(float,input().split())
    L.append([x,y])

#연결그래프 만들기
com=list(combinations([i for i in range(n)],2))
edge=[]
for node1,node2 in com:
    x1,y1=L[node1]
    x2,y2=L[node2]
    edge.append([math.sqrt((x1-x2)**2+(y1-y2)**2),node1,node2])


#크루스칼
parent=[i for i in range(n)]
edge.sort()
cost=0
nodeNum=0
for nowCost,node1,node2 in edge:
    if find(node1)!=find(node2):
        union(node1,node2)
        cost+=nowCost
        nodeNum+=1
        if nodeNum==n-1:
            break
print(cost)
