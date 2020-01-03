for t in range(int(input())):
    num=round(int(input())**(1.0/3.0),10)
    print(num)
    if num%1==0:
        print(f"#{t+1} {round(num)}")
    else :
        print(f"#{t+1} -1")
