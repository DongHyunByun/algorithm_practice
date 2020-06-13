L,U=input().split()
U="0"+U
size=len(U)
L=L.zfill(size)
ans=[0 for i in range(10)]

for i in range(1,size):
    #print(i,"번째자리 구하기")
    b=int(U[i])
    a=int(L[i])
    u=int(U[:i])
    l=int(L[:i])
    if i!=size-1:
        u2=int(U[i + 1:])
        l2=int(L[i+1:])
    else:
        u2=l2=0
    n = size - 1 - i
    #print(u,b,u2)
    #print(l,a,l2)
    for k in range(1,10):
        #print(k,"숫자가 몇번나올까")
        if u!=l:
            #기본
            ans[k]+=(u-l-1)*(10**n)
            #U관련
            if k==b:
                ans[k]+=u2+1
            elif k<b:
                ans[k]+=10**n
            #L관련
            if a==k:
                ans[k]+=10**n-l2
            elif a<k:
                ans[k]+=10**n
        else:
            if a==k and b!=k:
                ans[k]+=10**n-l2
            elif a!=k and b==k:
                ans[k]+=u2+1
            elif a==k and b==k:
                ans[k]+=u2-l2+1
            elif a<k<b:
                ans[k]+=10**n
        #print(ans)

print(ans)
finAns=0
for i in range(10):
    finAns+=ans[i]*i
print(finAns)



