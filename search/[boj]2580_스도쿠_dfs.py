import sys
L=[]
for i in range(9):
    L.append(list(map(int,input().split())))

#행, 열, 구역 검사
def cheak(L,r,c,num):
    #행검사
    if num in L[r]:
        return False
    #열검사
    for i in range(9):
        if L[i][c]==num:
            return False
    #영역검사
    dR = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dC = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    centorR=3*(r//3)+1
    centorC=3*(c//3)+1
    for k in range(9):
        tempR=centorR+dR[k]
        tempC=centorC+dC[k]
        if L[tempR][tempC]==num:
            return False
    return True

def dfs(num,L):
    if num==81:
        for i in range(9):
            print(*L[i])
        sys.exit()

    r=num//9
    c=num%9
    if L[r][c]!=0:
        dfs(num+1,L)
    else:
        for i in range(1,10):
            if cheak(L,r,c,i):
                L[r][c] = i
                dfs(num+1,L)
        L[r][c]=0

dfs(0,L)