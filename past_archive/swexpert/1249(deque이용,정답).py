from collections import deque

def find(L,LL,N):
    myStack=deque([[0,0]])
    while myStack:
        r,c=myStack.popleft()

        #가지치기
        if (LL[r][c]>LL[N-1][N-1]):
            continue

        #상하좌우 이동
        for i in [(0,1),(1,0),(-1,0),(0,-1)]:
            if (r+i[0]<0 or c+i[1]<0 or r+i[0]>=N or c+i[1]>=N):
                continue

            if ( LL[r+i[0]][c+i[1]]==-1 or LL[r+i[0]][c+i[1]] > L[r+i[0]][c+i[1]]+LL[r][c] ):
                LL[r+i[0]][c+i[1]]=LL[r][c]+L[r+i[0]][c+i[1]]
                myStack.append([r+i[0],c+i[1]])              

    return LL[N-1][N-1]
    
    
for t in range(int(input())):
    N=int(input())
    L=[]
    for i in range(N):
        temp=[]
        temp.extend(input())
        L.append(list(map(int,temp)))
    
    LL=[[-1 for i in range(N)] for j in range(N)]
    LL[N-1][N-1]=90000
    LL[0][0]=0

    ans=find(L,LL,N)

    print(f"#{t+1} {ans}")
