for t in range(int(input())):
    ans=0
    for i in range(1,int(input())+1):
        ans=ans+i*((-1)**(i+1))
    print(f"#{t+1} {ans}")