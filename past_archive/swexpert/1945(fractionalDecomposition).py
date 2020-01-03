for t in range(int(input())):
    N=int(input())
    print(f"#{t+1}",end="")
    for i in [2,3,5,7,11]:
        k=0
        while N%i==0 :
            N/=i
            k=k+1
        print("",k,end="")
    print()

