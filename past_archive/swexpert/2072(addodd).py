n = int(input())
for i in range(n) :
       print(f'#{i+1} {sum(map(lambda x: x if x%2 == 1 else 0  ,map(int,input().split())))}')