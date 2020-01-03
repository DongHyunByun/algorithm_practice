from collections import deque

def breaker(R,C,L,W,H):
    stack=deque([[R,C]])
    while stack:
        point=stack.pop()
        r=point[0]
        c=point[1]
        num=L[r][c]
        L[r][c]=0
        dodgeR=[1,-1,0,0]
        dodgeC=[0,0,-1,1]

        for i in range(1,num):
            #0 or 1이면 그패스 , 그렇지 않으면 스택에 추가
            for j in range(4):
                tempR=r+dodgeR[j]*i
                tempC=c+dodgeC[j]*i
                #index error 예외
                if tempR>=H or tempR<0 or tempC>=W or tempC<0 or L[tempR][tempC]==0:
                    continue
                if L[tempR][tempC]==1:
                    L[tempR][tempC]=0
                else:
                    stack.append([tempR,tempC])

def getDown(L,W,H):
    for j in range(W):
        down=[]
        #세로 압축
        for i in range(H):
            if L[i][j]!=0:
                down.append(L[i][j])
        #세로 
        for i in range(H-len(down)):
            L[i][j]=0
        for i in range(H-len(down),H):
            L[i][j]=down.pop(0)

def recursive(L,W,H,times,N):
    global ans

    if (times==N):      
        leftbrick=0
        for i in range(H):
            for j in range(W):
                if L[i][j]!=0:
                    leftbrick+=1
        if leftbrick<ans:
            ans=leftbrick
        return

    isEmpty=True

    for j in range(W):
        for i in range(H):
            if L[i][j]!=0:
                isEmpty=False
                copyL=[]
                for k in L:
                    copyL.append(list(k))
                breaker(i,j,copyL,W,H)
                getDown(copyL,W,H)
                recursive(copyL,W,H,times+1,N)
                break
    if isEmpty:
        ans=0
        return


for t in range(int(input())):
    N,W,H=list(map(int,input().split()))
    oriL=[]
    ans=99999999
    for i in range(H):
        tempL=list(map(int,input().split()))
        oriL.append(tempL)
    recursive(oriL,W,H,0,N)
    print(f"#{t+1} {ans}")