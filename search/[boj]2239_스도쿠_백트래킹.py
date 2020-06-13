import sys
# sys.setrecursionlimit(10**6) 넣으면 터진다.
L=[]
for i in range(9):
    L.append(list(map(int,list(input()))))
dR=[-1,-1,-1,0,0,0,1,1,1]
dC=[-1,0,1,-1,0,1,-1,0,1]

# r,c에 num을 넣을 수 있는가?
def isPossible(r,c,num):
    #가로 확인
    if num in L[r]:
        return False
    #세로 확인
    if num in [L[i][c] for i in range(9)]:
        return False
    #영역 확인
    cR=(r//3)*3+1
    cC=(c//3)*3+1
    for i in range(9):
        tempR=cR+dR[i]
        tempC=cC+dC[i]
        if L[tempR][tempC]==num:
            return False

    return True

# cnt
def dfs(cnt):
    if cnt==81:
        for i in L:
            print("".join(map(str,i)))
        sys.exit()
    r=cnt//9
    c=cnt%9
    #해당위치에 숫자가 있으면 다음
    if L[r][c]!=0:
        dfs(cnt+1)
    else:
        #해당위치에 숫자가 없으면 넣는게 가능한숫자 넣고 다음진행
        for i in range(1,10):
            if isPossible(r,c,i):
                L[r][c]=i
                dfs(cnt+1)
        L[r][c]=0

dfs(0)