for t in  range(int(input())):
    A,B=input().split()
    L=[[0]*(len(A)+1) for i in range((len(B)+1))]
    for i in range(len(B)):
        for j in range(len(A)):
            if B[i]==A[j]:
                L[i+1][j+1]=L[i][j]+1
            else :
                L[i+1][j+1]=max(L[i][j+1],L[i+1][j])
    print(f"#{t+1} {max(max(L))}")

