N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

dpR=[0 for j in range(M)]
dpL=[0 for j in range(M)]
dp=[[0 for j in range(M)] for i in range(N)]
dp[0][0]=L[0][0]
for j in range(1,M):
    dp[0][j]=L[0][j]+dp[0][j-1]

for i in range(1,N):
    dpR = [0 for j in range(M)]
    dpR[0]=dp[i-1][0]+L[i][0]
    for j in range(1,M):
        dpR[j]=max(dpR[j-1],dp[i-1][j])+L[i][j]

    dpL = [0 for j in range(M)]
    dpL[M-1]=dp[i-1][M-1]+L[i][M-1]
    for j in range(M-2,-1,-1):
        dpL[j]=max(dpL[j+1],dp[i-1][j])+L[i][j]

    for j in range(M):
        dp[i][j]=max(dpL[j],dpR[j])

print(dp[N-1][M-1])
