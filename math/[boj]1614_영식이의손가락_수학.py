x=int(input())
n=int(input())

def main():
    if n==0:
        print(x-1)
        return
    else:
        # 1,5
        if x==1 or x==5:
            print(x-1+8*n)
            return
        # 2,3,4
        else:
            if n%2==0:
                print(x-1+n*4)
            else:
                print(x-1+(n//2)*8+10-2*x)

main()
