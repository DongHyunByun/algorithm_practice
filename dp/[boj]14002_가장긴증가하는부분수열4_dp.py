def firstValue(temp):
    return temp[0]

def find(nowindx,preindx):
    if preindx==nowindx:
        s.append(L[nowindx])
        return
    else:
        s.append(L[nowindx])
        find(preindx,dp[preindx][1])

N=int(input())
L=list(map(int,input().split()))
dp=[[1,i] for i in range(N)]
for i in range(N):
    for j in range(i):
        if L[j]<L[i] and dp[i][0]<dp[j][0]+1:
            dp[i][0]=dp[j][0]+1
            dp[i][1]=j

maxNum=max(dp,key=firstValue)
indx=dp.index(maxNum)
#최장길이출력
print(maxNum[0])
s=[]
find(indx,dp[indx][1])
print(*list(reversed(s)))
