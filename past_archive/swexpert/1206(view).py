for t in range(10):
    hob=[]
    total=0
    len=int(input())
    hob.extend(map(int,input().split()))
    print(hob)
    for j in range(2,len-2):
        round=max(hob[j-2],hob[j-1],hob[j+1],hob[j+2])
        ea=hob[j]-round
        if ea>0:
            total+=ea
    print(f"#{t+1} {total}")
