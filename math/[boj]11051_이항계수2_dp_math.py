N,K=map(int,input().split())
d=[[0 for j in range(N+1)] for i in range(N+1)]

for i in range(N+1):
    for j in range(i+1):
        if j==0:
            d[i][j]=1
        else:
            d[i][j]=(d[i-1][j-1]+d[i-1][j])%10007


print(d[N][K]%10007)