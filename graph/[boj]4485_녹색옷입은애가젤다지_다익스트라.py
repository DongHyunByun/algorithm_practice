import heapq

maxNum=9876543210
dR=[0,0,-1,1]
dC=[1,-1,0,0]
tcase=1
while(1):
    N=int(input())
    if N==0:
        break
    L=[]
    for i in range(N):
        L.append(list(map(int,input().split())))
    nodeDist=[[maxNum for j in range(N)] for i in range(N)]
    dij=[[L[0][0],0,0]]
    nodeDist[0][0]=L[0][0]
    while(dij):
        temp=heapq.heappop(dij)
        nowCost=temp[0]
        r=temp[1]
        c=temp[2]
        if r==N-1 and c==N-1:
            print("Problem %d: %d"%(tcase,nowCost))
            tcase+=1
            break
        if nodeDist[r][c]<nowCost:
            continue
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<N and 0<=tempC<N:
                toCost=nodeDist[r][c]+L[tempR][tempC]
                if toCost<nodeDist[tempR][tempC]:
                    nodeDist[tempR][tempC]=toCost
                    heapq.heappush(dij,[toCost,tempR,tempC])


