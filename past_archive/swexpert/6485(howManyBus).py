for t in range(int(input())):
    b=[]
    numOfBus=[0 for i in range(5000)] #n정류장의 index는 n-1
    for n in range(int(input())):
        [A,B]=list(map(int,input().split()))
        for i in range(A,B+1):
            numOfBus[i-1]+=1
    
    for P in range(int(input())):
        b.append( numOfBus[int(input())-1] )
    print(f"#{t+1}",end=" ")
    print(*b)
