def euclidean(a,b):
    if b==0:
        return a
    else:
        return euclidean(b,a%b)

N,M=map(int,input().split())
print(M-euclidean(N,M))
