for t in range(int(input())):
    D,H,M=map(int,input().split())
    if M<11:
        ansM=60+M-11
        H-=1
    else : 
        ansM=M-11
    if H<11:
        ansH=24+H-11
        D-=1
    else : 
        ansH=H-11
    if D<11:
        print(f"#{t+1} -1")
        continue
    else: 
        ansD=D-11
    print(f"#{t+1} {ansM+ansH*60+ansD*60*24}")
