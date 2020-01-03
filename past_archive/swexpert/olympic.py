for t in range(int(input())):
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    ansL=[0 for i in range(len(A))]
    for i in range(len(B)) :
        for j in range(len(A)):
            if (A[j]<=B[i]):                
                ansL[j]+=1
                break
            else:
                continue
    
    print(f"#{t+1} {ansL.index(max(ansL))+1}")