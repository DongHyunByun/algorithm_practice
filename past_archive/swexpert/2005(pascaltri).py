
A=[]
B=[]
def prt (a):
    for i in range(len(a)):
        print(a[i],end=' ')
    print()

for t in range(int(input())):
    print(f'#{t+1}')
    for i in range(int(input())):
        if i>=2:
            for j in range(1,i):
                B[j]=A[j]+A[j-1]
            B.append(1)
            A=B[:]
            prt(A)

        else :
            A.append(1)
            B=A[:]
            prt(A)
    A.clear()
    B.clear()