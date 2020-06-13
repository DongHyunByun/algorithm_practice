a=input()
b=input()
c=input()
sizeA=len(a)
sizeB=len(b)
sizeC=len(c)

dp=[[[0 for k in range(sizeC+1)] for j in range(sizeB+1)] for i in range(sizeA+1)]

for i in range(1,sizeA+1):
    for j in range(1,sizeB+1):
        for k in range(1,sizeC+1):
            if a[i-1]==b[j-1]==c[k-1]:
                dp[i][j][k]=dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

print(dp[sizeA][sizeB][sizeC])