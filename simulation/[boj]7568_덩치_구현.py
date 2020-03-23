N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
rankL=[]
for i in range(N):
    up=0
    for j in range(N):
        if i==j:
            continue
        if L[i][0]<L[j][0] and L[i][1]<L[j][1]:
            up+=1
    rankL.append(up+1)
print(*rankL)