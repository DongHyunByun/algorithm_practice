import sys

while(1):
    N,M=map(int,sys.stdin.readline().rstrip().split())
    if N==0 and M==0:
        break
    dp=[[0 for j in range(M)] for i in range(N)]
    L=[]
    for i in range(N):
        L.append(list(map(int,input().split())))

    for i in range(1,N):
        for j in range(1,M):
            if L[i][j]:
                L[i][j]=min(L[i-1][j],L[i][j-1],L[i-1][j-1])+1

    print(max([max(L[i]) for i in range(N)]))
