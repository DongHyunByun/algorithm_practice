for t in range(int(input())):
    A,B,C=map(int,input().split())
    chipperPrice=min(A,B)
    print(f"#{t+1} {C//chipperPrice}")
