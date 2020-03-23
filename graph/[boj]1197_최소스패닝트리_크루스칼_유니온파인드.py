import heapq

def find(x):
    if parent[x]==x:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if (x!=y):
        parent[x]=y
def isCycleUnion(node1,node2):
    # 사이클이면
    if find(node1)==find(node2):
        return True
    # 사이클 아니면
    else:
        union(node1, node2)
        return False
V,E=map(int,input().split())
parent = [i for i in range(V + 1)]
edge=[]
for i in range(E):
    A,B,C=map(int,input().split())
    heapq.heappush(edge,[C,A,B])

edgeNum=0
ans=0
#크루스칼 시작
while(edgeNum!=V-1):
    cost,n1,n2=heapq.heappop(edge)
    if not isCycleUnion(n1,n2):
        ans+=cost
        edgeNum+=1

print(ans)