N=int(input())
L=[]
for i in range(N):
    L.append(int(input()))

findNum=N
ans=0
for i in range(N-1,-1,-1):
    if L[i]==findNum:
        findNum-=1
    else:
        ans+=1

print(ans)