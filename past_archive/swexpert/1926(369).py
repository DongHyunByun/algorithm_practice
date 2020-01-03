N = int(input())

for i in range(1,N+1):
    n=str(i).count("3")+str(i).count("6")+str(i).count("9")
    if n==0:
        print(i,end=' ')
    else :
        print(n*"-",end=' ')