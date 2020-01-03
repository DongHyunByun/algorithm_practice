for t in range(int(input())):
    L=list(map(int,input().split()))
    sumSet=set()
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                sumSet.add(L[i]+L[j]+L[k])
    print(f"#{t+1} {sorted(list(sumSet),reverse=True)[4]}")