from itertools import combinations
N=int(input())
L=[]
for i in range(N):
    x,y,z=map(int, input().split())
    L.append([x,y,z,i])
parent=[i for i in range(N)]

def returnX(A):
    return A[0]
def returnY(A):
    return A[1]
def returnZ(A):
    return A[2]

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


edge=[]
L.sort(key=returnX)
for i in range(N-1):
    edge.append([L[i + 1][0] - L[i][0], L[i][3], L[i+1][3]])
L.sort(key=returnY)
for i in range(N-1):
    edge.append([L[i + 1][1] - L[i][1], L[i][3], L[i+1][3]])
L.sort(key=returnZ)
for i in range(N-1):
    edge.append([L[i + 1][2] - L[i][2], L[i][3], L[i+1][3]])

edge.sort()
edgeSize=len(edge)
ans=0
for i in range(edgeSize):
    cost,a,b=edge[i]
    if find(a)!=find(b):
        ans+=cost
        union(a,b)

print(ans)

