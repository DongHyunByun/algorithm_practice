from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]

T=int(input())
for t in range(T):
    w,h=map(int,input().split())
    L=[]
    for i in range(h):
        L.append(list(input()))
    fire=deque([])
    sang=deque([])
    for i in range(h):
        for j in range(w):
            if L[i][j]=="*":
                fire.append([i,j])
            elif L[i][j]=="@":
                sang.append([i,j])
                L[i][j]=0
    ans="IMPOSSIBLE"
    time=0
    #탈출시작
    while(1):
        #불확산
        size=len(fire)
        for i in range(size):
            temp=fire.popleft()
            r=temp[0]
            c=temp[1]
            for k in range(4):
                tempR=r+dR[k]
                tempC=c+dC[k]
                if 0<=tempR<h and 0<=tempC<w and L[tempR][tempC]!="*" and L[tempR][tempC]!="#":
                    L[tempR][tempC]="*"
                    fire.append([tempR,tempC])
        #상근도망
        isEscape=False
        sangSize=len(sang)
        for i in range(sangSize):
            temp=sang.popleft()
            r=temp[0]
            c=temp[1]
            for k in range(4):
                tempR=r+dR[k]
                tempC=c+dC[k]
                if 0<=tempR<h and 0<=tempC<w:
                    if L[tempR][tempC]==".":
                        sang.append([tempR,tempC])
                        L[tempR][tempC]=time+1
                else:
                    #탈출성공
                    isEscape=True
                    ans=time+1
                    break
        if isEscape or sangSize==0:
            break
        '''
        for i in range(h):
            print(L[i])
        print()
        '''
        time+=1

    print(ans)