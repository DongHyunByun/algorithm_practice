N=int(input())
a,b=map(int,input().split())
a-=1
b-=1
size=int(input())
L=[0]
for i in range(size):
    L.append(int(input())-1)
maxNum=500
# dp[case][a][b] : case번째에 왼쪽문이 a에 열려있고, 오른쪽문이 b에 열려있을 때 최소이동 (a<b)
dp=[[[maxNum for j in range(N)] for i in range(N)] for k in range(len(L))]
dp[0][a][b]=0


for case in range(1,len(L)):
    toOpen=L[case]
    for i in range(N):
        for j in range(i+1,N):
            if dp[case-1][i][j]!=maxNum:
                for x in range(toOpen):
                    temp=abs(i-x)+abs(j-toOpen)+dp[case-1][i][j]
                    if temp<dp[case][x][toOpen]:
                        dp[case][x][toOpen]=temp
                for y in range(toOpen+1,N):
                    temp=abs(i-toOpen)+abs(j-y)+dp[case-1][i][j]
                    if temp<dp[case][toOpen][y]:
                        dp[case][toOpen][y]=temp

print(min([ min(dp[len(L)-1][i]) for i in range(N) ]))