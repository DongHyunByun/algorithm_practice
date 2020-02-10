
N=int(input())
a=N%5
if N==4 or N==7:
    print(-1)
else:
    if a==0:
        print(N//5)
    elif a==1:
        print(N//5+1)
    elif a==2:
        print(N//5+2)
    elif a==3:
        print(N//5+1)
    elif a==4:
        print(N//5+2)


