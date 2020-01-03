def rsp (a,b):
    if ((a==1) and (b==3)) or((a==2) and (b==1)) or((a==3)and(b==2)) :
        return('A')
    else :
        return('B')

x=list(map(int,input().split()))
print(rsp(x[0],x[1]))