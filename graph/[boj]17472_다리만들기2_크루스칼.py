from collections import deque
N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
dR=[0,0,-1,1]
dC=[1,-1,0,0]
isNumL=[[0 for j in range(M)] for i in range(N)]
E=[]
nodeNum=0

def makeNum():
    global nodeNum
    for i in range(N):
        for j in range(M):
            if L[i][j]==1 and isNumL[i][j]==0:
                nodeNum += 1
                q=deque([[i,j]])
                isNumL[i][j]=nodeNum
                while(q):
                    temp=q.popleft()
                    r=temp[0]
                    c=temp[1]
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<N and 0<=tempC<M and L[tempR][tempC]==1 and isNumL[tempR][tempC]==0:
                            isNumL[tempR][tempC]=nodeNum
                            q.append([tempR,tempC])


def makeGraph():
    for i in range(N):
        for j in range(M):
            #거리측정
            if isNumL[i][j]!=0:
                #네방향 전진
                for k in range(4):
                    #최대 10까지 전진
                    for go in range(1,10):
                        tempR=i+dR[k]*go
                        tempC=j+dC[k]*go
                        if 0<=tempR<N and 0<=tempC<M:
                            if isNumL[tempR][tempC]!=0:
                                if isNumL[tempR][tempC]!=isNumL[i][j] and go-1>=2:
                                    nowGo=go-1
                                    isIn=False
                                    tempL=sorted([isNumL[tempR][tempC],isNumL[i][j]])
                                    for indx,edge in enumerate(E):
                                        if edge[1:]==tempL:
                                            if nowGo<edge[0]:
                                                E[indx][0]=nowGo
                                            isIn=True
                                            break
                                    if not isIn:
                                        E.append([go,tempL[0],tempL[1]])
                                break
                        else:
                            break


def isCycle(krus):
    stack=deque([krus[0][0]])
    visited=[]
    while(stack):
        node=stack.pop()
        visited.append(node)
        if node in stack:
            return True
        for node1,node2 in krus:
            if node1==node:
                other=node2
            elif node2==node:
                other=node1
            else:
                continue
            if other not in visited:
                stack.append(other)

    return False

def kruscal():
    E.sort()
    krus=[]
    cost=0
    for i in range(len(E)):
        #추가해보기
        cost+=E[i][0]
        krus.append([E[i][1],E[i][2]])
        #사이클인지 확인
        if isCycle(krus):
            krus.pop()
            cost -= E[i][0]
        else:
            if len(krus) == nodeNum - 1:
                return cost

    return -1


def main():
    makeNum()
    makeGraph()
    '''
    for i in range(N):
        print(isNumL[i])
    print(E)
    '''
    print(kruscal())
main()
