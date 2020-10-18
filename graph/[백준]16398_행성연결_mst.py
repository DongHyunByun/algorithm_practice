N=int(input())
L=[]

def union(a,b):
    a=find(a)
    b=find(b)
    parent[b]=a

def find(a):
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

for i in range(N):
    L.append(list(map(int,input().split())))

# edge만들기
edge=[]
for i in range(N):
    for j in range(i+1,N):
        edge.append([L[i][j],i,j])
edge.sort()

# 크루스칼
parent=[i for i in range(N)]

ans=0
node=0
for cost,a,b in edge:
    if find(a)!=find(b):
        union(a,b)
        ans+=cost
        node+=1
        if node==N-1:
            break

print(ans)


