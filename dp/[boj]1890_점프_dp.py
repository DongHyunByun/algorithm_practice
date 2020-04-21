N=int(input())
dR=[0,1]
dC=[1,0]
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
dp=[[0 for j in range(N)] for i in range(N)]
dp[0][0]=1

for i in range(N):
    for j in range(N):
        if L[i][j]==0:
            continue
        for k in range(2):
            tempR=i+dR[k]*L[i][j]
            tempC=j+dC[k]*L[i][j]
            if 0<=tempR<N and 0<=tempC<N:
                dp[tempR][tempC]+=dp[i][j]

print(dp[N-1][N-1])