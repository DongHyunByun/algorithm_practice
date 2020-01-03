for t in range(int(input())):
    N,M,K=map(int,input().split())
    L=sorted(list(map(int,input().split())))
    isPossible=True
    for i in L:
        if (i//M)*K < L.index(i)+1:
            isPossible=False
            break
    if isPossible==True:
        print(f"#{t+1} Possible")
    else:
        print(f"#{t+1} Impossible")