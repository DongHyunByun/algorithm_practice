A="0"+input()
B="0"+input()
sizeA=len(A)
sizeB=len(B)
dp=[[0 for i in range(sizeB)] for j in range(sizeA)]
for i in range(1,sizeA):
    for j in range(1,sizeB):
        if A[i]==B[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[sizeA-1][sizeB-1])


