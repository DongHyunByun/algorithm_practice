import sys
N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(input()))
k=int(input())
parent=[i for i in range(N)]

def find(a):
    if a==parent[a]:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
#a에 b를 붙이기
def union(a,b):
    a=find(a)
    b=find(b)
    parent[b]=a

for i in range(N):
    for j in range(i+1,N):
        if L[i]==L[j]:
            union(i,j)

for i in range(N):
    find(i)
tempL=[0 for i in range(N)]
for i in range(N):
    tempL[parent[i]]+=1
cntL=[]
for i in range(N):
    cntL.append([tempL[i],i])

cntL.sort(reverse=True)
for num,rowNum in cntL:
    cntZero=0
    for j in L[rowNum]:
        if j=="0":
            cntZero+=1
    if k>=cntZero and k%2==cntZero%2:
        print(num)
        sys.exit()
print(0)