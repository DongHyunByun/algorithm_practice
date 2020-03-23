import sys

N,M=map(int,input().split())
dic1={}
dic2={}

for i in range(N):
    name=sys.stdin.readline().rstrip()
    dic1[name]=i+1
    dic2[i+1]=name
for i in range(M):
    temp=sys.stdin.readline().rstrip()
    try:
        print(dic2[int(temp)])
    except:
        print(dic1[temp])
