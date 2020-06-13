N=int(input())
d1=[0 for i in range(N)]
d2=[0 for i in range(N)]
d3=[0 for i in range(N)]
d1[0]=d2[0]=d3[0]=1

for i in range(1,N):
    d1[i]=(d2[i-1]+d3[i-1])%9901
    d2[i]=(d1[i-1]+d3[i-1])%9901
    d3[i]=(d1[i-1]+d2[i-1]+d3[i-1])%9901

print((d1[N-1]+d2[N-1]+d3[N-1])%9901)