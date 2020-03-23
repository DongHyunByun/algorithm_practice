N,K=map(int,input().split())
L=[]
for i in range(N):
    a,b,c,d=map(int,input().split())
    L.append([b,c,d,a])
L.sort(reverse=True)

for i in range(N):
    if L[i][3]==K:
        rank=i+1
        #동점자 빼기
        for j in range(i-1,-1,-1):
            if L[i][:3]==L[j][:3]:
                rank-=1
            else:
                break
        break
print(rank)