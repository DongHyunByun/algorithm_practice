import math
N=int(input())
sqrtN=int(math.sqrt(N))
ans=N-1
for i in range(2,sqrtN+1):
    if N%i==0:
        num=N//i
        ans=N-num
        break
print(ans)
