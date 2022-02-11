H,W = map(int,input().split())
D = list(map(int,input().split()))

L=[[0 for j in range(W)] for i in range(H)]

for j in range(W):
    for i in range(D[j]):
        L[H-1-i][j]=1

ans=0
for i in range(H):
    op=False
    count_row=0
    for j in range(W):
        if L[i][j]==1:
            if op==True:
                ans += count_row
                count_row=0
            else:
                op = True
        else:
            if op==True:
                count_row+=1
            else:
                continue

print(ans)