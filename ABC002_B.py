import io
import sys

_INPUT = """\
6
chokudai
okanemochi
aoki
mazushii
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  ans=[]
  for i in range(len(S)):
    if S[i] not in ['a','i','u','e','o']:
      ans.append(S[i])
  print(*ans,sep='')