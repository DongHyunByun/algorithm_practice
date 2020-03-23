N,M=map(int,input().split())
s=set()

for i in range(N):
    word=input()
    s.add(word)

ans=0
ansS=set()
for j in range(M):
    word = input()
    if word in s:
        ans+=1
        ansS.add(word)
        s.remove(word)

print(ans)
for i in sorted(ansS):
    print(i)