for t in range(int(input())):
    N,K=map(int,input().split())
    scoreL=sorted(list(map(int,input().split())))
    sum=0
    for i in range(K):
        sum+=scoreL.pop()
    print(f"#{t+1} {sum}")
