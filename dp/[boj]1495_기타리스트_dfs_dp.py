import sys

N,S,M=map(int,input().split())
L=list(map(int,sys.stdin.readline().rstrip().split()))

# i번째곡 연주하기전 볼륨이 j일때의 최댓값
dp=[[-1 for j in range(M+1)] for i in range(N)]

def dfs(vol,i):
    global ans
    if i==N:
        return vol

    # [저장된값 있으면]
    if dp[i][vol]!=-1:
        return dp[i][vol]

    # [저장된값 없으면]
    #(더할경우)
    plus = vol + L[i]
    if plus<=M:
        plusV=dfs(plus,i+1)
    else:
        plusV=-100
    #(뺄경우)
    minus = vol - L[i]
    if minus>=0:
        minusV=dfs(minus,i+1)
    else:
        minusV=-100

    maxV=max(plusV,minusV)
    dp[i][vol]=maxV
    return maxV

ans=dfs(S,0)
if ans==-100:
    print(-1)
else:
    print(ans)