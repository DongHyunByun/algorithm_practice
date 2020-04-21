from collections import deque
T=int(input())
dR=[0,0,-1,1]
dC=[1,-1,0,0]

for t in range(T):
    N=int(input())
    atomD=deque([])D
    for i in range(N):
        x,y,d,k=map(int,input().split())
        r=2*x+2000
        c=2*y+2000
        atomD.append([i,r,c,d,k])
    ans=0
    while(atomD):
        cheakD={}
        size=len(atomD)
        #원자 움직이기
        for _ in range(size):
            #원래있던곳 삭제
            atomNum,r,c,d,k=atomD.popleft()
            #새로갈곳 찾아서 옮기기
            tempR = r + dR[d]
            tempC = c + dC[d]
            if 0<=tempR<4001 and 0<=tempC<4001:
                atomD.append([atomNum,tempR,tempC,d,k])
                if (tempR,tempC) in cheakD:
                    cheakD[(tempR,tempC)].append([atomNum,d,k])
                else:
                    cheakD[(tempR,tempC)]=[[atomNum,d,k]]

        #부딪힌곳 있는지 확인
        for tup in cheakD:
            if len(cheakD[tup])>=2:
                for atomNum,d,k in cheakD[tup]:
                    atomD.remove([atomNum,tup[0],tup[1],d,k])
                    ans+=k

    print("#%d %d"%(t+1,ans))
