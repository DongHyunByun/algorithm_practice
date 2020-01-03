from collections import deque
N=int(input())
L=[]
for i in range(N):
    tempL=list(map(int,input().split()))
    if 9 in tempL:
        babyR=i
        babyC=tempL.index(9)
    L.append(tempL)
babyS=2
fish=0
t=0
moveR=[-1,0,0,1]
moveC=[0,-1,1,0]


while(1):
    '''
    for i in L:
        print(i)
    print(babyS,t)
    '''
    isEat=False
    q=deque([])
    #첫번째
    for i in range(4):
        R=babyR+moveR[i]
        C=babyC+moveC[i]
        if R<0 or R>=N or C<0 or C>=N:
            continue
        if L[R][C]==0 or L[R][C]==babyS:
            q.append([R,C,1])
        elif L[R][C]<babyS:
            isEat=True
            candiL=[[R,C,1]]
            q.clear()
            break
    if q:
        distance=100
        candiL=[]
        cheakL=[[0 for _ in range(N)] for _ in range(N)]
        cheakL[babyR][babyC]=1
        for i in q:
            cheakL[i[0]][i[1]]=1
    #queue시작
    while q:
        #print(q)
        temp=q.popleft()
        if temp[2]>=distance:
            break
        for i in range(4):
            R=temp[0]+moveR[i]
            C=temp[1]+moveC[i]
            if R<0 or R>=N or C<0 or C>=N:
                continue
            if (L[R][C]==0 or L[R][C]==babyS):
                if cheakL[R][C]==0:
                    cheakL[R][C]=1
                    q.append([R,C,temp[2]+1])
            elif L[R][C]<babyS :
                candiL.append([R,C,temp[2]+1])
                distance=temp[2]+1
                isEat=True

    candiL.sort()
    #먹을수 있는가?
    if isEat:
        fish+=1
        if fish==babyS:
            babyS+=1
            fish=0
        t+=candiL[0][2]
        L[babyR][babyC]=0
        babyR=candiL[0][0]
        babyC=candiL[0][1]
        L[babyR][babyC]=0

    else:
        print(t)
        break
    
    
    
    

