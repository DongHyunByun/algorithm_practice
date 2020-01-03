for t in range(int(input())):
    N=int(input())
    L=input().split()
    print(f"#{t+1}",end="")
    if N%2==0:
        k=int(N/2)
        for i in range(k):
            print("",L[i],end="")
            print("",L[i+k],end="")
        print("")
    else:
        K=int(N/2)
        for i in range(K):
            print("",L[i],end="")
            print("",L[i+K+1],end="")
        print("",L[K])