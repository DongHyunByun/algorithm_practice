from collections import deque

K=int(input())
W,H=map(int,input().split())
L=[]
for i in range(H):
    L.append(list(map(int,input().split())))

dR=[0,0,-1,1]
dC=[1,-1,0,0]
dhR=[-1,-2,-2,-1,1,2,2,1]
dhC=[-2,-1,1,2,2,1,-1,-2]

cL=[[[0 for k in range(K+1)] for j in range(W)] for i in range(H)]
for i in range(K+1):
    cL[0][0][i]=1

ans=0
q=deque([[0,0,0]])
while(q):
    temp=q.popleft()
    r=temp[0]
    c=temp[1]
    h=temp[2]
    if r==H-1 and c==W-1:
        ans=cL[r][c][h]
        break

    # 인접칸이동
    for d in range(4):
        tempR=r+dR[d]
        tempC=c+dC[d]
        if 0<=tempR<H and 0<=tempC<W and L[tempR][tempC]==0 and cL[tempR][tempC][h]==0:
            cL[tempR][tempC][h]=cL[r][c][h]+1
            q.append([tempR,tempC,h])
    # 말뛰기
    if h!=K:
        for k in range(8):
            tempR=r+dhR[k]
            tempC=c+dhC[k]
            if 0<=tempR<H and 0<=tempC<W and L[tempR][tempC]==0 and cL[tempR][tempC][h+1]==0:
                cL[tempR][tempC][h+1]=cL[r][c][h]+1
                q.append([tempR,tempC,h+1])

'''
#값확인
for i in range(H):
    print(cL[i])
'''

print(ans-1)