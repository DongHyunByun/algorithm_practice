
dR=[-1,-1,1,1]
dC=[-1,1,-1,1]

N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
maxNum=N*N

# myL에 r,c에 비숍놔둬도 되나?
def isPossible(r,c):
    if L[r][c]==0:
        return False
    for k in range(4):
        for i in range(1,N):
            tempR=r+dR[k]*i
            tempC=c+dC[k]*i
            if 0<=tempR<N and 0<=tempC<N:
                if L[tempR][tempC]==2:
                    return False
            else:
                break
    return True

def dfs(num,cnt):
    global ans
    if num>=maxNum:
        if ans<cnt:
            '''
            print()
            for i in L:
                print(i)
            '''
            ans=cnt
        return

    r=num//N
    c=num%N

    # 비숍놓는경우
    if isPossible(r,c):
        L[r][c]=2
        if N%2==0:
            if c==N-1:
                dfs(num+1,cnt+1)
            elif c==N-2:
                dfs(num+3,cnt+1)
            else:
                dfs(num + 2, cnt + 1)
        else:
            dfs(num+2,cnt+1)
        L[r][c]=1
    # 비숍 안놓는경우
    if N%2==0:
        if c == N - 1:
            dfs(num + 1, cnt)
        elif c == N - 2:
            dfs(num + 3, cnt)
        else:
            dfs(num + 2, cnt)
    else:
        dfs(num+2,cnt)


ans=0
dfs(0,0)
ansWhite=ans

ans=0
dfs(1,0)
ansBlack=ans

print(ansWhite+ansBlack)