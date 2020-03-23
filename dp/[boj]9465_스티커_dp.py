T=int(input())
for t in range(T):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    dpX=[0 for i in range(n+2)]
    dpY=[0 for i in range(n+2)]
    for i in range(2,n+2):
        dpX[i]=max(dpY[i-1],dpX[i-2],dpY[i-2])+x[i-2]
        dpY[i]=max(dpX[i-1],dpX[i-2],dpY[i-2])+y[i-2]
    print(max(dpX[n+1],dpY[n+1]))
