N=int(input())
L=list(map(int,input().split()))

size=len(L)

# 1개일때
if size==1:
    print("A")
# 2개일때
elif size==2:
    # 같으면 무조건
    if L[0]==L[1]:
        print(L[0])
    # 다르면 여러개
    else:
        print("A")
# 3개이상일때
else:
    if L[0]==L[1]:
        isPossible=True
        for i in range(2,size):
            if L[i]!=L[i-1]:
                isPossible=False
                break
        if isPossible:
            print(L[0])
        else:
            print("B")

    else:
        a = (L[2] - L[1]) / (L[1] - L[0])
        b = L[1] - L[0] * a

        # a가 정수가 아니면 불가능
        if int(a)!=a:
            print("B")
        # a가 정수면
        else:
            a=int(a)
            b=int(b)
            isPossible=True
            for i in range(3,size):
                if L[i]!=L[i-1]*a+b:
                    isPossible=False
                    break

            if isPossible:
                print(L[size-1]*a+b)
            else:
                print("B")


