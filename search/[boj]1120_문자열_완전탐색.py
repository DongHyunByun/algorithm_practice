A,B=input().split()
sizeA=len(A)
sizeB=len(B)
sub=sizeB-sizeA

ans=51
for i in range(sub+1):
    sum=0
    for k in range(sizeA):
        if A[k]!=B[i+k]:
            sum+=1
    ans=min(sum,ans)

print(ans)