import sys

N=int(input())
if N==0:
    print(0)
    sys.exit()
dp=[[0 for j in range(10)] for i in range(11)]
dp[1][0]=1
acumulate=0
def search(sub,digit,ans):
    #print(sub,digit,ans)
    if digit==0:
        print(ans)
        return
    acu=0
    for j in range(10):
        acu+=dp[digit][j]
        if acu>=sub:
            tempSub=sub-(acu-dp[digit][j])
            ans=ans*10+j
            search(tempSub,digit-1,ans)
            return

for i in range(1,11):
    for j in range(1,10):
        dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
        acumulate+=dp[i][j]
        if acumulate>=N:
            sub=N-(acumulate-dp[i][j])
            search(sub,i-1,j)
            sys.exit()

print(-1)

