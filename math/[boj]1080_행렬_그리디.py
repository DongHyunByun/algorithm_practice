N,M=map(int,input().split())
A=[]
for i in range(N):
    A.append(list(input()))
B=[]
for i in range(N):
    B.append(list(input()))

reverseD={"1":"0","0":"1"}
def rever(r,c):
    for i in range(3):
        for j in range(3):
            A[r+i][c+j]=reverseD[A[r+i][c+j]]

ans=0
for i in range(0,N-2):
    for j in range(0,M-2):
        if A[i][j]!=B[i][j]:
            ans+=1
            rever(i,j)

if A==B:
    print(ans)
else:
    print(-1)