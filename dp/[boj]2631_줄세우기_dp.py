N=int(input())
L=[]
for i in range(N):
    L.append(int(input()))

lis=[1 for i in range(N)]

for i in range(1,N):
    for j in range(0,i):
        if L[j]<L[i] and lis[i]<lis[j]+1:
            lis[i]=lis[j]+1
print(N-max(lis))

