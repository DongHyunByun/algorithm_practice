def smallerDecimalList(num):
    from math import sqrt
    L=[2,3,5]
    for i in range(7,num+1,2):
        L.append(i)
        for j in range(3,int(sqrt(i))+1,2):
            if i%j==0:
                del L[len(L)-1]
                break
    return L

def pickThree(L):
    ans=0
    lenOfL=len(L)
    for i in range(lenOfL):
        for j in range(i,lenOfL):
            for k in range(j,lenOfL):
                if L[i]+L[j]+L[k]==N:
                    ans+=1
    return ans

for t in range(int(input())):
    N=int(input())
    print(f"#{t+1} {pickThree(smallerDecimalList(N))}")
    