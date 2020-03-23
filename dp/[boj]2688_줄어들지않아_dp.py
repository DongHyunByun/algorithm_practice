dp=[[1 for j in range(10)] for i in range(65)]
def goDp():
    #dp[i][j] : i자리를 만들때 첫째자리수가 9-j이상으로 시작하는 수의 개수
    for i in range(1,65):
        for j in range(1,10):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
def main():
    goDp()
    T = int(input())
    for t in range(T):
        num=int(input())
        print(dp[num][9])

main()