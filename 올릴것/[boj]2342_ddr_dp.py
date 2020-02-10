L=list(map(int,input().split()))
L.insert(0,L.pop())
size=len(L)

dp=[[[500000 for r in range(5)] for l in range(5)] for i in range(size)]
dp[0][0][0]=0

def cal(a, b):
    if a==b:
        return 1
    elif a==0:
        return 2
    elif abs(a-b)==2:
        return 4
    else:
        return 3

# ddr시작
for i in range(1,size):
    for l in range(5):
        for r in range(5):
            # 오른발 왼발 같이 놓을때x
            if l==r:
                continue
            if L[i]!=l and L[i]!=r:
                continue
            for z in range(5):
                # 왼발이 밟을때
                if (l==L[i]):
                    dp[i][l][r]=min(dp[i][l][r],dp[i-1][z][r]+cal(z,l))
                # 오른발이 밟을때
                else:
                    dp[i][l][r]=min(dp[i][l][r],dp[i-1][l][z]+cal(z,r))

print(min([min(dp[size-1][i]) for i in range(5)]))
