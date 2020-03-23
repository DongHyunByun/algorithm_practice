import sys
toCal=1
dp=[1,1]
size=2
try:
    while True:
        n=int(input())
        if n<=toCal:
            print(dp[n])
        else:
            for i in range(n-toCal):
                dp.append(dp[size-1]+2*dp[size-2])
                size+=1
            toCal=n
            print(dp[n])
except:
    pass