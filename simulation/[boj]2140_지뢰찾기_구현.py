dR=[-1,-1,-1,0,0,1,1,1]
dC=[-1,0,1,-1,1,-1,0,1]

def cheak(r,c):
    global ans
    #0이 있으면 바로 종료
    for i in range(8):
        if L[r+dR[i]][c+dC[i]]=='0':
            ans-=1
            return

    #0이 없으면 주변 숫자들 내려
    for i in range(8):
        if L[r+dR[i]][c+dC[i]]!='#':
            L[r+dR[i]][c+dC[i]]=str(int(L[r+dR[i]][c+dC[i]])-1)

N=int(input())
L=[]
for i in range(N):
    L.append(list(input()))

ans=(N-2)*(N-2)

if N<=2:
    print(0)
else:
    for i in range(1,N-1):
        for j in range(1,N-1):
            if (i==1 or i==N-2 or j==1 or j==N-2):
                cheak(i,j)
    print(ans)