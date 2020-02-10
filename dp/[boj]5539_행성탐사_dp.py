M,N=map(int,input().split())
K=int(input())

L=[["0" for _ in range(N+1)]]
for i in range(M):
    L.append(["0"]+list(input()))

search=[]
for i in range(K):
    search.append(list(map(int,input().split())))

dp=[[[0,0,0] for j in range(N+1)] for i in range(M+1)]
for i in range(1,M+1):
    for j in range(1,N+1):
        # k는 (0:정글, 1:바다, 2:얼음)
        for k in range(3):
            dp[i][j][k]=dp[i-1][j][k]+dp[i][j-1][k]-dp[i-1][j-1][k]
        if L[i][j]=="J":
            dp[i][j][0]+=1
        elif L[i][j]=="O":
            dp[i][j][1]+=1
        else:
            dp[i][j][2]+=1

for a,b,c,d in search:
    for k in range(3):
        print(dp[c][d][k]-dp[a-1][d][k]-dp[c][b-1][k]+dp[a-1][b-1][k],end=" ")
    print()



