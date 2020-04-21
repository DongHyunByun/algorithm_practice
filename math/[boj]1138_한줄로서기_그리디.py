N=int(input())
L=[0]+list(map(int,input().split()))
ansL=[0 for i in range(N)]

def sit(taller,tall):
    cnt=0
    for i in range(N):
        if ansL[i]==0:
            if cnt==taller:
                ansL[i]=tall
                return
            else:
                cnt+=1
        else:
            continue


for tall in range(1,N+1):
    taller=L[tall]
    sit(taller,tall)
print(*ansL)
