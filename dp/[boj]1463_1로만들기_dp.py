INF=9876543210
N=int(input())
L=[0 for i in range(N+1)]


for i in range(N-1,0,-1):
    a=3*i
    b=2*i
    c=i+1
    if a>N:
        tempA=INF
    else:
        tempA=L[a]
    if b>N:
        tempB=INF
    else:
        tempB=L[b]
    if c>N:
        tempC=INF
    else:
        tempC=L[c]

    L[i]=min(tempA,tempB,tempC)+1

print(L[1])