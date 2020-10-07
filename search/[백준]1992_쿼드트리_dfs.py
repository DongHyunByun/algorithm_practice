n=int(input())
L=[]
for i in range(n):
    L.append(list(input()))

def dfs(r,c,size):
    global ans
    half=size//2
    numType=L[r][c]
    for i in range(size):
        for j in range(size):
            if L[r+i][c+j]!=numType:
                ans+="("
                dfs(r,c,half)
                dfs(r,c+half,half)
                dfs(r+half,c,half)
                dfs(r+half,c+half,half)
                ans+=")"
                return

    ans+=L[r][c]

ans=""
dfs(0,0,n)
print(ans)