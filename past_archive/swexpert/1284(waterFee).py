for t in range(int(input())):
    [P,Q,R,S,W]=list(map(int,input().split()))
    costA=P*W
    if W<=R:
        costB=Q
    else :
        costB=Q+(W-R)*S
    if costA>costB:
        print(f"#{t+1} {costB}")
    else :
        print(f"#{t+1} {costA}")