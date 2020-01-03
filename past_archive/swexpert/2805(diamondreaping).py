for t in range(int(input())):
    N=int(input())
    L=[]
    for i in range(N):
        L.extend(input().split())
    mid=N//2
    uppersum=0
    lowersum=0
    middle=0

    for i in range(0,mid):
        for j in range(mid-i,mid+i+1):
            uppersum+=int(L[i][j])

    for i in range(mid+1,N):
        for j in range(mid-(len(L)-i-1),mid+(len(L)-i-1)+1):
            lowersum+=int(L[i][j])

    for i in range(N):
        middle+=int(L[mid][i])
    sum=uppersum+lowersum+middle
    print(f"#{t+1} {sum}")
