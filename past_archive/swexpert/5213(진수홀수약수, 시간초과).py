for t in range(int(input())):
    L,R=map(int,input().split())
    total=0
    for i in range(L,R+1):
        ans=0
        for j in range(1,i+1):
            if (j%2!=0) and (i%j==0):
                ans+=j
        total+=ans
    print(f"#{t+1} {total}")
