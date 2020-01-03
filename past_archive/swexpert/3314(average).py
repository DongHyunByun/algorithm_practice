for t in range(int(input())):
    L=list(map(int,input().split()))
    sum=0
    for i in L:
        if i<40:
            sum+=40
        else :
            sum+=i
    print(f"#{t+1} {sum//5}")

