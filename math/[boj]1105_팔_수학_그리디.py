L,R=input().split()

size=len(R)
L=L.zfill(size)

ans=0
for i in range(size):
    if L[i]==R[i]:
        if L[i]=="8":
            ans+=1
    else:
        break

print(ans)