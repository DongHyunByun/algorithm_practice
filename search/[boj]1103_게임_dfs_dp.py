import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
dR = [0, 0, -1, 1]
dC = [1, -1, 0, 0]
def dfs(r, c):
    '''
    print(r,c)
    for i in dp:
        print(i)
    '''
    # 바깥으로 나가거나 구멍에 빠지면
    if not (0 <= r < N and 0 <= c < M):
        return 0
    # 구멍이면
    if L[r][c] == "H":
        return 0
    # 방문한적없음
    if dp[r][c]==-1:
        dp[r][c]=0
        for k in range(4):
            tempR = r + dR[k] * int(L[r][c])
            tempC = c + dC[k] * int(L[r][c])
            # 첫방문
            dp[r][c] = max(dp[r][c], dfs(tempR, tempC) + 1)
        fin[r][c]=1
        return dp[r][c]
    # 방문한적있음
    else:
        # 사이클있음
        if not fin[r][c]:
            print(-1)
            sys.exit()
        else:
            return dp[r][c]

L = []
for i in range(N):
    L.append(list(input()))

ans = 0
dp = [[-1 for j in range(M)] for i in range(N)]
fin =[[0 for j in range(M)] for i in range(N)]
print(dfs(0, 0))
'''
for i in dp:
    print(i)
'''