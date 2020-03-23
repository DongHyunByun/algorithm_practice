N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(3):
        L[i][j]+=min(L[i-1][j-1],L[i-1][(j+1)%3])

print(min(L[N-1]))