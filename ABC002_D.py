import io
import sys

_INPUT = """\
6
5 3
1 2
2 3
1 3
5 3
1 2
2 3
3 4
7 9
1 2
1 3
2 3
4 5
4 6
4 7
5 6
5 7
6 7
12 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  G=[[0]*N for _ in range(N)]
  ans=1
  for i in range(M):
    x,y=map(int,input().split())
    x-=1; y-=1
    G[x][y]=1
    G[y][x]=1
  for i in range(1<<N):
    tmp=[j for j in range(N) if (i>>j)%2==1]
    tmp2=0
    for j in tmp:
      tmp2+=sum([G[j][k] for k in tmp])
    if tmp2==len(tmp)**2-len(tmp):
      ans=max(ans,len(tmp))
  print(ans)