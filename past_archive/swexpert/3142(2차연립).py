for t in range(int(input())):
    n,m=map(int,input().split())
    unicorn=2*m-n
    twinhorn=n-m
    print(f"#{t+1} {unicorn} {twinhorn}")
