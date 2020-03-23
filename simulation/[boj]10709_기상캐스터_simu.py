H,W=map(int,input().split())
L=[]
for i in range(H):
    L.append(list(input()))

visited=[[-1 for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if L[i][j]=="c":
            visited[i][j]=0

for i in range(H):
    for j in range(W-1):
        if visited[i][j]==-1:
            continue
        elif visited[i][j+1]!=0:
                visited[i][j+1]=visited[i][j]+1

for i in range(H):
    for j in range(W):
        print(visited[i][j],end=" ")
    print()


