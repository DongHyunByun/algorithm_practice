for t in range(10):
    input()
    L=[]
    L.extend(list(map(int,input().split())))

    i=1
    while L[7]>0:
        if i==6:
            i=1
        L[0]-=i

        tem=L[0]
        del L[0]
        L.append(tem)
        i+=1

    L[7]=0
    print(f"#{t+1}",end=" ")
    print(*L)


