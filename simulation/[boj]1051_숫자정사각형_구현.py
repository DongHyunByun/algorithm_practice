import sys

N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(input())

minNum=min(N,M)

ans=1
for size in range(minNum,1,-1):
    for i in range(N-size+1):
        for j in range(M-size+1):
            if (L[i][j]==L[i+size-1][j]==L[i][j+size-1]==L[i+size-1][j+size-1]):
                print(size*size)
                sys.exit()
print(ans)