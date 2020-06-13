N, M = map(int, input().split())
K = int(input())
road = []
for k in range(K):
    temp = list(map(int, input().split()))
    if temp[0] + temp[1] > temp[2] + temp[3]:
        road.append([temp[2], temp[3], temp[0], temp[1]])
    else:
        road.append(list(temp))

dp = [[0 for j in range(M + 2)] for i in range(N + 2)]
dp[0][1] = 1

for i in range(1, N + 2):
    for j in range(1, M + 2):
        # 위에서 내려오는거
        if [i - 2, j - 1, i - 1, j - 1] in road:
            # print([i-2,j-1,i-1,j-1])
            road.remove([i - 2, j - 1, i - 1, j - 1])
        else:
            dp[i][j] += dp[i - 1][j]
        # 왼쪽에서 오는거
        if [i - 1, j - 2, i - 1, j - 1] in road:
            # print([i-1,j-2,i-1,j-1])
            road.remove([i - 1, j - 2, i - 1, j - 1])
        else:
            dp[i][j] += dp[i][j - 1]

print(dp[N + 1][M + 1])