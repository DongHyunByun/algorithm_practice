dR = [-1, 0, 1]
dC = [1, 1, 1]

R, C = map(int, input().split())

L = []
for i in range(R):
    L.append(list(input()))


def dfs(r, c):
    if c == C - 1:
        return True

    for k in range(3):
        tempR = r + dR[k]
        tempC = c + dC[k]
        if 0 <= tempR < R and L[tempR][tempC] == ".":
            L[tempR][tempC]="o"
            if dfs(tempR, tempC):
                return True

    return False

ans = 0
for i in range(R):
    ans += dfs(i, 0)
print(ans)


