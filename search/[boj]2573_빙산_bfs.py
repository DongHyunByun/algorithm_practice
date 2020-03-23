from collections import deque

N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

dR=[0,0,-1,1]
dC=[1,-1,0,0]

def melt():
    sub=[[0 for j in range(M)] for i in range(N)]
    # 주변에 바다가 몇개인지 저장
    for i in range(N):
        for j in range(M):
            if L[i][j]!=0:
                cntSea=0
                for k in range(4):
                    tempR=i+dR[k]
                    tempC=j+dC[k]
                    if 0<=tempR<N and 0<=tempC<M and L[tempR][tempC]==0:
                        cntSea+=1
                sub[i][j]=cntSea

    #주변바다만큼 빼줌
    for i in range(N):
        for j in range(M):
            if L[i][j]!=0:
                if L[i][j]<sub[i][j]:
                    L[i][j]=0
                else:
                    L[i][j]-=sub[i][j]

def cnt():
    ans=0
    visited=[[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if L[i][j]!=0 and visited[i][j]==0:
                ans+=1
                q=deque([[i,j]])
                visited[i][j]=1
                while(q):
                    temp=q.popleft()
                    r=temp[0]
                    c=temp[1]
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<N and 0<=tempC<M and L[tempR][tempC]!=0 and visited[tempR][tempC]==0:
                            visited[tempR][tempC]=1
                            q.append([tempR,tempC])
    return ans

def main():
    ans=0
    time=0
    while(1):
        time+=1
        melt()
        numOfIce=cnt()
        if numOfIce>=2:
            ans=time
            break
        elif numOfIce==0:
            break
    print(ans)



main()
