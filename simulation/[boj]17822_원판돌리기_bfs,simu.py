from collections import deque
import sys

dR=[0,0,-1,1]
dC=[1,-1,0,0]
N,M,T=map(int,input().split())
L=[[]]
tL=[]
for i in range(N):
    L.append(list(map(int,input().split())))
for i in range(T):
    tL.append(list(map(int,input().split())))
total=N*M

def rotate(i,d,k):
    #시계방향
    if d==0:
        for _ in range(k):
            L[i].insert(0,L[i].pop())
    #반시계방향
    else:
        for _ in range(k):
            L[i].append(L[i].pop(0))

#회전시작
for t in range(T):
    x,d,k=tL[t]
    #회전
    for i in range(x,N+1,x):
        rotate(i,d,k)
    '''
    print("회전후")
    for i in L:
        print(i)
    print()
    '''
    isNum=False
    #인접한 수 찾기
    for i in range(1,N+1):
        for j in range(M):
            #숫자가 있으면
            if L[i][j]!=0:
                q=deque([[i,j]])
                num=L[i][j]
                cnt=0
                while(q):
                    r,c=q.popleft()
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if tempC==M:
                            tempC=0
                        elif tempC==-1:
                            tempC=M-1
                        if 1<=tempR<N+1 and 0<=tempC<M and L[tempR][tempC]==num:
                            isNum=True
                            cnt += 1
                            L[tempR][tempC]=0
                            q.append([tempR,tempC])
                total-=cnt
                #다지워지면 0
                if total==0:
                    print(0)
                    sys.exit()
    #숫자 삭제후
    if not isNum:
        totalSum=0
        for i in range(1,N+1):
            totalSum+=sum(L[i])
        aver=totalSum/total
        for i in range(1,N+1):
            for j in range(M):
                if L[i][j]!=0:
                    if L[i][j]<aver:
                        L[i][j]+=1
                    elif L[i][j]>aver:
                        L[i][j]-=1
    '''
    print("인접 삭제후")
    for i in L:
        print(i)
    '''
ans=0
for i in range(1,N+1):
    ans+=sum(L[i])
print(ans)