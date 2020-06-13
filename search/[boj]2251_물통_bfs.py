from collections import deque
A,B,C=map(int,input().split())
limitL=[A,B,C]
visited=[[[0 for k in range(201)] for j in range(201)] for i in range(201)]
q=deque([[0,0,C]])
visited[0][0][C]=1
ansS=set([C])

isFirst=True
# x에서 y로 붙기
def pour(x,y,indexY):
    # 다 부울때
    if x+y<=limitL[indexY]:
        return 0,x+y
    # 다 못부울때
    else:
        return x+y-limitL[indexY],limitL[indexY]
while(q):
    a,b,c=q.popleft()
    #print(a,b,c)
    L=[a,b,c]
    if not isFirst and L==[A,B,C]:
        break
    isFirst=False

    # [총 6가지 방법으로 물옮기기가능]
    for i,alpaI in enumerate([a,b,c]):
        for j,alpaJ in enumerate([a,b,c]):
            if i!=j:
                #print(i,"에서",j,"로 붓는다")
                tempI,tempJ=pour(alpaI,alpaJ,j)
                tempL=list(L)
                tempL[i]=tempI
                tempL[j]=tempJ
                #print(tempL)
                if visited[tempL[0]][tempL[1]][tempL[2]]==0:
                    visited[tempL[0]][tempL[1]][tempL[2]]=1
                    q.append(tempL)
                    if tempL[0]==0 and tempL[2] not in ansS:
                        ansS.add(tempL[2])

ans=sorted(ansS)
print(*ans)

