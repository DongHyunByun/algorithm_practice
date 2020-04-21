import sys

N=int(input())
word=[[] for i in range(51)]
for _ in range(N):
    temp=sys.stdin.readline().rstrip()
    size=len(temp)
    if temp not in word[size]:
        word[size].append(temp)

for i in range(1,51):
    word[i].sort()
    for x in word[i]:
        print(x)



