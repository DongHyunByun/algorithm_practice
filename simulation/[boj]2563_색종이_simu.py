N=int(input())
L=[[0 for j in range(100)] for i in range(100)]

for i in range(N):
    a,b=map(int,input().split())
    r=b-1
    c=a-1
    for i in range(10):
        for j in range(10):
            L[r+i][c+j]=1

ans=0
for i in range(100):
    ans+=sum(L[i])
print(ans)