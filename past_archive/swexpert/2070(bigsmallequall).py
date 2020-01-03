T=int(input())

for i in range(T):
    a,b=map(int,input().split())
    print('#'+str(i+1),end='')
    if a>b :
        print(' >')
    elif a<b :
        print(' <')
    else:
        print(' =')
    