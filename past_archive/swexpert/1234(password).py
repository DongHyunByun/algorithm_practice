for t in range(10):
    N,password=input().split()
    passwordL=list(password)
    remove=True
    ans=""
    while remove==True:
        remove=False
        for i in range(len(passwordL)-1):
            if passwordL[i]==passwordL[i+1]:
                del passwordL[i]
                del passwordL[i]
                remove=True
                break
    for i in passwordL:
        ans+=i
    print(f"#{t+1} {ans}")
