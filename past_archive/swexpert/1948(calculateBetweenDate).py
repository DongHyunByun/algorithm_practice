for t in range(int(input())):
    between=0
    day=[31,28,31,30,31,30,31,31,30,31,30,31]  # m달의 날짜는 m-1인덱스의 값
    [m1,d1,m2,d2]=list(map(int,input().split()))
    if m1!=m2:
        for i in range(m1,m2-1):
            between=between+day[i]
        print(f"#{t+1} {between+d2+(day[m1-1]-d1+1)}")
    else:
        print(f"#{t+1} {d2-d1+1}")