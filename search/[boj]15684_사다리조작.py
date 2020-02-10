def go(L):
    for j in range(N):
        isSame=True
        startR=0
        startC=j
        while(1):
            if (L[startR][startC]==0 ):
                startR+=1
            elif (L[startR][startC]==1):
                startC+=1
                startR+=1
            elif (L[startR][startC]==2):
                startC-=1
                startR+=1

            if startR==H:
                if startC!=j:
                    isSame=False
                break

        if (not isSame):
            return False

    return True


def solve(num, L, addedCross):
    global ans
    
    '''
    print(num,num//N,num%N)
    for i in range(len(L)):
        print(L[i])
    '''
    # 종료조건
    if (ans!=-1 and addedCross>=ans):
        return
    if (num>=N*H or addedCross==3):
        if (go(L)) :
            ans=addedCross
        return 
    
    # 변수준비
    nowR=num//N
    nowC=num%N
   
    # 현재위치 선안긋기
    solve(num+1,L,addedCross)
    # 현재위치 선긋기
    if (nowC<N-1 and L[nowR][nowC]==0 and L[nowR][nowC+1]==0) :
        L[nowR][nowC]=1
        L[nowR][nowC+1]=2
        solve(num+2,L,addedCross+1)

        L[nowR][nowC]=0
        L[nowR][nowC+1]=0


N,M,H=map(int,input().split())

L=[[0 for j in range(N)] for i in range(H)]

# 0이면 아래, 1이면 ->, 2이면 <-
for i in range(M):
    a,b=map(int,input().split())
    L[a-1][b-1]=1
    L[a-1][b]=2

ans=-1
solve(0,L,0)
print(ans)
