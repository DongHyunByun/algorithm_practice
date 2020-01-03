for t in range(int(input())):
    N=int(input())
    b=[]
    a=list(map(int,input().split()))
    for i in range(N-1):
        b.append(a[i+1]-a[i])
    maxOfUp=max(b)
    maxOfDown=min(b)
    if maxOfUp<0:
        maxOfUp=0
    if maxOfDown>0:
        maxOfDown=0
    print(f"#{t+1} {maxOfUp} {-maxOfDown}")
