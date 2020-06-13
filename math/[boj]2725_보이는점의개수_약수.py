L=[[1 for j in range(1001)] for i in range(1001)]
# i:분모, j:분자
for i in range(1,1001):
    for j in range(i+1,1001):
        if L[i][j]==1:
            for k in range(2,1000//j+1):
                L[i*k][j*k]=0

t=int(input())
for i in range(t):
    N=int(input())
    ans=0
    for i in range(1,N+1):
        ans+=sum(L[i][i+1:N+1])
    ans*=2
    print(ans+3)

