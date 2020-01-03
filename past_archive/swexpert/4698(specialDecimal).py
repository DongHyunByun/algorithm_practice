from math import sqrt
L=[]
for t in range(int(input())):
    D,A,B=map(int,input().split())
    ans=0
    for i in range(A,B+1):
        if (i==1) or (str(D) not in str(i)) or (i%2==0):
            continue
        isdecimal=True
        for j in range(3,int(sqrt(i))+1,2):
            if i%j==0 :
                isdecimal=False
                break
        if isdecimal==True:
            ans+=1
    L.append(ans)

for k in range(len(L)):
    print(f"#{k+1} {L[k]}")
