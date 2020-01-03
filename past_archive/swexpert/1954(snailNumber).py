for t in range(int(input())):
    N=int(input())
    L=[[0]*N for i in range(N)]
    inirow=0
    inicol=0
    num=1
    for i in range(N,0,-2):
        if i==1:
            L[inirow][inicol]=N**2
            break
        for m in range(i-1):
            L[inirow][inicol+m]=num
            num+=1
        for m in range(i-1):
            L[inirow+m][inicol+i-1]=num
            num+=1
        for m in range(i-1):
            L[inirow+i-1][inicol+i-1-m]=num
            num+=1
        for m in range(i-1):
            L[inirow+i-1-m][inicol]=num
            num+=1
        inirow = inirow+1
        inicol = inicol+1

    print(f"#{t+1}")
    for i in range(N):
        for j in range(N):
            print(L[i][j],end=" ")
        print()