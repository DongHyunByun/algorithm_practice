card=input()
size=len(card)
dp=[0 for i in range(size)]
def dfs(n):
    global cnt
    if card[n]=="0":
        return 0

    if n==size-1:
        return 1
    if n==size-2:
        if int(card[n:n + 2]) < 35 and card[n+1]!="0":
            return 2
        else:
            return 1

    if dp[n]:
        return dp[n]
    else:
        # 하나추가
        one=dfs(n+1)
        dp[n]+=one
        # 두개추가
        if int(card[n:n+2])<35:
            two=dfs(n+2)
            dp[n]+=two
        return dp[n]

cnt=0
print(dfs(0))

