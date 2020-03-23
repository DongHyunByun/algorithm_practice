from collections import deque
import sys

def bfs():
    q=deque([start])
    myMap[start[0]][start[1]][start[2]]=0
    while(q):
        temp=q.popleft()
        #print(temp)
        l=temp[0]
        r=temp[1]
        c=temp[2]
        for k in range(6):
            tempL=l+dL[k]
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempL<L and 0<=tempR<R and 0<=tempC<C:
                if myMap[tempL][tempR][tempC]=="E":
                    return myMap[l][r][c] + 1
                elif myMap[tempL][tempR][tempC]==".":
                    myMap[tempL][tempR][tempC]=myMap[l][r][c]+1
                    q.append([tempL,tempR,tempC])
    return -1

dL=[0,0,0,0,1,-1]
dR=[0,0,-1,1,0,0]
dC=[1,-1,0,0,0,0]

while(1):
    #input
    L, R, C = map(int, sys.stdin.readline().rstrip().split())
    if L==0:
        break
    myMap = []
    for layer in range(L):
        nowLayer = []
        for i in range(R):
            temp=list(sys.stdin.readline().rstrip())
            if "S" in temp:
                start=[layer,i,temp.index("S")]
            nowLayer.append(temp)
        myMap.append(nowLayer)
        sys.stdin.readline().rstrip()

    #bfs시작
    temp=bfs()
    if temp==-1:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)."%(temp))

