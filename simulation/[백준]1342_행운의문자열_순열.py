from itertools import permutations

word=input()
size=len(word)
d={}
for alpha in word:
    if alpha not in d:
        d[alpha]=1
    else:
        d[alpha]+=1

totalD=1
for key in d:
    a=1
    for i in range(1,d[key]+1):
        a*=i
    totalD*=a


per=permutations([i for i in range(size)],size)
ans=0

for tup in per:
    preAlpha=""
    isLuckey=True
    for i in tup:
        if preAlpha==word[i]:
            isLuckey=False
            break
        preAlpha=word[i]

    if isLuckey:
        ans+=1

print(ans//totalD)