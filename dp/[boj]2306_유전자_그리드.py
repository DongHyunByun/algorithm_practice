A=input()
size=len(A)

dp=[[0 for j in range(size)] for i in range(size)]

for j in range(1,size):
    for k in range(size-j):
        dp[k][j + k] = dp[k + 1][j + k - 1]
        #a()t or g()c
        if (A[k]=="a" and A[j+k]=="t") or (A[k]=="g" and A[j+k]=="c"):
            dp[k][j+k]+=2

        #합치기
        for s in range(1,j+1):
            dp[k][j+k]=max(dp[k][j+k],dp[k][j+k-s]+dp[k+(j+1-s)][j+k])

print(dp[0][size-1])


