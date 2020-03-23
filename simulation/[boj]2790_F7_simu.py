import sys
N=int(input())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline().rstrip()))
L.sort(reverse=True)

ans=1
maxNum=L[0]+1
for i in range(1,N):
    if maxNum<=L[i]+N:
        ans+=1
        maxNum=max(maxNum,L[i]+1+i)
    else:
        break
print(ans)
