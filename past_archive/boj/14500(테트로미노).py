from collections import deque

N,M=map(int,input().split())
ans=0
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

dr=[-1,0,0,1]
dc=[0,-1,1,0]


def fuck(L,i,j):
    a=b=c=d=-1
    try:
        a=L[i][j]+L[i][j+1]+L[i][j+2]+L[i-1][j+1]
    except:
        pass
    try:
        b=L[i][j]+L[i][j+1]+L[i][j+2]+L[i+1][j+1]
    except:
        pass
    try:
        c=L[i][j]+L[i+1][j]+L[i+2][j]+L[i+1][j+1]
    except:
        pass
    try:
        d=L[i][j]+L[i][j+1]+L[i-1][j+1]+L[i+1][j+1]
    except:
        pass

    return max(a,b,c,d)

visited=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j]=1
        stack=deque([[i,j,1,L[i][j],-1]])
        while(stack):
            temp=stack.pop()
            r=temp[0]
            c=temp[1]
            for k in range(4):
                if 3-temp[4]==k:
                    continue
                tempR=r+dr[k]
                tempC=c+dc[k]
                if tempR==-1 or tempR==N or tempC==-1 or tempC==M or visited[tempR][tempC]==1:
                    continue
                else:
                    if temp[2]==3:
                        if temp[3]+L[tempR][tempC] > ans:
                            ans=temp[3]+L[tempR][tempC]
                    else:
                        stack.append([tempR,tempC,temp[2]+1,temp[3]+L[tempR][tempC],k])
        tempNum=fuck(L,i,j)
        if tempNum>ans:
            ans=tempNum


print(ans)