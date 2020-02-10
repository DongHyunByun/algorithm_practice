import heapq

dR=[0,0,-1,1]
dC=[1,-1,0,0]

M,N=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(input()))

maxNum=9876543210
nodeDist=[[maxNum for j in range(M)] for i in range(N)]
nodeDist[0][0]=0
dij=[[0,0,0]]
heapq.heapify((dij))
while(dij):
    #print(dij)
    temp=heapq.heappop(dij)
    crush=temp[0]
    r=temp[1]
    c=temp[2]

    if r==N-1 and c==M-1:
        print(crush)
        break

    if nodeDist[r][c]<crush:
        continue

    for i in range(4):
        tempR=r+dR[i]
        tempC=c+dC[i]
        if 0<=tempR<N and 0<=tempC<M:
            if L[tempR][tempC]=="1":
                w=crush+1
            else:
                w=crush
            if nodeDist[tempR][tempC]>w:
                nodeDist[tempR][tempC]=w
                heapq.heappush(dij,[w,tempR,tempC])