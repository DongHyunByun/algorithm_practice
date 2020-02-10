from collections import deque

dR=[0,0,-1,1]
dC=[1,-1,0,0]
M,N,K=map(int,input().split())
L=[[0 for i in range(N)] for j in range(M)]
for i in range(K):
    a,b,c,d=map(int,input().split())
    for R in range(b,d):
        for C in range(a,c):
            L[R][C]=-1

def main():
    ansL=[]
    for i in range(M):
        for j in range(N):
            if L[i][j]!=-1:
                cnt=1
                q=deque([[i,j]])
                L[i][j]=-1
                while(q):
                    temp=q.popleft()
                    r=temp[0]
                    c=temp[1]
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<M and 0<=tempC<N and L[tempR][tempC]!=-1:
                            cnt+=1
                            L[tempR][tempC]=-1
                            q.append([tempR,tempC])
                ansL.append(cnt)
    ansL.sort()
    print(len(ansL))
    print(*ansL)

main()