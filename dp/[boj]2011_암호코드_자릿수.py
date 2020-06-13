A="X"+input()
size=len(A)
dp=[0 for i in range(size)]
dp[0]=dp[1]=1

if A[1]=="0":
    print(0)
else:
    for i in range(2,size):
        # 0만아니면 한칸으로 만들기가능
        if A[i]!="0" :
            dp[i]+=dp[i-1]
        # 10이상, 27미만이면 두칸으로 만들기가능
        if 10<=int(A[i-1:i+1])<27:
            dp[i]+=dp[i-2]

    print(dp[size-1]%1000000)


