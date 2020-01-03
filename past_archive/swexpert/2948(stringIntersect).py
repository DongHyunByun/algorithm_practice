for t in range(int(input())):
    L1=set()
    L2=set()
    N,M=map(int,input().split())
    L1.update(input().split())
    L2.update(input().split())
    print(f"#{t+1} {len(L1&L2)}")
    
