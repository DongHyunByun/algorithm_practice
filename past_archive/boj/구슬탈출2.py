from collections import deque
import copy

N,M=map(int,input().split())
L=[]
for i in range(N):
    temp=list(input())
    if "B" in temp:
        bR=i
        bC=temp.index("B")
    if "R" in temp:
        rR=i
        rC=temp.index("R")
    if "O" in temp:
        oR=i
        oC=temp.index("O")
    L.append(temp)

def tilt(L,num):
    global rR,rC,bR,bC
    inHole=False
    if num==1:
        #레드가 위
        if rC==bC and rR<bR:
            #레드
            for i in range(1,N):
                if L[rR-i][rC]=="#":
                    L[rR][rC]="."
                    L[rR-i+1][rC]="R"
                    rR=rR-i+1
                    break
                elif L[rR-i][rC]=="O":
                    L[rR][rC]="."
                    inHole=True
                    break
            #블루
            for i in range(1,N):
                if L[bR-i][bC]=="#" or L[bR-i][bC]=="R":
                    L[bR][bC]="."
                    L[bR-i+1][bC]="B"
                    bR=bR-i+1
                    break
                elif L[bR-i][bC]=="O":
                    return 0

        elif rC==bC and rR>bR:
            #블루
            for i in range(1,N):
                if L[bR-i][bC]=="#":
                    L[bR][bC]="."
                    L[bR-i+1][bC]="B"
                    bR=bR-i+1
                    break
                elif L[bR-i][bC]=="O":
                    return 0
            #레드
            for i in range(1,N):
                if L[rR-i][rC]=="#" or L[rR-i][rC]=="B":
                    L[rR][rC]="."
                    L[rR-i+1][rC]="R"
                    rR=rR-i+1
                    break
                elif L[rR-i][rC]=="O":
                    return 1
        else:
            #레드
            for i in range(1,N):
                if L[rR-i][rC]=="#":
                    L[rR][rC]="."
                    L[rR-i+1][rC]="R"
                    rR=rR-i+1
                    break
                elif L[rR-i][rC]=="O":
                    inHole=True
                    break
            #블루
            for i in range(1,N):
                if L[bR-i][bC]=="#":
                    L[bR][bC]="."
                    L[bR-i+1][bC]="B"
                    bR=bR-i+1
                    break
                elif L[bR-i][bC]=="O":
                    return 0
    
    elif num==4:
        #레드가 밑
        if rC==bC and rR>bR:
            #레드
            for i in range(1,N):
                if L[rR+i][rC]=="#":
                    L[rR][rC]="."
                    L[rR+i-1][rC]="R"
                    rR=rR+i-1
                    break
                elif L[rR+i][rC]=="O":
                    L[rR][rC]="."
                    inHole=True
                    break
            #블루
            for i in range(1,N):
                if L[bR+i][bC]=="#" or L[bR+i][bC]=="R":
                    L[bR][bC]="."
                    L[bR+i-1][bC]="B"
                    bR=bR+i-1
                    break
                elif L[bR+i][bC]=="O":
                    return 0

        elif rC==bC and rR<bR:
            #블루
            for i in range(1,N):
                if L[bR+i][bC]=="#":
                    L[bR][bC]="."
                    L[bR+i-1][bC]="B"
                    bR=bR+i-1
                    break
                elif L[bR+i][bC]=="O":
                    return 0
            #레드
            for i in range(1,N):
                if L[rR+i][rC]=="#" or L[rR+i][rC]=="B":
                    L[rR][rC]="."
                    L[rR+i-1][rC]="R"
                    rR=rR+i-1
                    break
                elif L[rR+i][rC]=="O":
                    return 1
        else:
            #레드
            for i in range(1,N):
                if L[rR+i][rC]=="#":
                    L[rR][rC]="."
                    L[rR+i-1][rC]="R"
                    rR=rR+i-1
                    break
                elif L[rR+i][rC]=="O":
                    inHole=True
                    break
            #블루
            for i in range(1,N):
                if L[bR+i][bC]=="#":
                    L[bR][bC]="."
                    L[bR+i-1][bC]="B"
                    bR=bR+i-1
                    break
                elif L[bR+i][bC]=="O":
                    return 0
    elif num==2:
        #레드가 왼쪽
        if rR==bR and rC<bC:
            #레드
            for i in range(1,M):
                if L[rR][rC-i]=="#":
                    L[rR][rC]="."
                    L[rR][rC-i+1]="R"
                    rC=rC-i+1
                    break
                elif L[rR][rC-i]=="O":
                    L[rR][rC]="."
                    inHole=True
                    break
            #블루
            for i in range(1,M):
                if L[bR][bC-i]=="#" or L[bR][bC-i]=="R":
                    L[bR][bC]="."
                    L[bR][bC-i+1]="B"
                    bC=bC-i+1
                    break
                elif L[bR][bC-i]=="O":
                    return 0

        elif rR==bR and rC>bC:
            #블루
            for i in range(1,M):
                if L[bR][bC-i]=="#":
                    L[bR][bC]="."
                    L[bR][bC-i+1]="B"
                    bC=bC-i+1
                    break
                elif L[bR][bC-i]=="O":
                    return 0
            #레드
            for i in range(1,M):
                if L[rR][rC-i]=="#" or L[rR][rC-i]=="B":
                    L[rR][rC]="."
                    L[rR][rC-i+1]="R"
                    rC=rC-i+1
                    break
                elif L[rR][rC-i]=="O":
                    return 1
        else:
            #레드
            for i in range(1,M):
                if L[rR][rC-i]=="#":
                    L[rR][rC]="."
                    L[rR][rC-i+1]="R"
                    rC=rC-i+1
                    break
                elif L[rR][rC-i]=="O":
                    inHole=True
                    break
            #블루
            for i in range(1,M):
                if L[bR][bC-i]=="#":
                    L[bR][bC]="."
                    L[bR][bC-i+1]="B"
                    bC=bC-i+1
                    break
                elif L[bR][bC-i]=="O":
                    return 0
    else:
        #레드가 오른쪽
        if rR==bR and rC>bC:
            #레드
            for i in range(1,M):
                if L[rR][rC+i]=="#":
                    L[rR][rC]="."
                    L[rR][rC+i-1]="R"
                    rC=rC+i-1
                    break
                elif L[rR][rC+i]=="O":
                    L[rR][rC]="."
                    inHole=True
                    break
            #블루
            for i in range(1,M):
                if L[bR][bC+i]=="#" or L[bR][bC+i]=="R":
                    L[bR][bC]="."
                    L[bR][bC+i-1]="B"
                    bC=bC+i-1
                    break
                elif L[bR][bC+i]=="O":
                    return 0

        elif rR==bR and rC<bC:
            #블루
            for i in range(1,M):
                if L[bR][bC+i]=="#":
                    L[bR][bC]="."
                    L[bR][bC+i-1]="B"
                    bC=bC+i-1
                    break
                elif L[bR][bC+i]=="O":
                    return 0
            #레드
            for i in range(1,M):
                if L[rR][rC+i]=="#" or L[rR][rC+i]=="B":
                    L[rR][rC]="."
                    L[rR][rC+i-1]="R"
                    rC=rC+i-1
                    break
                elif L[rR][rC+i]=="O":
                    return 1
        else:
            #레드
            for i in range(1,M):
                if L[rR][rC+i]=="#":
                    L[rR][rC]="."
                    L[rR][rC+i-1]="R"
                    rC=rC+i-1
                    break
                elif L[rR][rC+i]=="O":
                    inHole=True
                    break
            #블루
            for i in range(1,M):
                if L[bR][bC+i]=="#":
                    L[bR][bC]="."
                    L[bR][bC+i-1]="B"
                    bC=bC+i-1
                    break
                elif L[bR][bC+i]=="O":
                    return 0
    if inHole:
        return 1
    else:
        return 2
        
queue=deque([[L,0,rR,rC,bR,bC]])

visited=[]


while queue:
    temp=queue.popleft()
    if temp[2:6] in visited:
        continue
    else:
        visited.append(list(temp[2:6]))
    isFin=False
    '''
    for i in temp[0]:
        print(i)
    '''
    
    for i in range(1,5):

        temL=copy.deepcopy(temp[0])
        rR=temp[2]
        rC=temp[3]
        bR=temp[4]
        bC=temp[5]

        ans=tilt(temL,i)
        if ans==1:
            isFin=True
            break
        if rR==temp[2] and rC==temp[3] and bR==temp[4] and bC==temp[5]:
            continue
        '''
        print(i,"번으로 기울임")
        for k in temL:
            print(k)
        '''
        if ans==0:
            continue
        else:
            if temp[1]<10:
                queue.append([temL,temp[1]+1,rR,rC,bR,bC])
    if isFin and temp[1]!=10:
        print(temp[1]+1)
        break
if not isFin or temp==10:
    print(-1)


    

